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
            
            #print('0',n)
            lst.append(0)
            binary(n)
            
        else:
            n=n//2
            #if n>=2:
            #print('1',n)
            lst.append(1)
            binary(n)
            
    else:
        lst.append(1)
    return lst[::-1]

if __name__ == '__main__':
    n = int(raw_input())
    lst1 = binary(n)
    
#print(lst1)
#print(len(lst1))
    count = 0
    for x in range(len(lst1)):
        if x>-1:
            if lst1[x] == 1:
                #print(x)
                count=count+1
                #print(count)
            else:
                #print('-',x)
                lst2.append(count)
                #print('-',count)
                #print('-',lst2)
                count=0
    lst2.append(count)
    print(max(lst2))




