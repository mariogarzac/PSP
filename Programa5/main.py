# !/usr/bin/env python3
# Este programa calcula p dada una x y los grados de libertad
# 
#
# Mario Garza Chapa A01720245
#
# Creado: 21/04/2022

#.b=15
#.m=1

from Statistics import Statistics
from Verificador import Verificador

# MAIN DEL PROGRAMA
def main():
    ver = Verificador()
    stats = Statistics()
    
    # Verifica que los datos sean correctos 
    # Si los datos son correctos, se calculará la dist t
    # .m=6
    p = ver.verificaP()
    dof = ver.verificaDof()
    if (p == -1 or dof == -1):
        return 0
    else:
        x = stats.getX(dof,p)

    # Se imprime los x, dof y p
    print("x = {:5f}".format(x)) 
    print("dof = {}".format(dof)) 
    print("p = {:5f}".format(p)) 
            
if __name__ == "__main__":
    main()
