#!/bin/python

import math
import os
import random
import re
import sys

lst=[]
lst1=[]
lst2=[]
def binary(n):
    if n>1:
        if n%2==0:
            n=n//2            
            lst.append(0)
            binary(n)            
        else:
            n=n//2
            lst.append(1)
            binary(n)            
    else:
        lst.append(1)
    return lst[::-1]

if __name__ == '__main__':
    n = int(raw_input())
    lst1 = binary(n)
    count = 0
    for x in range(len(lst1)):
        if lst1[x] == 1:
            count=count+1
        else:
            lst2.append(count)             
            count=0
    lst2.append(count)
    print(max(lst2))
