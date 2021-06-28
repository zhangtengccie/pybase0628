#!/usr/bin/python3.9
# -*- coding=utf8 -*- 
# Creater:zhangteng

department1 = 'Security'
department2 = 'Python'
depart1_m = 'cq_bomb'
depart2_m = 'qinke'
COURSE_FEES_SEC = 456789.123456
COURSE_FEES_Python = 1234.3456

# 格式化字符串
line1 = f'Department1 name:{department2:10} Manager:{depart2_m:10} COURSE FEES:{COURSE_FEES_Python:<10.2f} THE END!'
line2 = f'Department2 name:{department1:10} Manager:{depart1_m:10} COURSE FEES:{COURSE_FEES_SEC:<10.2f} THE END!'

# 新方法格式化
line1 ='Department1 name:{department1:10} Manager:{depart1_m:10} COURSE FEES:{COURSE_FEES_SEC:<10.2f} THE END!'.format(department1=department1,depart1_m=depart1_m,COURSE_FEES_SEC=COURSE_FEES_SEC)
line2 ='Department2 name:{department2:10} Manager:{depart2_m:10} COURSE FEES:{COURSE_FEES_Python:<10.2f} THE END!'.format(department2=department2,depart2_m=depart2_m,COURSE_FEES_Python=COURSE_FEES_Python)

# 传统方法格式化
line1 = 'Department1 name:%-10s Manager:%-10s COURSE FEES:%-10.2f THE END!' % (department1, depart1_m, COURSE_FEES_SEC)
line2 = 'Department2 name:%-10s Manager:%-10s COURSE FEES:%-10.2f THE END!' % (department2, depart2_m, COURSE_FEES_Python)

lenght = len(line1)
print('=' * lenght)
print(line1)
print(line2)
print('=' * lenght)
