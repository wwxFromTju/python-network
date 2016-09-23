#!/usr/bin/env python
# encoding=utf-8

import socket


def find_server_name():
    protocalname = "tcp"
    for port in [80, 25]:
        server_name = socket.getservbyport(port, protocalname)
        print("Port: {} => service name: {}".format(port, server_name))

    print("Port: {} => service name: {}".format(53, socket.getservbyport(53, "udp")))


if __name__ == "__main__":
    find_server_name()