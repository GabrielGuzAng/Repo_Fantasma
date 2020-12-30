# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 18:13:40 2020

@author: PC-RN80
"""

num=int(input("\n ingrese num \n"))

prom=0
cant=0

while(num!=0):
    if(num>=0 and num<=10):
        prom=num+prom
        cant=cant+1
        num=int(input("\n ingrese num \n"))
    else:
        num=int(input(" Ingrese un valor dentro de l rango"))
       
    
prom_final=prom/cant   
print("\n El promedio es %.2f \n"% prom_final)