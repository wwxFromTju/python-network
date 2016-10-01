#!/usr/bin/env python
# encoding=utf-8

import socket
import sys

SERVER_PATH = '/tmp/python_unix_socket_server'


def domain_socket_client():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)

    server_address = SERVER_PATH
    print('connecting to {}'.format(server_address))
    try:
        sock.connect(server_address)
    except socket.error as msg:
        print(msg, file=sys.stderr)
        sys.exit(1)

    try:
        message = b'this is the message. this will be echoed back!'
        print('sending [{}]'.format(message))
        sock.sendall(message)
        amount_received = 0
        amount_expected = len(message)

        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('received [{}]'.format(data))
    finally:
        print('closing client')
        sock.close()


if __name__ == '__main__':
    domain_socket_client()