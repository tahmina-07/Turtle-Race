# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 03:18:37 2022

@author: USER
"""

from turtle import Turtle
from random import randint
Amina = Turtle()
Amina.color('purple')
Amina.shape('turtle')
Amina.penup()
Amina.goto(-160, 100)
Amina.pendown()

Rick = Turtle()
Rick.color('red')
Rick.shape('turtle')
Rick.penup()
Rick.goto(-160, 70)
Rick.pendown()

Faryal = Turtle()
Faryal.color('blue')
Faryal.shape('turtle')
Faryal.penup()
Faryal.goto(-160, 40)
Faryal.pendown()

Ferdaws = Turtle()
Ferdaws.color('yellow')
Ferdaws.shape('turtle')
Ferdaws.penup()
Ferdaws.goto(-160, 10)
Ferdaws.pendown()

for movement in range(100):
    Amina.forward(randint(1, 6))
    Rick.forward(randint(1, 6))
    Faryal.forward(randint(1, 6))
    Ferdaws.forward(randint(1, 6))

input("press Enter to close")





