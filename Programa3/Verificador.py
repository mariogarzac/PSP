#!/usr/bin/python
# Tiene como fin verificar que exista el archivo y/o que no esté vacío 
#
# Mario Garza Chapa A01720245
#
# Creado: 28/03/2022

import os

#.b=15
class Verificador:
    # Verifica si el archivo existe o si el archivo está vacío
    # En caso de que no esté vacío, regresará True para que se ejecute
    # El lector
    #.i
    def verifica(self, fileName):
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
