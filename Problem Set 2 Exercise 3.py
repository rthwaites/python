# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 22:01:11 2016

@author: Thwaites
"""

balance = 4773
annualInterestRate = 0.2 
mIR = annualInterestRate / 12
minPay = 10
remain = balance
month = 0
upperlim = remain

for month in range(12):
    interest = mIR * upperlim
    upperlim += interest
    month += 1

upperlim = upperlim / 12

