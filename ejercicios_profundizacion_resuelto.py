#!/usr/bin/env python
'''
Tipos de variables [Python]
Ejercicios de profundización
---------------------------
Autor: Inove Coding School
Version: 1.3

Descripcion:
Programa creado para que practiquen los conocimietos
adquiridos durante la semana
'''

__author__ = "Brian_boto"
__email__ = "brian.boto@gmail.com"
__version__ = "1.3"

def ej1():
    # Ejercicios de práctica con números
    print('Nuestra primera calculadora')
    
    print('Ingrese primer numero')
    Numero_1 = float(input())

    print('Ingrese segundo numero')
    Numero_2 = float(input())

    #Realice un calculadora, se ingresará por línea de comando dos
    #números reales y se deberá calcular todas las operaciones entre ellos:
    #- Suma
    suma = Numero_1 + Numero_2
    #- Resta
    resta = Numero_1 - Numero_2
    #- Multiplicación
    Multiplicación = Numero_1 * Numero_2
    #- División
    Division = Numero_1 / Numero_2
    #- Exponente/Potencia
    Potencia = Numero_1 ** Numero_2

    print('La suma entre', Numero_1, 'y', Numero_2, 'es', suma)
    print('La resta entre', Numero_1, 'y', Numero_2, 'es', resta)
    print('La multiplicacion entre', Numero_1, 'y', Numero_2, 'es', Multiplicación)
    print('La division entre', Numero_1, 'y', Numero_2, 'es', Division)
    print( Numero_1, 'elevado a', Numero_2, 'es', Potencia)

    #- Para todos los casos se debe imprimir en pantalla el resultado aclarando
      #la operación realizada en cada caso y con que números
      #se ha realizado la operación
      #ej: La suma entre 4.2 y 6.5 es 10.7

    


def ej2():
    print('Ejercicios de práctica numérica y cadenas')
    
    #Realice un programa que consulte por consola:
    #- El nombre completo de la persona
    print('Ingrese su nombre y apellido')
    nombre_apellido = str(input())
    #- El DNI de la persona
    print('Ingrese su numero de DNI')
    dni = str(input())
    #- La edad de la persona 
    print('Ingrese su edad')
    edad = str(input())
    #- La altura de la persona
    print('Ingrese su altura en metros')
    altura = str(input())
    print('Nombre Completo:',nombre_apellido, ', DNI:' , dni)
    print('Nombre Completo:',nombre_apellido, ', Edad:' , edad, ', Altura:' , altura)

    

    


def ej3():
    print('Ejercicios de práctica con cadenas')

    print('Ingrese nombre completo del padre 1')
    nombre_padre_1 = str(input())
    
    print('Ingrese nombre completo del padre 2')
    nombre_padre_2 = str(input())
    nombre_1, apellido_1 = nombre_padre_1.split(' ')
    nombre_2, apellido_2 = nombre_padre_2.split(' ')
    print('Ingrese nombre/s del hijo')
    nombre_hijo = str(input())
    print('El nombre completo del hijo es:', nombre_hijo,apellido_1,apellido_2)
    
'''
    Realice un programa que determine cual sería el apellido de una persona
    si se ingresaran los dos nombres completos de sus padres.
    Dicha persona deberá tener los apellidos de ambos padres

    - Primero el programa debe consultar el nombre completo del padre_1
    - Luego el programa debe consultar el nombre completo del padre_2
    - Luego debe consultar el nombre del hijo/a
    - Debe extraer los apellidos de los padres
    - Luego formar el nombre completo del hijo/a utilizando los apellidos
      de sus padres
      y el nombre ingresado de dicha persona
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre completo recomendamos usar
    el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca de este método
    que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus

    '''

def ej4():
    # Ejercicios de práctica con cadenas
    print('Comencemos a ponernos serios')

    print('Ingrese nombre y apellido de la primera persona')
    nombrecompleto_1 = str(input())
    print('Ingrese nombre y apellido de la segunda persona')
    nombrecompleto_2 = str(input())
    solonombre_1, soloapellido1 = nombrecompleto_1.split(' ')
    solonombre_2, soloapellido2 = nombrecompleto_2.split(' ')
    apellido_buscado = soloapellido2
    es_pariente = apellido_buscado in nombrecompleto_1
    print(nombrecompleto_2, 'es pariente de', nombrecompleto_1,'?', es_pariente)

    '''
    Realice un programa que determine si una persona_2
    es pariente de la persona_1
    Para facilitar el ejercicio solo ingresar un nombre
    y un apellido por persona
    Ingresar dichos datos como Nombre Apellido, es decir,
    primero el nombre y luego el apellido, separado por un espacio.
    - El programa debe consultar primero el nombre completo de la persona_1
    - Luego debe consultar el nombre completo de la persona_2
    - Debe extraer el apellido de la persona_2
    - Luego preguntar si apellido de la persona_2 está contenido
      en el nombre completo de la persona_1
    - En caso de contenerlo, son parientes
    - Imprimir en pantalla el resultado

    NOTA: Para extraer el apellido del nombre recomendamos
    usar el método "split"
    Mostraremos un ejemplo:

    direccion_completa = 'Monroe 2716'
    calle, altura = direccion_completa.split(' ')

    Les dejo por su cuenta a que busquen un poco más acerca
    de este método que seguramente utilizarán mucho de acá en adelante.
    Les dejamos un link con algunos ejemplos más:
    https://www.pythonforbeginners.com/dictionary/python-split

    Cualquier duda con el método split pueden consultarla por el campus
    
'''

def ej5():
    # Ejercicios de práctica con cadenas
    print('Ahora si! buena suerte!')
    print('Ingrese su nombre completo')
    nombrecompleto_1 = str(input())
    nombre1, apellido1 = nombrecompleto_1.split(' ')
    print('Su nombre en minusculas es:')
    print(nombrecompleto_1.lower())
    print('Su nombre en mayusculas es:')
    print(nombrecompleto_1.upper())
    print('Su nombre en con la primera letra en mayusculas es:')
    print(nombre1.capitalize(), apellido1.capitalize())
   
    '''Realice un programa que reciba por consola su nombre completo
    e imprima en pantalla su nombre en los siguientes formatos:
    - Todas las letras en minúsculas
    - Todas las letras en mayúsculas
    - Solo la primera letra del nombre en mayúscula

    NOTA: Para realizar este ejercicio deberá usar los siguientes métodos
    de strings:
    - lower
    - upper
    - capitalize

    Puede buscar en internet como usar en Python estos métodos.
    Les dejamos el siguiente link que posee casos de uso de algunos de ellos:

    Link de referencia:
    https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/

    Cualquier duda con estos métodos pueden consultarla por el campus
    '''

if __name__ == '__main__':
    print("Ejercicios de práctica")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
