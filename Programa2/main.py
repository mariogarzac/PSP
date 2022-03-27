#!/usr/bin/python
# Este programa tiene como fín leer archivos y contar cuantas lineas
# de código tiene y contar cuantas son de base, item, modificadas o agregadas
# 
#
# Mario Garza Chapa A01720245
#
# Creado: 23/02/2022


import queue
from Lector import Lector
from Verificador import Verificador


# MAIN DEL PROGRAMA
def main():

    ver = Verificador()
    lec = Lector()
    #Queue para ir almacenado los valores de cada archivo
    order = queue.Queue() 
    
    print("-------------------------------------------")
    print("-Para terminar la ejecución escribir exit -")
    print("-------------------------------------------")
    fileName = input("Nombre del archivo para leer: ")
    while(fileName != "exit"):

        # Verifica que el archivo esté en el mismo directorio
        # Si está, lo leerá y contará las líneas
        if(fileName != "" and ver.verifica(fileName)):            
            order.put(lec.procesarArchivo(fileName))
        fileName = input("Nombre del archivo para leer: ")
                
    #Ordenará e imprimirá los valores
    if (fileName == "exit"):
        lec.calculateClass(order)
    input("Presiona ENTER para cerrar: ")


if __name__ == "__main__":
    main()
