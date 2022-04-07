#!/usr/bin/env python3
# Este programa calcula p dada una x y los grados de libertad
# 
#
# Mario Garza Chapa A01720245
#
# Creado: 6/04/2022

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
        p = stats.distT(dof,x)
    
    # Se imprime los valores que se utilizaron y p
    print("x = {:5f}".format(x)) 
    print(f"dof = {dof}") 
    print("p = {:5f}".format(p)) 
            
if __name__ == "__main__":
    main()
