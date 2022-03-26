

import os

class Verificador:
    # Verifica si el archivo existe o si el archivo está vacío
    # En caso de que no esté vacío, regresará True para que se ejecute
    # El lector
    
    #.i
    def verifica(self, fileName):
        # if para revisar que exista y no esté vacío
        try:
            # Abre el archivo y revisa que su tamaño no sea 0 bytes
            fp = open(fileName, "r")
            if (os.path.getsize(fileName) == 0):
                print("El archivo está vacío")
                fp.close()
                return False
            return True
        except:
            print("No existe el archivo en el PATH actual, revisa el nombre.")
            print("Path actual: {}".format(os.getcwd()))
            return False
