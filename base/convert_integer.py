#!/usr/bin/env python
# encoding=utf-8

import socket

def convert_integer():
    data = 1234

    # 32-bits, n:network, h:host l:long
    host_byte_32 = socket.ntohl(data)
    net_byte_32 = socket.htonl(data)
    print("Original: {} => Long host byte order: {}, network byte order: {}".format(data, host_byte_32, net_byte_32))

    # 16-bits, 和上面的一样
    host_byte_16 = socket.ntohs(data)
    net_byte_16 = socket.htons(data)
    print("Original: {} => short host byte order: {}, network byte order: {}".format(data, host_byte_16, net_byte_16))


if __name__ == "__main__":
    convert_integer()