
import math

def getConstant(self, dof):
    top = (dof - 1) / 2
    bot = (dof / 2) - 1 
    top = getGamma(top)
    bot = getGamma(bot)
    bot_2 = pow(9*math.pi,1/2)
    return round(top/(bot*bot_2),5)

def getGamma(dof):
    if (dof == 1):
        return 1 * dof
    elif (dof == 1/2):        
        return math.sqrt(math.pi) * dof
    else:        
        return getGamma(dof - 1) * dof

    