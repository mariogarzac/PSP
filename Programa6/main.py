# !/usr/bin/env python3
# Este programa calcula p dada una x y los grados de libertad
# 
#
# Mario Garza Chapa A01720245
#
# Creado: 21/04/2022

#.b=15
#.m=7
#.d=4

from Statistics import Statistics
from Verificador import Verificador

# MAIN DEL PROGRAMA
def main():
    ver = Verificador()
    stats = Statistics()
    
    # Verifica que los datos sean correctos 
    # Si los datos son correctos, se calculará la dist t
    p = ver.verificaP()
    if (p == -1):
        return 0
    else:
        dof = ver.verificaDof()
    
    if (dof <= 0):
        return 0
    else:
        x = round(stats.getX(dof,p),5)

         # Se imprime los x, dof y p
        print("p = {:5f}".format(p)) 
        print("dof = {}".format(dof))
        print("x = {:5f}".format(x)) 
     
    
            
if __name__ == "__main__":
    main()
