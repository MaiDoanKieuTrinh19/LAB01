# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:54:46 2024

@author: Student
"""
hinh=input('Nhập hình với v- hình vuông, n-hình chữ nhật, t- hình tròn: ')
if hinh=='v':
    canh=float(input('Nhập chiều dài cạnh của hình vuông: '))
    S=canh**2
    print('Diện tích hình vuông là: ',S)
    P=canh*4
    print('Chu vi hình vuông là: ',P)
elif hinh=='n':
    CD=float(input('Nhập chiều dài hình chữ nhật: '))
    CR=float(input('Nhập chiều rộng hình chữ nhật: '))
    S=CD*CR
    print('Diện tích hình chữ nhật là: ',S)
    P=(CD+CR)*2
    print('Chu vi hình chữ nhật là: ',P)
elif hinh=='t':
    r=float(input('Nhập bán kính hình chữ nhật: '))
    pi=3.14
    S=r**2*pi
    print('Diện tích hình tròn là: ',S)
    P=2*r*pi
    print('Chu vi hình trong là: ',P)
else:
    print('Không xác định')    

    
    
    
