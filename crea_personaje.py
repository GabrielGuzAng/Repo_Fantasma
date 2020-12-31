# -*- coding: utf-8 -*-
"""
Created on Wed Dec 30 19:12:28 2020

@author: PC-RN80
"""

import random 

n=4
personaje={"Fuerza":0,"Velocidad":0,"Astucia":0}

for key, value in personaje.items():
    dados=[random.randint(1, 6) for i in range(n)]
    dados.sort()
    a_sumar=dados[1:]
    res=sum(a_sumar)
    personaje[key]=res

# dados=[random.randint(1, 6) for i in range(n)]
# dados.sort()
# a_sumar=dados[1:]
# res=sum(a_sumar)

# print("\n", dados,"\n")
# print("\n res=",res," \n")

for key, value in personaje.items():
    print(key)
    print(value)