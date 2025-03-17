'''
if en cascada:
Estructura de control que permite
evaluar varias condiciones en
cascada, es decir, si la primera
condicion no se comple,
se evalua la siguiente 
y asi sucesivamente
'''

#Ejemplo 1
#Modificar el programa de votacion
#para que considere las edad de 17
#años

edad = int(input ("ingresa tu edad: "))
if edad >18:
    print("puedes votar")
elif edad == 17:
    print("puedes votar el proximo año")
elif edad ==18:
    print("es tu primera vez votando y y tienes contraseña")
elif edad <=10:
    print("el bebe tiene registro civil")
    
    
    
elif edad < 17:
    print("no puedes votar aun")