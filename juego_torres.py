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
    for torre_1, torre_2 in zip(r1,r2): #usamos el zip para mapear los índices en más de una variable
        distancia = abs(torre_2 - torre_1) #El juego se reduce a las distancias, es decir dependiendo de la distancia habrá un ganador u otro. Asimismo es muy importante recalcar que también depende de que empiece.
        ganador = ""
        if distancia == 1: # La distancia mínima es 0 puesto que en las reglas se establece que r1 != r2
            ganador = "Jugador 1"
        




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