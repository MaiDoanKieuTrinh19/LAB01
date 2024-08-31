# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:49:47 2024

@author: Hi
"""
#cau a
print('        Câu a ')
a=float(input('Nhập số a= '))
b=float(input('Nhập số b= '))
c=float(input('Nhập số c= '))
if a>b:
    a, b = b, a
if a>c:
    a, c = c, a
if b>c:
    b, c = c, b 
print(f'Thứ tự tăng dần của 3 số trên là {a}, {b}, {c}')
print("===============================================")
#caub 
print('         Câu b ')
a=float(input('Nhập số a= '))
b=float(input('Nhập số b= '))
c=float(input('Nhập số c= '))
d=float(input('Nhập số d= '))
if a>b:
    a,b = b,a
if a>c:
    a,c = c,a
if a>d:
    a,d = d,a
if b>c:
    b,c = c,b
if b>d:
    b,d = d,b
if c>d:
    c,d = d,c
print(f'Thứ tự tăng dần của các số là: {a}, {b}, {c}, {d}')