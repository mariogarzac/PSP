
import math

class Statistics:
    def distT(self, dof, x):
        print("Calculating dist T... ")
        numSeg = 10
        W = round(x / numSeg,2)
        E = 0.0000001
        prev = new = 0   
        constPart = self.getConstant(dof)

        # While loop para seguir hasta que se cumpla prev - new < E
        # Se calcula F(x) en el for y también se calucla p dentro de los ifs
        #while (True):
        # En este for se calcula la función F(x)
        for i in range (0, numSeg + 1):
            fX = round(constPart * self.getConstantExp(W*i,dof),5)            
            if (i == 0 or i == numSeg):
                new += W/3 * fX                
            elif(i % 2 == 0):
                new += W/3 * 2 * fX                                
            else:
                new += W/3 * 4 * fX                
                
        return new


    def getConstant(self, dof):
        top = (dof - 1) / 2
        bot = 0 if dof == 0 else (dof / 2) - 1 

        top = self.getGamma(top)
        bot = self.getGamma(bot)
        bot_2 = pow(dof * math.pi, 1/2)
        return round(top/(bot*bot_2),6)

    def getConstantExp(self,x,dof):        
        return round(pow((1 + (pow(x,2))/dof),(-(dof+1)/2)),5)

    def getGamma(self, dof):
        if (dof <= 0):
            return 1
        elif (dof == 1):
            return 1 * dof
        elif (dof == 1/2):        
            return math.sqrt(math.pi) * dof
        else:            
            return self.getGamma(dof - 1) * dof


  