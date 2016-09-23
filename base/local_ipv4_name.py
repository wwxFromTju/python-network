#!/usr/bin/env python
# encoding=utf-8

import socket


def print_ipve_name():
    host_name = socket.gethostname()
    print("host name: {}".format(host_name))

    ip_address = socket.gethostbyname(host_name)
    print("IP address: {}".format(ip_address))


if __name__ == "__main__":
    print_ipve_name()