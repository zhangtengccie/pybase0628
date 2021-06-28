#!/usr/bin/python3.9
# -*- coding=utf8 -*- 
# Creater:zhangteng

import re

string1 = 'Port-channel1.189     192.168.189.254  YES   CONFIG  up         up   '

result = re.match('([A-Z]\S+\d)\s+(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+\w+\s+\w+\s+(up|down)\s+(up|down)\s+',
                  string1).groups()
# result =  re.match('(\w+\-\w+\.\d+)\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+(\w+)\s+(\w+)\s+(\w+)\s+(\w+)\s+',str1).groups()

string_format = '{:<15}:{}'
str1 = string_format.format('接口', result[0])
str2 = string_format.format('IP地址', result[1])
str3=string_format.format('状态', result[2])
max_len=max(len(str1),len(str2),len(str3))
print('-' * max_len)
print(str1)
print(str2)
print(str3)
