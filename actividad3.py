'''
Actividad 3:
Escribir un programa que calcule el salario neto de un trabajador
despues de descuentos y bonificaciones
=> INICIALMENTE, el programa debe solicitar un tipó de trabajadores entre los siguiente

a- contrato a termino indefinido
b-contrato por prestacion de servicios
c-contratode aprendizaje
d-jornal


=> Jornal:
Se debe solicitar:
-el tipo de unidad a pagar
-el numero de unidades hechas
- el valor de la unidad
el salario se calcula como
el valor_unidad * numero de unidades es mayor a 100
se le da un bonificacion del 10%

=> Contrato de aprendizaje
se debe solicitar el salario minimo 
el salario neto es 
el  75% del salario minimo

=> Contrato de prestacion de servicio
se debe solicitar
- el valor del contrato
-el numero de meses trabajados
-antiguedad en la empresa

Se calcula dividiendo el valor del contrato entre el numero de meses trabajados
-Si la antiguedad es menor a 2 años
se le aumenta el 2% al salario mensual
-Si la antiguedad esta entre 2 y 5 años
se le aumenta el 5% al salario mensual
-Si la antiguedad es mayor a 5 años
se le aumenta el 10% al salario mensual
descuento de ley
8% de salud
10% de pension
1% de caja de compensacion
=> contrato a termino indefinido
el salario mensual se calcula en base a la
siguiente tabla:
de escalafones o grados:
- 1: 1.5 veces el SMLV
- 2: 1.7 veces el SMLV
- 3: 2 veces el SMLV
- 4: 2.5 veces el SMLV
- 5: 3 veces el SMLV
el programa debe solicitar 
el escalafon o grado
el empleado
-las bonificaciones y
descuentos de ley son las mismas
que en el caso b
'''


salario_neto = 0

# Pedir el tipo de empleado
tipo_empleado = input("Ingrese el tipo de empleado (a, b, c, d): ").strip().lower()

# Verificar si el usuario eligió "a"
if tipo_empleado == "a":
    print("Ha ingresado término indefinido")

    # Pedir datos del salario y escalafón
    SMLV = float(input("Ingrese el SMLV: "))
    escalafon = int(input("Ingrese el escalafón (1-5): "))

    # Determinar salario base según escalafón
    if escalafon == 1:
        salario_mensual = 1.5 * SMLV
    elif escalafon == 2:
        salario_mensual = 1.7 * SMLV
    elif escalafon == 3:
        salario_mensual = 2 * SMLV
    elif escalafon == 4:
        salario_mensual = 2.5 * SMLV
    elif escalafon == 5:
        salario_mensual = 3 * SMLV
    else:
        print("Escalafón no válido")
        salario_mensual = 0

    if salario_mensual > 0:
        antiguedad = int(input("Ingrese la antigüedad en la empresa (en años): "))

        # Aplicar bonificación según antigüedad
        if antiguedad < 2:
            bonificacion = salario_mensual * 0.02
        elif 2 <= antiguedad <= 5:
            bonificacion = salario_mensual * 0.05
        else:
            bonificacion = salario_mensual * 0.10

        salario_mensual += bonificacion  # Sumar bonificación

        # Aplicar descuentos de ley
        descuento_salud = salario_mensual * 0.08
        descuento_pension = salario_mensual * 0.10
        descuento_caja = salario_mensual * 0.01

        salario_neto = salario_mensual - (descuento_salud + descuento_pension + descuento_caja)

    
    
    
    
elif tipo_empleado == "b" : 
    print("ha ingresado prestacion de servicios")
    valor_contrato = int(input("ingrese el valor de el contrato:"))
    numero_meses = int(input("ingrese el numero de meses trabajados:"))
    antiguedad =int(input("ingrese la antiguedad de la empresa:"))
    salario_mensual = valor_contrato / numero_meses
    #bonificaciones : elif anidados
    if antiguedad <2:
        bonificacion = salario_mensual * 0.02
        salario_mensual = salario_mensual + bonificacion
    elif antiguedad >= 2 and antiguedad <= 5:
        bonificacion = salario_mensual *0.05
        salario_mensual = salario_mensual + bonificacion
    elif antiguedad >5:
        bonificacion = salario_mensual *0.10
        salario_mensual = salario_mensual+ bonificacion
        #descuentos
        descuento_Salud = salario_mensual *0.08
        descuento_pension =salario_mensual *0.10
        descuento_caja = salario_mensual *0.01
        salario_neto = salario_mensual - descuento_Salud - descuento_pension - descuento_caja + bonificacion
    
    
    
    
    
    
elif tipo_empleado == "c" :
    print("ha ingresado contrato de aprendizaje")
    salario_minimo = int(input("ingrese el salario minimo"))
    descuento = salario_minimo * 0.25
elif tipo_empleado == "d" :
    print("ha ingresado jornal")
    #
    #variables locales
    #variables que solo pueden ser
    #reconocidas y asignadas en un bloque 
    #de codigo especifico
    
    tipo_unidad = input("ingrese el tipo de unidad:")
    numero_unidades= int(input("ingrese el numero de"+ tipo_unidad + "hechas:")) 
    valor_unidad = int(input("ingrese el valor de" + tipo_unidad))
    salario_neto = numero_unidades * valor_unidad
else:
    print ("tipo de empleado no valido")
print("el salario neto es:",salario_neto)
print("fin del programa")
    