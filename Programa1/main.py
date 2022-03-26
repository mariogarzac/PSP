#!/usr/bin/python
# Este programa tiene como fín leer archivos y regresar la cantidad
# de líneas con código, líneas en blanco y líneas con comentarios que
# contiene el archivo que se leyó.
#
# Mario Garza Chapa A01720245
#
# Creado: 23/02/2022


import os
from Lector import Lector
from Verificador import Verificador

# MAIN DEL PROGRAMA

#.i
def main():
    print("Path actual: {}".format(os.getcwd()))
    fileName = input("Nombre del archivo para leer: ")
    ver = Verificador()
    lec = Lector()

    
    # Verifica que el archivo esté en el mismo directorio
    # Si está, lo leerá y contará las líneas
    if(ver.verifica(fileName)):
        lec.procesarArchivo(fileName)



if __name__ == "__main__":
    main()
