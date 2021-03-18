# -*- coding: utf-8 -*-
# @Time    : 2021/3/16 20:19
# @Author  : sen

import subprocess

print('$ nslookup')
p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
# print(output.decode('utf-8'))
print(output.decode('gbk'))
print('Exit code:', p.returncode)
