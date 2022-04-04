
import math

class Statistics:
    def getConstant(self, dof):
        top = (dof - 1) / 2
        bot = (dof / 2) - 1 
        top = self.getGamma(top)
        bot = self.getGamma(bot)
        bot_2 = pow(9*math.pi,1/2)
        return round(top/(bot*bot_2),6)

    def getGamma(self, dof):
        if (dof <= 0):
            return 0
        if (dof == 1):
            return 1 * dof
        elif (dof == 1/2):        
            return math.sqrt(math.pi) * dof
        else:        
            return self.getGamma(dof - 1) * dof

  