# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

hh=int(input('Nhập giờ: '))
mm=int(input('Nhập phút: '))
ss=int(input('Nhập giây: '))
if 0<=hh<24 and 0<=mm<60 and 0<=ss<60:
    print(f'{hh}:{mm}:{ss}')
else:
    print('Bạn đã nhập sai giờ phút giây')
