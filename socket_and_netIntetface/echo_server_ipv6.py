#!/usr/bin/env python
# encoding=utf-8

import socket
import argparse
import sys

HOST = 'localhost'


def echo_server(port, host=HOST):
    for result in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM, 0, socket.AI_PASSIVE):
        af, socktype, proto, canonname, sa = result
        try:
            sock = socket.socket(af, socktype, proto)
        except socket.error as err:
            print('error: {}'.format(err))

        try:
            sock.bind(sa)
            sock.listen(1)
            print('server lisenting on {}:{}'.format(host, port))
        except socket.error as msg:
            sock.close()
            continue
        break
        sys.exit(1)
    conn, addr = sock.accept()
    print('connected to', addr)

    while True:
        data = conn.recv(1024)
        print('received data from the client: [{}]'.format(data))
        if not data:
            break
        conn.send(data)
        print('sent data echoed back to the client: [{}]'.format(data))
    conn.close()


if __name__ == '__main__':
    parse = argparse.ArgumentParser(description='ipv6 socket server')
    parse.add_argument('--port', action='store', dest='port', type=int, required=True)
    given_args = parse.parse_args()
    port = given_args.port
    echo_server(port)