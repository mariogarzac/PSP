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
    
    def verificaDatos(self):
        try:
            x = int(input("Escribe la x que se utilizará: "))            
            if (x < 0):
                print("x debe de ser mayor a 0")
                return -1, -1
                
            dof = int(input("Escribe los grados de libertad: "))
            if (dof < 0):
                print("dof debe de ser mayor a 0")
                return -1, -1
        except ValueError:
            print("ERROR. Los valores deben de ser números. ")
            return -1, -1

        return x,dof
