'''
operadores lógicos

aquellos que operan unicamente
con valores booleanos (V F)
Acorde a las tablas de verdad
'''
#Ejemplo 1: Operador not:

y = not True 
print("el resultado de operador con not es",y)

#ejemlo 2:operador and
y=False and True
print("El resultado de operar con and es", y)

#ejemplo 3: Operador or
y = False or False
print("El resultado de operar con or e ",y)

'''
Jerarquia de precedencia de operadores
(logicos inclusive)
1. ()
2. **
3. *, /, %,
4. +, -
5. >, <, >=, <=, !=, ==
6. not
7.and
8.or
9.=
'''

#ejemplo 4: Jerarquia de operadores
y = False and not true or False
print("El resultado de operar con jerearquia de operadores es ",y)