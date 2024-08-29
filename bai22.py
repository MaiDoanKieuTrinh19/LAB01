# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 10:24:44 2024

@author: Hi
"""
print('Giải phương trình bậc nhât ax+b=0 ')
a=float(input('Nhập a= '))
b=float(input('Nhập b= '))
if a==0 and b==0:
    print('Phương trình vô số nghiệm ')
elif a==0 and b!=0:
    print('Phương trình vô nghiệm ')
elif a!=0:
    x=-b/a
    print('Phương trình có nghiệm x=',x)
else:
    print('Không xác định')
