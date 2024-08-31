# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 14:51:14 2024

@author: MaiDoanKieuTrinh-23732851
"""
h=int(input('Nhập giờ: '))
m=int(input('Nhập phút: '))
s=int(input('Nhập giây: '))
print(f'Giờ phút giây đã nhập là: {h}:{m}:{s}')
tongs=h*3600+m*60+s
print('Tổng số giây là: ',tongs)
