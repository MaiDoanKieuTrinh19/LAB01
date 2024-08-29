# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 18:34:51 2024

@author: Student
"""


h1=int(input('Nhập giờ thứ nhất: '))
m1=int(input('Nhập phút thứ nhất: '))
s1=int(input('Nhập giây giờ thứ nhất: '))
h2=int(input('Nhập giờ thứ hai: '))
m2=int(input('Nhập phút thứ hai: '))
s2=int(input('Nhập giây thứ hai: '))
tongs1 = h1*3600+m1*60+s1
tongs2 = h2*3600+m2*60+s2

#cộng hai giờ 
tongsogiay=tongs1+tongs2 
tongG = tongsogiay//3600
tongM = (tongsogiay%3600)//60
tongS = (tongsogiay%3600)%60 
#trừ hai giờ 
hieusogiay= tongs1-tongs2
hieuG = hieusogiay//3600
hieuM = (hieusogiay%3600)//60
hieuS = (hieusogiay%3600)%60 
print(f'Tổng của 2 giờ là: {tongG}:{tongM}:{tongS}')
print(f'Hiệu của 2 giờ là: {hieuG}:{hieuM}:{hieuS}')