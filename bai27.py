# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 16:36:44 2024

@author: Hi
"""

hinh=float(input('Nhập hình với 1- hình vuông, 2-hình chữ nhật,  3-hình tròn: '))
if hinh==1:
    canh=float(input('Nhập chiều dài cạnh của hình vuông: '))
    S=canh**2
    print('Diện tích hình vuông là: ',S)
    P=canh*4
    print('Chu vi hình vuông là: ',P)
elif hinh==2:
    CD=float(input('Nhập chiều dài hình chữ nhật: '))
    CR=float(input('Nhập chiều rộng hình chữ nhật: '))
    S=CD*CR
    print('Diện tích hình chữ nhật là: ',S)
    P=(CD+CR)*2
    print('Chu vi hình chữ nhật là: ',P)
elif hinh==3:
    r=float(input('Nhập bán kính hình chữ nhật: '))
    pi=3.14
    S=r**2*pi
    print('Diện tích hình tròn là: ',S)
    P=2*r*pi
    print('Chu vi hình trong là: ',P)
else:
    print('Không xác định được hình')
    