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
    comienza = 2 #El juego nos lo indica
    for torre_1, torre_2 in zip(r1,r2): #usamos el zip para mapear los índices en más de una variable
        distancia = abs(torre_2 - torre_1) #El juego se reduce a las distancias, es decir dependiendo de la distancia habrá un ganador u otro. Asimismo es muy importante recalcar que también depende de que empiece.
        ganador = ""
        if comienza == 2:
            if distancia == 1:
                ganador = 'Jugagor 1'
                comienza = 2
            else:
                ganador = 'Judador 2'
                comienza = 1
        else:
            if distancia == 1:
                ganador = 'Jugador 2'
                comienza = 1
            else:
                ganador = 'Jugador 1'
                comienza = 2

    if ganador == 1:
        return('ha ganado el jugador 1!')
    else:
        return ('ha ganado el jugador 2!')


if __name__ == '__main__':
    
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
        print.write(result + '\n')


while True:
    print(':MENÚ:.')
    print('En primer lugar debera introducir el número de tableros, es decir el numero de partidas que desea jugar')
    print('En segundo lugar indica la dimensión del tablero, recuerde que ')
    print('En tercer lugar indique las posición de la primera torre')
    print('Por último indique las posiciones de la segunda torre')
