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
        rSquared = pow(r,2)
        b1 = self.getB1(n, xAvg, yAvg, sumXY, xSquared)
        b0 = self.getB0(yAvg, b1, xAvg)
        yk = self.getYk(b0, b1, xk)

        values = [n, r, rSquared, b0, b1, yk, xk]
        return values          

    # Calcula r     
    #.i
    def getR(self, n, sumX, sumY, xSquared, ySquared, sumXY):
        top = (n * sumXY) - (sumX * sumY)
        bottom = math.sqrt(((n * xSquared) - (pow(sumX,2))) * ((n * ySquared) - (pow(sumY,2))) )
        return top/bottom

    # Calcula b0
    #.i
    def getB0(self,yAvg, b1, xAvg):
        return (yAvg - (b1 * xAvg))

    # Calcula b1
    #.i
    def getB1(self, n, xAvg, yAvg, sumXY, xSquared):
        top = sumXY - (n * xAvg * yAvg)
        bottom = xSquared - (n * pow(xAvg,2))
        return top/bottom 

    # Calcula yk
    #.i
    def getYk(self, b0, b1, xk):        
        return b0 + (b1 * xk)

    # Imprime los elementos calculados 
    #.i      
    def prettyPrint(self, values):
        #orden en el arreglo values
        #[n, r, rSquared, b0, b1, yk, xk]
        print(f"N = {values[0]}")
        print(f"xk = {values[6]}")
        print(f"r = {values[1]}")
        print(f"rSquared = {values[2]}")
        print(f"b0 = {values[3]}")
        print(f"b1 = {values[4]}")
        print(f"yk = {values[5]}")


