# !/usr/bin/env python3
# Este programa calcula p dada una x y los grados de libertad
# Se usan varias funciones para tener más modularidad
#
# Mario Garza Chapa A01720245
#
# Creado: 22s/04/2022

#.b=44

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
        prev = 1
        new = 0
        constPart = self.__getConstant(dof)

        # While loop para seguir hasta que se cumpla prev - new < E
        # Se calcula F(x) en el for y también se calucla p dentro de los ifs
        while (True):        
            for i in range (0, numSeg + 1):
                fX = constPart * self.__getConstantExp(W * i,dof)
                if (i == 0 or i == numSeg):
                    new += W/3 * fX
                elif(i % 2 == 0):
                    new += W/3 * 2 * fX
                else:
                    new += W/3 * 4 * fX

            # Se revisa si ya se puede terminar el ciclo o si se debe de continuar
            # con un número de segmentos mayor
            if (prev - new < E):               
                break
            else:                                
                prev = new
                new = 0
                numSeg *= 2
                W = x / numSeg
        #.m
        return round(new,9)

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


  