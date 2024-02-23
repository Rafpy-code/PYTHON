# -*- coding: utf-8 -*-
"""
Created on Thu Apr  7 13:01:35 2022 @author: Ramón
"""

import string

# initialize string
text = 'Python !! is the be1st $ programming language @ hoy'

#sum(), strip(), split() methods, le sumo uno por que cuenta desde el 0
result = sum([i.strip(string.punctuation).isalpha() for i in text.split()])+1
print(text)
print(text.split())
print("There are " + str(result) + " palabras.")