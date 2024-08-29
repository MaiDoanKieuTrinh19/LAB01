# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 15:13:21 2024

@author: Hi
"""

can_nang=float(input('Nhập số cân nặng của (kg): '))
chieu_cao=float(input('Nhập số chièu cao của bạn (m): ')) 
BMI=can_nang/(chieu_cao**2)
print('Chỉ số BMI của bạn là: ',round(BMI, 2))
if BMI<16:
    print('Gầy độ III')
elif 16<=BMI<17:
    print('Gầy độ II')
elif 17<=BMI<18.5:
    print('Gầy độ I')
elif 18.5<=BMI<25:
    print('Bình thường')
elif 25<=BMI<30:
    print('Thừa cân')
elif 30<=BMI<35:
    print('Béo phì độ I')
elif 35<=BMI<40:
    print('Béo phì độ II')
elif BMI>=40:
    print('Béo phì độ III')
else:
    print('Không xác định ')
    
    


