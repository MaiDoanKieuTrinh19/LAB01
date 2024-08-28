# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 19:37:59 2024

@author: Student
"""

can_nang=float(input('Nhập số cân nặng của (kg): '))
chieu_cao=float(input('Nhập số chièu cao của bạn (m): ')) 
BMI=can_nang/(chieu_cao**2)
print('Số đo kiểm tra sức khỏe BMI của bạn là: ',round(BMI, 3))
