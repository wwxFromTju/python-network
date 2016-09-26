#!/usr/bin/env python
# encoding=utf-8

import socket


def block_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setblocking(1)
    s.settimeout(0.5)
    s.bind(('127.0.0.1', 0))

    socket_address = s.getsockname()
    print("trivial launched on socket : {}".format(str(socket_address)))
    while 1:
        s.listen(1)


if __name__ == '__main__':
    block_server()