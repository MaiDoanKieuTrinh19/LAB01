# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:13:02 2024

@author: Hi
"""

a=int(input('Nhập số nguyên a= '))
b=int(input('Nhập số nguyên b= '))
c=int(input('Nhập số nguyên c= '))
d=int(input('Nhập số nguyên d= '))
#giả sửa a là số lớn nhất
lon_nhat=a
if b>a:
    lon_nhat=b
if c>lon_nhat:
    lon_nhat=c
if d>lon_nhat:
    lon_nhat=d
print('Số lớn nhất là: ',lon_nhat)