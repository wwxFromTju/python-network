#!/usr/bin/env python
# encoding=utf-8

import socket


def socket_time():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("default timeout: {}".format(s.gettimeout()))
    s.settimeout(100)
    print("set the new timeout: {}".format(s.gettimeout()))


if __name__ == '__main__':
    socket_time()