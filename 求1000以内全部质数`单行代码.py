#!/usr/bin/python
# -*- coding: cp936 -*-

from math import sqrt
 
print(" ".join("%s"% x for x in range(2,1000)if not[y for y in range(2,int(sqrt(x)))if not x%y]))
