#!/usr/bin/python
# Este programa tiene como fín leer archivos y regresar la cantidad
# de líneas con código, líneas en blanco y líneas con comentarios que
# contiene el archivo que se leyó.
# Este es un archivo que contiene las clases
#
# Mario Garza Chapa A01720245
#
# Creado: 25/02/2022

import re

# CLASE LECTOR PARA LEER Y PROCESAR LOS ARCHIVOS EN CASO DE QUE EXISTAN

class Lector:
    # Función para leer el archivo y procesar
    #.i
    def procesarArchivo(self, fileName):
        # variables para contar codigo, comentarios y líneas en blanco
        lineasConCodigo = 0
        lineasConComentario = 0
        lineasEnBlanco = 0
        lineasTotales = 0
        line = " "

        # Ciclo para leer la cantidad de lineas
        with open(fileName, "r") as arch:
            while (line := arch.readline()):                
                lineasTotales += 1
                if ('//' in line or '/*' in line or '* ' in line or '*/' in line):
                    lineasConComentario += 1
                elif ('#' in line):
                    lineasConComentario += 1
                elif (not re.search(r'[\S+/]', line)):
                    lineasEnBlanco += 1
                else:
                    lineasConCodigo += 1

            print("Nombre del archivo: {}".format(fileName))
            print("--------------------------------------------")
            print("Cantidad de líneas en blanco:{} ".format(lineasEnBlanco))
            print("Cantidad de líneas en código:{} ".format(
                lineasConCodigo))
            print("Cantidad de líneas con comentarios:{} ".format(
                lineasConComentario))
            print("Cantidad de lineas en el programa:{} ".format(
                 lineasTotales))
            print("--------------------------------------------")
        arch.close()

# CLASE PARA VERIFICAR SI EL ARCHIVO EXISTE O SI ESTA VACÍO

