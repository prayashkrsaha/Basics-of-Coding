#learniin of 2 D arary
#Source - https://www.hackerrank.com/challenges/30-2d-arrays/problem

#!/bin/python3

import math
import os
import random
import re
import sys


def _get_hourglass_sum(matrix,r,c):
    sum=0
    sum+=matrix[r-1][c-1]
    sum+=matrix[r-1][c]
    sum+=matrix[r-1][c+1]
    sum+=matrix[r][c]
    sum+=matrix[r+1][c+1]
    sum+=matrix[r+1][c]
    sum+=matrix[r+1][c-1]
    return sum


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

max_hourglass_sum=-63
for i in range(1,5):
    for j in range (1,5):
        cur_hourglass_sum=_get_hourglass_sum(arr,i,j)
        if cur_hourglass_sum>max_hourglass_sum:
            max_hourglass_sum=cur_hourglass_sum

print(max_hourglass_sum)
