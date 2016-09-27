# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 20:55:57 2016

@author: Thwaites
"""

balance = 4773
annualInterestRate = 0.2 
mIR = annualInterestRate / 12
minPay = 10
remain = balance

while remain >= 0:
    minPay += 10
    remain = balance
    month = 1    
    
    while month <= 12 and remain >= 0:
        remain -= minPay
        interest = mIR * remain
        remain += interest
        month += 1
    
    print(minPay)

