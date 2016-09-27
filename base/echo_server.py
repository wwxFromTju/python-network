#!/usr/bin/env python
# encoding=utf-8

import socket
import sys
import argparse


host = '127.0.0.1'
data_payload = 2048
backlog = 5


def echo_server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = (host, port)
    print('starting up echo server on {} port {}'.format(*server_address))
    sock.bind(server_address)

    sock.listen(backlog)

    while True:
        print('waiting to receive message from client')
        client, address = sock.accept()
        data = client.recv(data_payload)

        if data:
            print('data: {}'.format(data))
            client.send(data)
            print('send {} bytes back to {}'.format(data, address))
        client.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='socket server example')
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_server(port)