#!/usr/bin/env python
# encoding=utf-8

import argparse
import socket
import sys

HOST = 'localhost'
BUFSIZE = 1024


def ipv6_echo_client(port, host=HOST):
    for res in socket.getaddrinfo(host, port, socket.AF_UNSPEC, socket.SOCK_STREAM):
        af, socktype, proto, canonname, sa = res
        try:
            sock = socket.socket(af, socktype, proto)
        except socket.error as err:
            print('error : {}'.format(err))

        try:
            sock.connect(sa)
        except socket.error as msg:
            sock.close()
            continue

    if sock is None:
        print('failed to open socket!')

    msg = b'hello from ipv6 client'
    print('send data to server: {}'.format(msg))
    sock.send(msg)

    while True:
        data = sock.recv(BUFSIZE)
        print('received from server', repr(data))
        if not data:
            break

    sock.close()


if __name__ == '__main__':
    parse = argparse.ArgumentParser(description='ipv6 socket client')
    parse.add_argument('--port', action='store', dest='port', type=int, required=True)
    given_args = parse.parse_args()
    port = given_args.port
    ipv6_echo_client(port)