# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:48:14 2024

@author: Student
"""

a=input('Nhập một chữ bất kì: ')
if a.isupper():
    b=a.lower()
    print('Chữ viết thường của chữ đã nhập là: ',b)
elif a.islower():
    b=a.upper()
    print('Chữ viết hoa của chữ đã nhập là: ',b)