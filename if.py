'''
Estructura de  control 
se utiliza paea timar decisiones 
basadas en expresiones condicionales
'''

#ejemplo 1: if simple
edad= int(input("ingresa tu edad: "))
documento = input ("tienes documento? (si/no)")
#condicional: Si la edad es mayor o igual a 18
if edad >= 18 and documento=='si':
 #codigo para cuando es mayor a 18
    print ("eres mayor de edad, puedes votar")
else:
    #codigo para cuando es menor a 18
    print ("Eres menor de edad,o no tienes documento")
#codigo que se ejecuta siempre
print("Fin del programa")