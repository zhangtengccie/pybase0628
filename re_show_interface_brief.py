import re

# 标准作业接讲解
string1 = 'Port-channel1.189     192.168.189.254  YES   CONFIG  up   up   '

re_result = re.match(r'(\w\S+\d)\s+(\d{1,3}.\d{1,3}.\d{1,3}.\d{1,3})\s+\w+\s+\w+\s+(up|down)\s+\w',
                     string1.strip()).groups()
# print(re_result)

fromat_str = '{0:<10}:{1:<30}'
print(fromat_str.format('接口', re_result[0]))
print(fromat_str.format('IP地址', re_result[1]))
print(fromat_str.format('状态', re_result[2]))
