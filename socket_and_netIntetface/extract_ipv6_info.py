#!/usr/bin/env python
# encoding=utf-8

import socket
import netifaces as ni
import netaddr as na


def extract_ipv6_info():
    print('ipv6 support built into python: {}'.format(socket.has_ipv6))
    for interface in ni.interfaces():
        all_addresses = ni.ifaddresses(interface)
        print('interface {}:'.format(interface))
        for family, addrs in all_addresses.items():
            fam_name = ni.address_families[family]
            for addr in addrs:
                if fam_name == 'AF_INET6':
                    addr = addr['addr']
                    has_eth_string = addr.split('%eth')
                    if has_eth_string:
                        addr = addr.split('%eth')[0]
                    print('IP Address: {}'.format(na.IPNetwork(addr)))
                    print('IP Version: {}'.format(na.IPNetwork(addr).version))
                    print('IP Prefix length: {}'.format(na.IPNetwork(addr).prefixlen))
                    print('Network: {}'.format(na.IPNetwork(addr).network))
                    print('Broadcast: {}'.format(na.IPNetwork(addr).broadcast))


if __name__ == '__main__':
    extract_ipv6_info()