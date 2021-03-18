# -*- coding: UTF-8 -*-
# @Time    : 2021/3/16 20:17
# @Author  : sen

import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
print('Exit code:', r)