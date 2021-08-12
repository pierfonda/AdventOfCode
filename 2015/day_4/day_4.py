#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 15 14:59:12 2021

@author: pier
"""

import hashlib 

inputStr='iwrupvqb'

i=0

while True:
    i+=1
    var=hashlib.md5((inputStr+str(i)).encode('utf-8')).hexdigest()
    if var[:6]=='000000' :
        print("at",i,"the md5 hash is",var)
        break

