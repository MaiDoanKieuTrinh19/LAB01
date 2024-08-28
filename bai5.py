# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:39:08 2024

@author: MaiDoanKieuTrinh_23732851
"""

A=input('Nhập giờ phút giây theo định dạng hh:mm:ss : ')
hh, mm, ss= map(int,A.split(':'))
if 0<=hh<24 and 0<=mm<60 and 0<=ss<60:
    tong_so_giay= hh*3600+mm*60+ss
    print(f'Tổng số giây của {A} là: {tong_so_giay} ')
else:
    print('Bạn đã nhập sai giờ phút giây')