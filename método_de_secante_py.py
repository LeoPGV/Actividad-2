# -*- coding: utf-8 -*-
"""Método de Secante.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1L_A8SqCXKBgjeVmY9Nlh2NZS3WnxP_Cy
"""

from math import *
import numpy as np
import matplotlib.pyplot as plt

def funcion1(x):
    return cos(x)-x

#Ingrese el valor inicial 
p0 = 0.5
p1 = pi/4
error = 100
tol = 0.0000001
niter = 0
nmax = 100

print("n \t\t Pn \t\t error")
print("{0} \t\t {1:6.6f} \t {2:6.6f}".format(niter, p0, 0 ))

q0 = funcion1(p0)
q1 = funcion1(p1)

while error > tol and niter < nmax:
    p = p1-(q1*(p1-p0))/(q1-q0)
    error = abs(funcion1(p)-funcion1(p1))
    p0 = p1
    q0 = q1
    p1 = p
    q1 = funcion1(p)
    niter +=1
    print("{0} \t\t {1:6.8f} \t {2:6.8f}".format(niter, p, error ))

print("La raiz apriximada es {0:6.8f}".format(p))