# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 13:48:31 2018

@author: haithama
"""
Fflg=0; Cflg=0;
x = int(input("input temerature mode 1 for C to F and 2 for F to C "))
T = int(input("input temerature "))
if x==1:
    Fflg=1;
    F = ((T + 40)* 9/5) - 40
    print("temperature in F is ",F)
elif x==2:
    Cflg=1;
    C = ((T + 40)* 5/9) - 40
    print("temperature in C is ",C)
    
else:print("wrong temperature mode selection, please re enter your choice")


if ((F<=32 and Fflg==1) or (C<=0 and Cflg==1)):
    print("very cold")
elif ((32<F<=50 and Fflg==1) or (0<C<=20 and Cflg==1)):
    print("cold")
elif ((50<F<=75 and Fflg==1) or (20<C<=38 and Cflg==1)):
    print("worm")
elif ((75<F and Fflg==1) or (38<C and Cflg==1)):
    print("hot")
    
    
    
      
    