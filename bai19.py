# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:04:16 2024

@author: Hi
"""

a=int(input('Nhập số nguyên a= '))
b=int(input('Nhập số nguyên b= '))
c=int(input('Nhập số nguyên c= '))
d=int(input('Nhập số nguyên d= '))
#giả sửa a là số nhỏ nhất
nho_nhat=a
if b<a:
    nho_nhat=b
if c<nho_nhat:
    nho_nhat=c
if d<nho_nhat:
    nho_nhat=d
print('Số nhỏ nhất là: ',nho_nhat)
