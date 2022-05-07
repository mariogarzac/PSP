#!/usr/bin/env python3
# Tiene como fin verificar que los valores sean correctos para poder calcular 
# la distribución T
#
# Mario Garza Chapa A01720245
#
# Creado: 22/04/2022

#.b=16
#.m=3
#.d

class Verificador:
    # Verifica que los datos sean correctos, en caso de ser incorrectos regresará
    # -1 para indicarlo.
    # Si son correctos, regresará los datos que ingreso el usuario.    
       
    #.i
    def verificaX(self):
        try:
            # Pide el input de x como float para poder procesar decimales
            x = float(input("Escribe la x que se utilizará: "))            
            if (x < 0):
                print("x debe de ser mayor a 0")
                return -1
            else:
                return x
        
        except ValueError:
            print("ERROR. Los valores deben de ser números. ")            
            return -1

    #.i
    def verificaDof(self):
        try:           
            dof = int(input("Escribe los grados de libertad: "))
            if (dof <= 0):
                print("dof debe de ser mayor a 0")
                return -1
            else:
                return dof
        except ValueError:
            print("ERROR. Los valores deben de ser números. ")
            print("Los grados de libertad no pueden ser decimales. ")
            return -1
        

    #.i
    def verificaP(self):
        try:
            p = float(input("Escribe la p que se utilizará: "))
            if (p < 0 or p > 0.5):                
                print("p debe de ser mayor a 0 y menor que 0.5")
                return -1
            else:
                return p          
        except ValueError:
            print("ERROR. Los valores deben de ser números. ")
            print("Los grados de libertad no pueden ser decimales. ")    
            return -1    

        
