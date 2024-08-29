# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 09:40:19 2024

@author: Hi
"""

A=input('Nhập giờ phút giây thứ nhất theo định dạng hh:mm:ss : ')
B=input('Nhập giờ phút giây thứ 2 theo định dạng hh:mm:ss : ')
h1,m1,s1=map(int,A.split(':'))
h2,m2,s2=map(int,B.split(':'))
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
