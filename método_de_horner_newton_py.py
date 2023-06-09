# -*- coding: utf-8 -*-
"""Método de Horner-Newton.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L_A8SqCXKBgjeVmY9Nlh2NZS3WnxP_Cy
"""

import numpy as np
import matplotlib.pyplot as plt
import numpy.polynomial.polynomial as pol

#Metodo de Newton-Horner 

tol=0.000001
i=0
nmax=20
error=100
#coeficientes de x^4 + 2x^3 + x^2-x-6
a=-6
b=-1
c=1
d=2
e=1
#Se define la funcion p(x)
p = np.array([a,b,c, d,  e ])
pi=1.5

#Ciclo iterativo 
while error > tol and i <= nmax:
   #Se aplica el método de horner 
  q4=e
  q3=d+ q4*(pi)
  q2=c + q3*(pi)
  q1=b+ q2*pi

  #Se determina el Q(x)
  q=np.array([q1,q2, q3,  q4 ])
  

  #Se calcula el valor de cada pn
  pn = pi - (pol.polyval(pi, p))/(pol.polyval(pi, q))

  error = abs(pn - pi)

  pi=pn
  i += 1
  print("{0} \t\t {1:6.6f} \t {2:6.6f}".format(i, pn,error ))

print(f"La raiz aproximada es {pn}")