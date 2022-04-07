#!/usr/bin/env python3
# Tiene como fin verificar que los valores sean correctos para poder calcular 
# la distribución T
#
# Mario Garza Chapa A01720245
#
# Creado: 6/04/2022

#.b=15
#.d=12
#.m=3

class Verificador:
    # Verifica que los datos sean correctos, en caso de ser incorrectos regresará
    # -1 para indicarlo.
    # Si son correctos, regresará los datos que ingreso el usuario.    
    #.i
    def verificaDatos(self):
        try:
            # Pide el input de x como float para poder procesar decimales
            x = float(input("Escribe la x que se utilizará: "))            
            if (x < 0):
                print("x debe de ser mayor a 0")
                return -1, -1
                
            # pide el input como entero porque no se puede tener decimales en los grados de libertad
            dof = int(input("Escribe los grados de libertad: "))
            if (dof < 0):
                print("dof debe de ser mayor a 0")
                return -1, -1
        # si el valor es algo que no sea un número, lo rechazará.
        except ValueError:
            print("ERROR. Los valores deben de ser números. ")
            print("Los grados de libertad no pueden ser decimales. ")
            return -1, -1
        
        return x,dof
