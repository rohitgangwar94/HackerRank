#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []
    count = 0
    a=0
    l=[]

    for i in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    #print(arr[0:2:2])
    for i in range(4):
        for j in range(4):
            a=arr[j][i]+arr[j][i+1]+arr[j][i+2]+arr[j+1][i+1]+arr[j+2][i]+arr[j+2][i+1]+arr[j+2][i+2]
            l.append(a)
    print(max(l))
