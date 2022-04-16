# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 23:03:08 2022

@author: 105518125劉育秀

作業四:求1~100間的質數    
"""

for i in range(2,101):     
    isR = True
    for x in range(2,i):
        if i % x == 0:
            isR = False
            
    #if isR == True:
    if isR:
            print(i,"是質數")


        
    
    
    