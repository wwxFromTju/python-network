#!/usr/bin/env python
# encoding=utf-8

import socket
import sys
import argparse


host = '127.0.0.1'


def echo_client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = (host, port)
    print('connecting to {} port {}'.format(*server_address))
    sock.connect(server_address)

    try:
        message = b"test message. this will be echoed"
        print('sending {}'.format(message))
        sock.sendall(message)
        amount_received = 0
        amount_expected = len(message)
        while amount_received < amount_expected:
            data = sock.recv(16)
            amount_received += len(data)
            print('received: {}'.format(data))
    except socket.error as e:
        print('socket error {}'.format(str(e)))
    except Exception as e:
        print('other exception: {}'.format(str(e)))
    finally:
        print("closing connectin to the server")
        sock.close()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='socket server example')
    parser.add_argument('--port', action='store', dest='port', type=int, required=True)
    given_args = parser.parse_args()
    port = given_args.port
    echo_client(port)
