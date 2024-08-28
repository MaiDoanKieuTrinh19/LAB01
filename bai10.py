# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a=int(input('Nhập số thứ nhất: '))
b=int(input('Nhập số thú hai: '))
c=int(input('Nhập số thứ ba: '))
d=int(input('Nhập số thứ tư: '))
tong=a+b+c+d
if 0<tong<10:
    print('Số nút của xe bạn là: ',tong)
elif tong>=10:
    sonut=tong//10+tong%10
    if sonut>=10:
        sonut=sonut//10+sonut%10
    print('Số nút của xe bạn là: ',sonut)
else:
    print('Không xác định')
    
