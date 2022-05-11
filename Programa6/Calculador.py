#!/usr/bin/python
# 
# Clase lector que hará todo el procesamiento de los archivos
# Esto incluye contar las lineas y sus respectivas bases, items, modificaciones y agregados
# al igual que imprimir los resutlados
#
# Mario Garza Chapa A01720245
#
# Creado: 28/03/2022


import math
import statistics
from Statistics import Statistics
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
            try:          
                for line in arch:
                    line = (line.strip()).split(',')                
                    x.append(float(line[0]))
                    y.append(float(line[1]))
                
            except ValueError:
                print("ERROR. El archivo es incompatible con este programa. ")
                return 0            
            except IndexError:
                print("ERROR. Hay un valor sin par. ")
                return 0
            finally:
                arch.close()                

            values = self.__getValues(x,y, int(xk))
            self.__prettyPrint(values)
                                
        arch.close()

    # Función para calcular los elementos 
    #.i
    def __getValues(self, x, y, xk):
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
        r = self.__getR(n, sumX, sumY, xSquared, ySquared, sumXY)
        rSquared = pow(r,2)
        b1 = self.__getB1(n, xAvg, yAvg, sumXY, xSquared)
        b0 = self.__getB0(yAvg, b1, xAvg)
        yk = self.__getYk(b0, b1, xk)
        sig = self.__getSig(r, n, rSquared)
        ran = self.__getRange(n, xk, xAvg, x, y, b0, b1)
        UPI = yk + ran
        LPI = 0 if (yk - ran < 0) else yk - ran

        
        values = [n, xk, r, rSquared, b0, b1, yk, sig, ran,  UPI, LPI]
        return values   

    #.i
    def __getRange(self,n, xk, xAvg, xArr, yArr, b0, b1): 
        stats = Statistics()       
        x = stats.getX(n - 2, 0.35)
        sum = stdDev = bottom = 0

        # Get Standard Deviation
        for i in range(0, n):          
            sum += pow(yArr[i] - b0 - (b1 * xArr[i]), 2)

        sum *= (1 / (n - 2))
        stdDev = math.sqrt(sum)
       
        # Get square root part
        top = pow(xk - xAvg, 2)

        for i in range (0, n):
            bottom += pow(xArr[i] - xAvg , 2)

        division = math.sqrt(1 + (1 / n) + (top/bottom))
        
        return (x * stdDev * division)


    # Calucla la significacia
    #.i
    def __getSig(self, r, n, rSquared):
        stats = Statistics()
        top = abs(r) * math.sqrt(n - 2)    
        bottom = math.sqrt(1 - rSquared)
        x = top/bottom        
        p = stats.distT(n - 2,x)         
        return 1 - (2 * p)

    # Calcula r
    #.i
    def __getR(self, n, sumX, sumY, xSquared, ySquared, sumXY):
        top = (n * sumXY) - (sumX * sumY)
        bottom = math.sqrt(((n * xSquared) - (pow(sumX,2))) * ((n * ySquared) - (pow(sumY,2))) )
        return top/bottom

    # Calcula b0
    #.i
    def __getB0(self,yAvg, b1, xAvg):
        return (yAvg - (b1 * xAvg))

    # Calcula b1
    #.i
    def __getB1(self, n, xAvg, yAvg, sumXY, xSquared):
        top = sumXY - (n * xAvg * yAvg)
        bottom = xSquared - (n * pow(xAvg,2))
        return top/bottom 

    # Calcula yk
    #.i
    def __getYk(self, b0, b1, xk):        
        return b0 + (b1 * xk)

    # Imprime los elementos calculados 
    #.i      
    def __prettyPrint(self, values):
        # orden en el arreglo values
        # [n, xk, r, rSquared, b0, b1, yk, sig, ran,  UPI, LPI]
        print("N = {}".format(values[0]))
        print("xk = {:.5f}".format(values[1]))
        print("r = {:.5f}".format(values[2]))
        print("rSquared = {:.5f}".format(values[3]))
        print("b0 = {:.5f}".format(values[4]))
        print("b1 = {:.5f}".format(values[5]))
        print("yk = {:.5f}".format(values[6]))
        print("sig = {:.10f}".format(values[7]))
        print("range = {:.5f}".format(values[8]))
        print("UPI = {:.5f}".format(values[9]))
        print("LPI = {:.5f}".format(values[10]))