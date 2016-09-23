#!/usr/bin/env python
# encoding=utf-8

import socket
from binascii import hexlify


def convert_ipv4_address_hex():
    for ip_address in ["127.0.0.1", '192.168.0.1']:
        packed_ip_addr = socket.inet_aton(ip_address)
        unpacked_ip_addr = socket.inet_ntoa(packed_ip_addr)
        print("IP Address: {}=> Packed: {}, Unpacked: {}".format(ip_address, hexlify(packed_ip_addr), unpacked_ip_addr))


if __name__ == "__main__":
    convert_ipv4_address_hex()