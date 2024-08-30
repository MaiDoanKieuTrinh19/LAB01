# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:04:16 2024

@author: Hi
"""

a=int(input('Nhập số nguyên a= '))
b=int(input('Nhập số nguyên b= '))
c=int(input('Nhập số nguyên c= '))
d=int(input('Nhập số nguyên d= '))
if a<b and a<c and a<d:
    print(f'Số nhỏ nhất là {a}')
elif b<a and b<c and b<d:
    print(f'Số nhỏ nhất là {b}')
elif c<a and c<b and c<d:
    print(f'Số nhỏ nhất là {c}')
else:
    print(f'Số nhỏ nhất là {d}')
