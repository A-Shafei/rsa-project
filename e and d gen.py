# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 00:39:14 2020

@author: mhmdb
"""





def egcd(a, b):
    s,t, s_i,t_i = 1,0, 0,1 
    while b != 0 :
        q = a//b
        r = a % b
        x = s - s_i*q 
        y = t - t_i*q
        a, b = b, r
        s, t = s_i, t_i
        s_i, t_i = x, y
        
    return a, s, t    


def seed(initial):
    global x_i
    x_i = initial

def lcg():
    a = 7**5
    c = 0
    m = 2**31-1
    global x_i
    x_i = (a*x_i + c) % m
    return x_i

seed(68854*30)

rndm_list=[]
for i in range(50000):
    rndm_list.append(int(lcg()))

for i in reversed(rndm_list):
    if egcd(i, k)[0]  == 1:
        e = i 
        d = egcd(i, k)[1]
        d = d% k + d 
        break 
print(e)
print(d)  
print((d*e)%k)         
      
        
        
        