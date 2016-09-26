#!/usr/bin/env python
# encoding=utf-8

import sys
import socket


def reuser_socket_addr():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    old_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print('old sock state: {}'.format(old_state))

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    new_state = sock.getsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR)
    print('new sock state: {}'.format(new_state))

    local_port = 8282

    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind(('', local_port))
    srv.listen(1)
    print('listening on port: {}'.format(local_port))

    while True:
        try:
            connection, addr = srv.accept()
            print('connected by {}:{}'.format(addr[0], addr[1]))
        except KeyboardInterrupt:
            break
        except socket.error as msg:
            print('{}'.format(msg))


if __name__ == '__main__':
    reuser_socket_addr()