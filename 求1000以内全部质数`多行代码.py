#!/usr/bin/python
# -*- coding: cp936 -*-

import math
def prime(x):
	for i in range(2,x):
		if x%i==0:
			return False
		if i==x-1:
			return True


print(2,end=',')
for i in range(3,1001,2):
  if prime(i):
    print(i,end=',')
