# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 23:10:55 2020

@author: PC-RN80
"""

def suma(a,b):
    return a+b
def resta(a,b):
    return a-b

op={
    "suma":suma,
    "resta":resta,    
}

#print(op["suma"](2,3))

a=int(input("ingrese un numero a \n\n"))
b=int(input("ingrese un numero b \n\n"))

c=input(" escriba que operación desea realizar \n\n")

if c in op:
  print(op[c](2,3))
else:
    print(" dicha operacion no existe \n\n")
