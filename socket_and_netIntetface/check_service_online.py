#!/usr/bin/env python
# encoding=utf-8

import argparse
import socket
import errno
from time import time as now

# maybe have some error


DEFAULT_TIMEOUT = 120
DEFAULT_SERVER_HOST = 'localhost'
DEFAULT_SERVER_PORT = 80


class NetServiceChecker(object):
    def __init__(self, host, port, timeout=DEFAULT_TIMEOUT):
        self.host = host
        self.port = port
        self.timeout = timeout
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def end_wait(self):
        self.sock.close()

    def check(self):
        if self.timeout:
            end_time = now() + self.timeout

        while True:
            try:
                if self.timeout:
                    next_timeout = end_time - now()
                    if next_timeout < 0:
                        return False
                    else:
                        print('setting socket next timeout {}s'.format(next_timeout))
                        self.sock.settimeout(next_timeout)
                self.sock.connect((self.host, self.port))
            except socket.timeout as err:
                if self.timeout:
                    return False
            except socket.error as err:
                print('exception: {}'.format(err))
            else:
                self.end_wait()
                return True


if __name__ == '__main__':
    parse = argparse.ArgumentParser(description='wait for network service')
    parse.add_argument('--host', action='store', dest='host', default=DEFAULT_SERVER_HOST)
    parse.add_argument('--port', action='store', dest='port', type=int, default=DEFAULT_SERVER_PORT)
    parse.add_argument('--timeout', action='store', dest='timeout', type=int, default=DEFAULT_TIMEOUT)

    given_args = parse.parse_args()
    host = given_args.host
    port = given_args.port
    timeout = given_args.timeout

    service_checker = NetServiceChecker(host, port, timeout=timeout)
    print('checking for network service {}:{}...'.format(host, port))

    if service_checker.check():
        print('service is availanle again!')