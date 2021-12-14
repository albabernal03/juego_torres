import math
import os
import random
import re
import sys
#
# Complete the 'verticalRooks' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
# 1. INTEGER_ARRAY r1
# 2. INTEGER_ARRAY r2
#
def verticalRooks(r1, r2):
 # Write your code here

 if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    t = int(input().strip())
    for t_itr in range(t):
        n = int(input().strip())
        r1 = []
        for _ in range(n):
            posicion_torre_1 = int(input().strip())
            r1.append(posicion_torre_1)
        r2 = []
        for _ in range(n):
            posicion_torre_2 = int(input().strip())
            r2.append(posicion_torre_2)
        result = verticalRooks(r1, r2)
        fptr.write(result + '\n')

 fptr.close()