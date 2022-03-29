#!/usr/bin/python
# Este programa tiene como fín leer archivos y calcular 
# numero de pares, xk, r, r^2, b0, b1 y yk
#
# Mario Garza Chapa A01720245
#
# Creado: 23/02/2022


from Calculador import Calculador
from Verificador import Verificador

#.d=8
#.m=6
# MAIN DEL PROGRAMA
def main():

    ver = Verificador()
    calc = Calculador()
    
    #Se lee el nombre del archivo
    fileName = input("Nombre del archvio a leer: ")

    # Verifica que el archivo esté en el PATH
    # Si está, lo leerá y realizará los calculos
    if(ver.verifica(fileName)):            
        calc.getElements(fileName)        
            

if __name__ == "__main__":
    main()
