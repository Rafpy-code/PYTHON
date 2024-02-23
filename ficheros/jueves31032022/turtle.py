# -*- coding: utf-8 -*-
"""
Created on Fri Apr  1 10:30:56 2022 @author: Ramón
"""
from turtle import *
'''
color("red", "yellow")

begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()

color("blue")
stamp()
fd(150)
'''
for i in range(15):
    '''color("yellow")
    stamp()
    fd(30)'''
    circle(60)
    write("Home = ", True, align="center")
    write((0,0), True)
    
    color("red")
    stamp()
    down(40)