#!/usr/bin/env python
# encoding=utf-8

import subprocess
import shlex


command_line = 'ping -c 1 www.baidu.com'
args = shlex.split(command_line)

try:
    subprocess.check_call(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print('baidu web server is up!')
except subprocess.CalledProcessError:
    print('failed to get ping.')