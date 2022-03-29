#!/usr/bin/python
# 
#  Clase lector que hará todo el procesamiento de los archivos
#   Esto incluye contar las lineas y sus respectivas bases, items, modificaciones y agregados
#   al igual que imprimir los resutlados
#
# Mario Garza Chapa A01720245
#
# Creado: 25/02/2022

#.d=78
#.m=1
# CLASE LECTOR PARA LEER Y PROCESAR LOS ARCHIVOS EN CASO DE QUE EXISTAN

import math
class Calculador:
    # Función para recibir los elementos calculados
    #.i
    def getElements(self, fileName):
        # variables para contar codigo, comentarios y líneas en blanco
        # Ciclo para leer la cantidad de lineas
        x = [] 
        y = []

        with open(fileName, "r") as arch:
            xk = arch.readline()
            for line in arch:
                line = (line.strip()).split(',')                
                x.append(float(line[0]))
                y.append(float(line[1]))
            
            if (len(x) != len(y)):
                print("Hay elementos que no tienen par. ")
                arch.close()
                return 0                 

            values = self.getValues(x,y, int(xk))
            self.prettyPrint(values)
                                
        arch.close()

    # Función para calcular los elementos 
    #.i
    def getValues(self, x, y, xk):
        sumX = sumY = sumXY = xSquared = ySquared = 0

        for i in range(0,len(x)):
            xSquared += pow(x[i],2)
            ySquared += pow(y[i],2)
            sumXY += x[i]*y[i]
            sumX += x[i]
            sumY += y[i]  

        n = len(x)
        xAvg = sumX/n
        yAvg = sumY/n
        r = self.getR(n, sumX, sumY, xSquared, ySquared, sumXY)
        rSquared = round(pow(r,2),5)
        b1 = self.getB1(n, xAvg, yAvg, sumXY, xSquared)
        b0 = self.getB0(yAvg, b1, xAvg)
        yk = self.getYk(b0, b1, xk)

        values = [n, r, rSquared, b0, b1, yk, str(xk)]
        return values          

    # Calcula r     
    #.i
    def getR(self, n, sumX, sumY, xSquared, ySquared, sumXY):
        top = (n * sumXY) - (sumX * sumY)
        bottom = math.sqrt(((n * xSquared) - (pow(sumX,2))) * ((n * ySquared) - (pow(sumY,2))) )
        return round(top/bottom,5)

    # Calcula b0
    #.i
    def getB0(self,yAvg, b1, xAvg):
        return round((yAvg - (b1 * xAvg)),5)

    # Calcula b1
    #.i
    def getB1(self, n, xAvg, yAvg, sumXY, xSquared):
        top = sumXY - (n * xAvg * yAvg)
        bottom = xSquared - (n * pow(xAvg,2))
        return round((top/bottom),5)

    # Calcula yk
    #.i
    def getYk(self, b0, b1, xk):        
        return round((b0 + (b1 * xk)),5)

    # Imprime los elementos calculados 
    #.i      
    def prettyPrint(self, values):
        #[n, r, rSquared, b0, b1, yk, xk]
        print("N = {}".format(values[0]))
        print("xk = {}".format(values[6].strip()))
        print("r = {}".format(values[1]))
        print("rSquared = {}".format(values[2]))
        print("b0 = {}".format(values[3]))
        print("b1 = {}".format(values[4]))
        print("yk = {}".format(values[5]))


