# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 12:20:01 2022 @author: Ramón
Generar secuencias de números con random y numpy
"""

import random
import numpy as np

print('Generación de números con random.seed(semilla)')
#fijamos la semilla.
random.seed(0)

#generamos los números aleatorios.
x = [random.uniform(-100, 100) for i in range(10)]
print(x)
y = [random.uniform(-100, 100) for i in range(10)]
print(y)



print('Generación de números con np.random.seed(semilla)')

#fijamos la semilla.
np.random.seed(0)

#generamos los números aleatorios.
x = [np.random.uniform(-100, 100) for i in range(10)]
y = [np.random.uniform(-100, 100) for i in range(10)]
print(x,y)