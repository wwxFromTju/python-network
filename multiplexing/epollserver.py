#!/usr/bin/env python
# encoding=utf-8

import socket
import select
import argparse


SERVER_HOST = 'localhost'

EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
SERVER_RESPONSE = b"""HTTP/1.1 200 OK\r\nDate: Mon, 1 Apr 2013 01:01:01
GMT\r\nContent-Type: text/plain\r\nContent-Length: 25\r\n\r\n
Hello from epoll server!
"""


class EpollServer(object):
    def __init__(self, host=SERVER_HOST, port=0):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((host, port))
        self.sock.listen(1)
        self.sock.setblocking(0)
        self.sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
        print('started epoll server')
        self.epoll = select.poll()
        self.epoll.register(self.sock.fileno(), select.POLLIN)

    def run(self):
        try:
            connections = {}
            requests = {}
            responses = {}

            while True:
                events = self.epoll.poll(1)
                for fileno, event in events:
                    if fileno == self.sock.fileno():
                        connection, address = self.sock.accept()
                        connection.setblocking(0)
                        self.epoll.register(connection.fileno(), select.POLLIN)
                        connections[connection.fileno()] =connection
                        requests[connection.fileno()] = b''
                        responses[connection.fileno()] = SERVER_RESPONSE
                    elif event & select.POLLIN:
                        requests[fileno] += connections[fileno].recv(1024)
                        if EOL1 in requests[fileno] or EOL2 in requests[fileno]:
                            self.epoll.modify(fileno, select.POLLOUT)
                            print('-' * 40 + '\n' + requests[fileno].decode()[:-2])
                    elif event & select.POLLOUT:
                        byteswritten = connections[fileno].send(responses[fileno])
                        responses[fileno] = responses[fileno][byteswritten:]
                        if len(responses[fileno]) == 0:
                            self.epoll.modify(fileno, 0)
                            connections[fileno].shutdown(socket.SHUT_RDWR)
                        elif event & select.POLLHUP:
                            self.epoll.unregiser(fileno)
                            connections[fileno].close()
                            del connections[fileno]

        finally:
            self.epoll.unregiser(self.sock.fileno())
            self.epoll.close()
            self.sock.close()


if __name__ == '__main__':
    parse = argparse.ArgumentParser(description='socket server example with poll')
    parse.add_argument('--port', action='store', dest='port', type=int, required=True)
    given_args = parse.parse_args()
    port = given_args.port
    server = EpollServer(host=SERVER_HOST, port=port)
    server.run()
