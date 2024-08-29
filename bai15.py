# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 09:25:44 2024

@author: Hi
"""
import math 
a=float(input('Nhập số a= '))
b=float(input('Nhập số b= '))
A=(a+b)/(math.pow(a,1/3)+math.pow(b,1/3))
B=(math.pow(a,1/3)-math.pow(b,1/3))**1/2
giatri=A/B
print('Giá trị của biểu thức A là: ', giatri)
