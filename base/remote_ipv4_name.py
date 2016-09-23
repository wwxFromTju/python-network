#!/usr/bin/env python
# encoding=utf-8

import socket

def get_remote_ipv4_name():
    remote_host = "www.zhihu.com"
    try:
        ip_address = socket.gethostbyname(remote_host)
        print("the host: {} \n ip is: {}".format(remote_host, ip_address))
    except socket.error:
        print(socket.error)


if __name__ == "__main__":
    get_remote_ipv4_name()