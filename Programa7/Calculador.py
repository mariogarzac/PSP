#!/usr/bin/python
# 
# Clase Calculador que hará todo el procesamiento de los archivos
# imprime los valores n, xk, r, rSquared, b0, b1, yk, sig, ran,  UPI, LPI
# 
# Mario Garza Chapa A01720245
#
# Creado: 10/05/2022

#.b=61
#.d=56

import numpy as np

class Calculador:    
    # Función para recibir los elementos y hacer las llamadas utilizadas para la regresión
    #.i
    def regression(self, fileName):
        # Se inicializan los arreglos 
        x = [] 
        y = []
        w = []
        z = []

        # Se lee el archivo y se almacenan los valores de wk, xk, yk y zk
        #.m=6
        with open(fileName, "r") as arch:
            line = arch.readline()
            line = (line.strip()).split(',')
            wk = float(line[0])
            xk = float(line[1])
            yk = float(line[2])


            # Se llenan los arreglos w, x, y, z
            try:          
                for line in arch:
                    line = (line.strip()).split(',')                
                    w.append(float(line[0]))
                    x.append(float(line[1]))
                    y.append(float(line[2]))
                    z.append(float(line[3]))                    
                
            except ValueError:
                print("ERROR. El archivo es incompatible con este programa. ")
                return 0            
            except IndexError:
                print("ERROR. Hay un valor sin par. ")
                return 0
            finally:
                arch.close()               

            # Se calcula el primer renglón
            row1 = [len(w), sum(w), sum(x), sum(y), sum(z)]
            row2 = self.__wRow(w,x,y,z)
            row3 = self.__xRow(w,x,y,z)
            row4 = self.__yRow(w,x,y,z)
            
            # Se hace una matriz con todos los renglones para utilizarse en la función de gauss jordan
            mat = [row1,row2,row3,row4]
            bValues = self.__gauss(mat, len(mat))
            
            # Se calcula zk utilizando b0,b1,b2,b3, wk, xk y yk
            zk = bValues[0] + (bValues[1] * wk) + bValues[2] * xk + bValues[3] * yk

            self.__prettyPrint(len(w), wk, xk, yk, bValues,zk)

    # Función para calcular el segundo renglón
    #.i
    def __wRow(self,w, x, y, z):
        sumW = sum(w)
        sumW2 = sumWX =sumWY =sumWZ = 0

        for i in range(0,len(w)):
            sumW2 += pow(w[i],2)
            sumWX += w[i] * x[i]
            sumWY += w[i] * y[i]
            sumWZ += w[i] * z[i]
    
        row = [sumW, sumW2, sumWX, sumWY, sumWZ]
        return row

    # Función para calcular el tercer renglón
    #.i
    def __xRow(self,w, x, y, z):
        sumX= sum(x)
        sumWX = sumX2 = sumXY =sumXZ = 0

        for i in range(0,len(x)):
            sumWX += w[i] * x[i]
            sumX2 += pow(x[i],2)
            sumXY += x[i] * y[i]
            sumXZ += x[i] * z[i]
    
        row = [sumX, sumWX, sumX2, sumXY, sumXZ]
        return row 

    # Función para calcular el cuarto renglón
    #.i
    def __yRow(self,w, x, y, z):
        sumY = sum(y)
        sumWY = sumY2 = sumXY =sumYZ = 0

        for i in range(0,len(y)):
            sumWY += w[i] * y[i]
            sumXY += x[i] * y[i]
            sumY2 += pow(y[i],2)
            sumYZ += y[i] * z[i]
    
        row = [sumY, sumWY, sumXY, sumY2, sumYZ]
        return row   

    # Función de gauss jordan para diagonalizar la matriz
    #.i
    def __gauss(self,mat,n):
        bValues = np.zeros(n)
        try:
            for i in range(n):
                for j in range(n):
                    if (i != j):
                        div = mat[j][i]/mat[i][i]

                        for k in range(n + 1):
                            mat[j][k] = mat[j][k] - div * mat[i][k]

            for i in range(n):
                bValues[i] = mat[i][n]/mat[i][i]
            return bValues
    
        except ZeroDivisionError:
            print("Se dividió por 0\n")

    # Función para imprimir los elementos
    #.i #.m=8
    def __prettyPrint(self, n, wk, xk, yk,bValues,zk): 
        print("N = {}".format(n))
        print("wk = {:.4f}".format(wk))  
        print("xk = {:.4f}".format(xk))
        print("yk = {:.4f}".format(yk))
        print("------------")
        print("b0 = {:.4f}".format(bValues[0]))
        print("b1 = {:.4f}".format(bValues[1]))
        print("b2 = {:.4f}".format(bValues[2]))
        print("b3 = {:.5f}".format(bValues[3]))
        print("------------")
        print("zk = {:.5f}".format(zk))      