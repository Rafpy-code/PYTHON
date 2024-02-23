# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 12:56:51 2022

@author: user
"""
import numpy as np
import matplotlib.plylot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

#funcion de la exuacion 
def function_prueba(x):
    res = np.sqrt(x[0]**2 + x[i]**2)
    return res

#Genero los vectores 
x = np.linspace(-100, 100, 1000)
y = np.linspace(-100, 100, 1000)

#Evaluamos todos los valores de las variables
x_ax, y_ax = np.meshgrid(x,y)
vals = np.c_[x_ax.ravel(), y_ax.ravel()]
fx = np.reshape([function_prueba(val) for val in vals], (1000, 1000))

#Representamos los resultados obtenidos
figure_3d = plt-figure(figsize=(8,6))

