#!/usr/bin/python
# Este programa tiene como fín leer archivos y contar cuantas lineas
# de código tiene y contar cuantas son de base, item, modificadas o agregadas
# 
#
# Mario Garza Chapa A01720245
#
# Creado: 23/02/2022


import queue
import os
from Lector import Lector
from Verificador import Verificador


# MAIN DEL PROGRAMA
def main():

    answer = "y"
    ver = Verificador()
    lec = Lector()
    #Queue para ir almacenado los valores de cada archivo
    order = queue.Queue() 
    verify = False  
    
    while(answer == "y"):

        fileName = input("Nombre del archivo para leer: ")
        # Verifica que el archivo esté en el mismo directorio
        # Si está, lo leerá y contará las líneas
        if(ver.verifica(fileName)):
            verify = True
            order.put(lec.procesarArchivo(fileName))
                
        answer = input("Seguir leyendo archivos? (y/n): ")                
        while(not (answer == "y" or answer == "n")):
         answer = input("Seguir leyendo archivos? (y/n): ") 
    
    #Ordenará e imprimirá los valores
    if (verify):
        lec.calculateClass(order)
    cerrar = input("Presiona ENTER para cerrar: ")


if __name__ == "__main__":
    main()
