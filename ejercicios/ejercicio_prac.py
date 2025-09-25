# Ejercicios propuestos (sin solución)

# 1-Crea una función que reciba dos números y devuelva cuál es mayor.
def num_mayor(num1,num2):
    if num1 > num2 :
        mayor = num1
    elif num2 > num1:
        mayor = num2
    else:
        mayor = "son iguales"
    return print(f"el numero mayor es:{mayor}")
num_mayor(5,7) # el numero mayor es:7
            
# 2-Crea una función que calcule el área de un círculo (usa π ≈ 3.1416).
def area_circulo(radio):
    return 3.1416 * radio **2
radio = 6
area = area_circulo(radio)
print(f"El area del circulo con radio {radio} es: {area:.2f}")
  #  El area del circulo con radio 6 es: 113.10


# 3-Escribe una función que reciba un número y diga si es primo o no.
def num_primo(num):
    """ if num > 2 :
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False """
    for i in range(3, int(num**0.5) + 1,2):
        if num % i == 0:
            return False
    return True
print(num_primo(7))

# 4-Crea una función que reciba una lista de números y devuelva la suma de los pares.


# 5-Haz una función que reciba un texto y devuelva cuántas vocales tiene.


# 6-Implementa una calculadora con funciones para sumar, restar, multiplicar y dividir.


# 7-Usa *args para hacer una función que calcule el promedio de cualquier 
# cantidad de números.


# 8-Usa **kwargs para crear una función que muestre la información de una persona 
# (nombre, edad, ciudad, etc.).
