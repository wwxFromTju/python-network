#!/usr/bin/env python
# encoding=utf-8

import socket
import argparse
import netifaces as ni


def inspect_ipv6_support():
    print('ipv6 support built into python: {}'.format(socket.has_ipv6))
    ipv6_addr = {}
    for interface in ni.interfaces():
        all_addresser = ni.ifaddresses(interface)
        print('interface {}:'.format(interface))

        for family, addrs in all_addresser.items():
            fam_name = ni.address_families[family]
            print('address family: {}'.format(fam_name))
            for addr in addrs:
                if fam_name == 'AF_INET6':
                    ipv6_addr[interface] = addr['addr']
                print('address : {}'.format(addr['addr']))
                nmask = addr.get('netmask', None)
                if nmask:
                    print('netmask : {}'.format(nmask))
                bcast = addr.get('broadcast', None)
                if bcast:
                    print('broadcast: {}'.format(bcast))
    if ipv6_addr:
        print('found ipv6 address: {}'.format(ipv6_addr))
    else:
        print('no ipv6 interface found!')


if __name__ == '__main__':
    inspect_ipv6_support()