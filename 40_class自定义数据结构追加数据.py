#!/usr/bin/python
# -*- coding: cp936 -*-
import turtle
from turtle import *


class Dog:

    tricks = []             # mistaken use of a class variable

    def __init__(self, name):
        self.name = name

    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')
e = Dog('Buddy')
d.add_trick('roll over')
e.add_trick('play dead')
print(d.name,'\n',d.tricks)              # unexpectedly shared by all dogs
#output: ['roll over', 'play dead']

 



