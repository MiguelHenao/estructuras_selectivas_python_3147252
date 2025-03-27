'''
if anidados
            Estructuras 
            que se encuentran
            
            Syntax
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Ejemplo 1:
        #Modificacion del ejercisio de votacion,
        #ahora solo puede votar si es mayor de edad
        pero si tiene documento
        #mostrar explicaciones en los otros casos
            
'''

edad = int(input("ingrese su edad:"))
if edad >= 18:
    documento = input("tiene documento? (si/no)")
    if documento =="si":
        print("usted puede votar")
    else:
        print("usted no puede votar por que no tiene documento")
else:
        print ("usted no puede votar por que es menor de edad")