#!/usr/bin/env python
# encoding=utf-8

import os
import socket
import threading
import socketserver


SERVER_HOST = 'localhost'
SERVER_PORT = 0
BUF_SIZE = 1024
ECHO_MSG = 'hello echo server!'


class ForkingClient():
    def __init__(self, ip, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((ip, port))

    def run(self):
        current_process_id = os.getppid()
        print('pid {} sending echo message to the server: {}'.format(current_process_id, ECHO_MSG))
        sent_data_length = self.sock.send(bytes(ECHO_MSG, 'utf-8'))
        print('sent: {} characters, so far...'.format(sent_data_length))

        response = self.sock.recv(BUF_SIZE)
        print('PID {} received: {}'.format(current_process_id, response[5:]))

    def shutdown(self):
        self.sock.close()


class ForkingServerRequestHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(BUF_SIZE)
        current_process_id = os.getppid()
        response = '{}: {}'.format(current_process_id, data)
        print('server sending response [current_process_id: data] = [{}]'.format(response))


class ForkingServer(socketserver.ForkingMixIn, socketserver.TCPServer):
    pass


def main():
    server = ForkingServer((SERVER_HOST, SERVER_PORT), ForkingServerRequestHandler)
    ip, port = server.server_address
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.setDaemon(True)
    server_thread.start()
    print('server loop running PID: {}'.format(os.getpid()))

    client1 = ForkingClient(ip, port)
    client1.run()

    client2 = ForkingClient(ip, port)
    client2.run()

    server.shutdown()
    client1.shutdown()
    client2.shutdown()
    server.socket.close()


if __name__ == '__main__':
    main()
