#!/usr/bin/env python
# encoding=utf-8

import sys
import socket
import argparse


def main():
    parser = argparse.ArgumentParser(description="socket error examples")
    parser.add_argument('--host', action='store', dest='host', required=False)
    parser.add_argument('--port', action='store', dest='port', type=int, required=False)
    parser.add_argument('--file', action='store', dest='file', required=False)
    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.errno as e:
        print('error creating socket: {}'.format(e))

    try:
        s.connect((host, port))
    except socket.gaierror as e:
        print("address-related error connecting to server: {}".format(e))
        sys.exit(1)

    try:
        s.sendall("GET {} HTTP/1.0 \r\n\r\n".format(filename))
    except socket.error as e:
        print("Error sending data: {}".format(e))
        sys.exit(1)

    while 1:
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print("Error receiving data: {}".format(e))
            sys.exit(1)

        if not len(buf):
            break

        sys.stdout.write(buf)


if __name__ == "__main__":
    main()

