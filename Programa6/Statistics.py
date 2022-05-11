# !/usr/bin/env python3
# Este programa calcula p dada una x y los grados de libertad
# Se usan varias funciones para tener más modularidad
#
# Mario Garza Chapa A01720245
#
# Creado: 22/04/2022

#.b=44
#.d=3
#.m=2

import math

class Statistics:
   #.i
    def getX(self, dof, targetP):        
        currX = 1.0             
        deltaInc = currX/2      
        maxE = 0.0000001   
        i = 0
        prevP = newP = self.distT(dof, currX)        

        if (newP < targetP):        
            currX += deltaInc
            dir = 1            
        elif (newP > targetP):            
            currX -= deltaInc
            dir = 0            
        
        prevP = newP
        newP = self.distT(dof, currX)             
        # Loop para calcular la x hasta que la p pasada y la nueva tengan un error menor a E

        while(True):   
            i += 1         
            if (newP < targetP):
                if (dir != 1):
                    deltaInc /= 2
                    dir = 1
                currX += deltaInc
                prevP = newP
                newP = self.distT(dof, currX)                

            elif (newP > targetP):
                if (dir != 0):
                    deltaInc /= 2
                    dir = 0
                currX -= deltaInc
                prevP = newP
                newP = self.distT(dof, currX)                
        
            if (abs(newP - prevP) < maxE):
                return currX

    #.i
    def distT(self, dof, x):     
        numSeg = 10
        W = round(x / numSeg,2)
        E = 0.0000001
        oldP = float(0.0)
        newP = float(0.0)
        constPart = self.__getConstant(dof)

        # While loop para seguir hasta que se cumpla prev - new < E
        # Se calcula F(x) en el for y también se calucla p dentro de los ifs
        while (True):        
            for i in range (0, numSeg + 1):
                fX = constPart * self.__getConstantExp(W * i,dof)
                if (i == 0 or i == numSeg):
                    newP += W/3 * fX
                elif(i % 2 == 0):
                    newP += W/3 * 2 * fX
                else:
                    newP += W/3 * 4 * fX

            # Se revisa si ya se puede terminar el ciclo o si se debe de continuar
            # con un número de segmentos mayor
            if (abs(oldP - newP )< E):
                break
            else:                                
                oldP = newP
                newP = 0
                numSeg *= 2
                W = x / numSeg
            
        #.m        
        return newP

    # Calcula la parte constante de la ecuación
    #.i
    def __getConstant(self, dof):
        top = (dof - 1) / 2
        bot = 0 if dof == 0 else (dof / 2) - 1 

        top = self.__getGamma(top)
        bot = self.__getGamma(bot)
        bot_2 = pow(dof * math.pi, 1/2)
        return round(top/(bot*bot_2),6)

    # Calcula el exponente de la parte constante
    #.i
    def __getConstantExp(self,x,dof):        
        return round(pow((1 + (pow(x,2))/dof),(-(dof+1)/2)),5)

    # Calcula la función gama con los grados de libertad que se proporcionaron
    #.i
    def __getGamma(self, dof):
        if (dof <= 0):
            return 1
        elif (dof == 1):
            return 1 * dof
        elif (dof == 1/2):        
            return math.sqrt(math.pi) * dof
        else:            
            return self.__getGamma(dof - 1) * dof


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
        x = self.getX(n - 2, 0.35)
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
        top = abs(r) * math.sqrt(n - 2)    
        bottom = math.sqrt(1 - rSquared)
        x = top/bottom        
        p = self.distT(n - 2,x)         
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
        #orden en el arreglo values
        #[n, r, rSquared, b0, b1, yk, xk, sig]
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