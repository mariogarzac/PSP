#!/usr/bin/python
# 
#  Clase lector que hará todo el procesamiento de los archivos
#   Esto incluye contar las lineas y sus respectivas bases, items, modificaciones y agregados
#   al igual que imprimir los resutlados
#
# Mario Garza Chapa A01720245
#
# Creado: 25/02/2022

import queue
import re

# CLASE LECTOR PARA LEER Y PROCESAR LOS ARCHIVOS EN CASO DE QUE EXISTAN
class Lector:
    # Función para leer el archivo y procesar
    #.i
    def procesarArchivo(self, fileName):
        # variables para contar codigo, comentarios y líneas en blanco
        ldcTotal = 0
        ldcBase = 0
        ldcMod = 0
        ldcDel = 0
        ldcItem = 0
        ldcAdd = 0

        claseName = fileName.split('.')
        claseName = claseName[0].upper()        

        # Ciclo para leer la cantidad de lineas
        with open(fileName, "r") as arch:
            while (line := arch.readline()):                            
                #Busca las lineas de código que puedan ser base, borradas, items o modificadas
                if (re.search(r'\#.[bdim][\n\=\s]', line)):                    
                    if (".b" in line):
                        ldcBase += self.getNumber(line,'b')
                    elif(".d" in line):                    
                        ldcDel += self.getNumber(line,'d')
                    elif(".i" in line):
                        ldcItem += self.getNumber(line,'i')
                    elif(".m" in line):
                        ldcMod += self.getNumber(line,'m')

                if(re.search(r'^[\w\'\+\-\[]+', line.lstrip())):
                    ldcTotal += 1
                    #print(f"{counter},{line.lstrip()}")
                elif (re.search(r'\}\s\w', line.lstrip())):
                    ldcTotal += 1
                    #print(f"{counter},{line.lstrip()}")                
                    
            arch.close()

            ldcAdd = ldcTotal - ldcBase + ldcDel
            data = [claseName, ldcTotal, ldcItem, ldcBase, ldcDel, ldcMod, ldcAdd]  
            
        #regresa el arreglo de cada archivo
        return data

    #Función auxiliar para hacer el código de procesarArchivo más limpio
    #.i
    def getNumber(self, line, char):        
        if(f"#.{char}=" in line):                                                                       
            num = int("".join(filter(str.isdigit, line)))            
            return num
        else:
            return 1    

    #Calcula si es una clase base, nueva o reusada
    #.i
    def calculateClass(self, order):
        base = queue.Queue()
        nueva = queue.Queue()
        reusada = queue.Queue()        

        #Tomará un queue que se manda desde el main e irá acomodando en sus respectivas categorias
        while (not order.empty()): 
            data = order.get()
            if (data[3] > 0 and (data[5] > 0 and data[4] > 0 and data[6] > 0)):                
                base.put(data)
            elif (data[3] == 0 and data[5] == 0 and data[4] == 0 and data[6] > 0):                
                nueva.put(data)
            elif (data[3] > 0 and data[5] == 0 and data[4] == 0 and data[6] == 0):                
                reusada.put(data)
            else:
                print("Hubo un error. ")

        self.prettyPrint(base,nueva,reusada)

    #Función auxiliar para imprimir las clases en sus categorias
    # y también crea y escribe en un archivo .txt
    #.i
    def prettyPrint(self, base, nueva, reusada):
        total = 0
        file = open("/Users/mariogarza/Documents/Programming/Python/PSP/ConteoLDC.txt","w")

        print("CLASES BASE:")       
        file.write("CLASES BASE:\n")
        while(base.qsize() > 0):
            data = base.get()            
            total += data[1]
            print((f"\t{data[0]}: T:{data[1]}, I:{data[2]}, B:{data[3]}, D:{data[4]}, M:{data[5]}, A:{data[6]}"))            
            file.write((f"\t{data[0]}: T:{data[1]}, I:{data[2]}, B:{data[3]}, D:{data[4]}, M:{data[5]}, A:{data[6]}\n"))
        print("--------------------------------------------")        
        file.write("--------------------------------------------\n") 

        print("CLASES NUEVAS:")
        file.write("CLASES NUEVAS:\n")
        while (nueva.qsize() > 0):
            data = nueva.get()
            total += data[1]
            print((f"\t{data[0]}: T:{data[1]}, I:{data[2]}"))
            file.write((f"\t{data[0]}: T:{data[1]}, I:{data[2]}\n"))
        print("--------------------------------------------")
        file.write("--------------------------------------------\n")

        print("CLASES REUSADAS:")
        file.write("CLASES REUSADAS:\n")
        while (reusada.qsize() > 0):
            data = reusada.get()
            total += data[1]
            print((f"\t{data[0]}: T:{data[1]}, I:{data[2]}, B:{data[3]}"))
            file.write((f"\t{data[0]}: T:{data[1]}, I:{data[2]}, B:{data[3]}\n"))
        print("--------------------------------------------")
        file.write("-------------------------------------------- \n")

        print(f"LDC totales: {total}")
        file.write(f"LDC totales: {total}\n")
        file.close()
