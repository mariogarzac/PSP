#!/usr/bin/python
# Este programa tiene como fín leer archivos y calcular 
# numero de pares, xk, r, r^2, b0, b1 y yk
#
# Mario Garza Chapa A01720245
#
# Creado: 28/03/2022

from Statistics import Statistics
from Verificador import Verificador

#.m=3
# MAIN DEL PROGRAMA
def main():

    ver = Verificador()
    stats = Statistics()
    
    #Se lee el nombre del archivo
    fileName = input("Nombre del archvio a leer: ")

    # Verifica que el archivo esté en el PATH
    # Si está, lo leerá y realizará los calculos
    if(ver.verificaArchivo(fileName)):            
        stats.getElements(fileName)        
    
    input("Presiona ENTER para cerrar.")
    
if __name__ == "__main__":
    main()
