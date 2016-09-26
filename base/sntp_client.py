#!/usr/bin/env python
# encoding=utf-8

# not run


import socket
import struct
import sys
import time


NTP_SERVER = '0.uk.pool.ntp.org'
TIME1970 = 2208988800


def sntp_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    data = b"\x1b" + 47 * b'\0'
    client.sendto(data, (NTP_SERVER, socket.SOCK_DGRAM))
    data, address = client.recvfrom(1024)

    if data:
        print('response received from:', address)
    t = struct.unpack('!12I', data)[10]
    t -= TIME1970
    print('\tTime={}'.format(time.ctime(t)))


if __name__ == '__main__':
    sntp_client()