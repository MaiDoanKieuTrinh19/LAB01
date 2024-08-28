# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:02:33 2024

@author:MaiDoanKieuTrinh_23732851
"""
ngay=int(input('Nhập ngày sinh của bạn: '))
thang=int(input('Nhập tháng sinh của bạn: '))
nam=int(input('Nhập năm sinh của bạn: '))
#câua
print(f'Ngày tháng năm sinh của bạn là: {ngay}/{thang}/{nam}')
#câub
sonam= nam%100
print(f'Ngày tháng năm sinh của bạn là: {ngay}/{thang}/{sonam:02d}')
#câuc
print(f'Năm tháng ngày sinh của bạn là: {nam}/{thang}/{ngay}')
