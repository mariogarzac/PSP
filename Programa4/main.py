#!/usr/bin/env python
# Este programa tiene como fín leer archivos y calcular 
# numero de pares, xk, r, r^2, b0, b1 y yk
#
# Mario Garza Chapa A01720245
#
# Creado: 28/03/2022

from os import stat
from Statistics import Statistics
from Verificador import Verificador

#.b=10
#.d=3
#.m=4

# MAIN DEL PROGRAMA
def main():

    ver = Verificador()
    stats = Statistics()
    

    # Verifica que los datos sean correctos 
    # Si los datos son correctos, se calculará la dist t

    x,dof = ver.verificaDatos()
    if (x == -1):
        return 0
    else:
        print(stats.getConstant(dof))

            

if __name__ == "__main__":
    main()
