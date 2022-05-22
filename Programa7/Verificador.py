#!/usr/bin/env python3
# Verifica que exista el archivo y que no sea vacio.
#
# Mario Garza Chapa A01720245
#
# Creado: 22/05/2022

#.b=50
#.d=35

import os

class Verificador:
       #.i
    def verificaArchivo(self, fileName):
        # if para revisar que exista y no esté vacío
        try:
            fp = open(fileName, "r") 
            
        #Si no existe el archivo      
        except FileNotFoundError:
            print("No existe el archivo en el PATH actual, revisa el nombre.")
            print("Path actual: {}".format(os.getcwd()))
            return False 

        #Si el archivo está vacio 
        if(os.path.getsize(fileName) == 0):
            print("Archivo vacio. ")
            fp.close()
            return False  
        
        fp.close()
        return True 
