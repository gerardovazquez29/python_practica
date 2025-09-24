def hello():
    return "que pedo"
print(hello())


def hellos(greet,name):
    return f"{greet} {name}"
print(hellos('hola','Santiago'))


# docstring
def suma(a: int,b:int):
    """
    info: Nuestra app es chingona
    """
    return a + b
print(suma(6,8))

# scopes o alcances
# son variables de alcance global o local

global_variable = "Soy global"

# global keyword
tax = 16

def globalo():
    global tax # con global cambias la variable 
    tax = 18
    return tax
print(tax) # 16
print(globalo()) # 18
print(tax) # 18


# non local keyword
def outer():
    enclosing_variable = "Enclosing variable"

    def inner():
        nonlocal enclosing_variable
        enclosing_variable = "Enclosing modificado"

    inner()
    print(enclosing_variable) # Enclosing modificado

outer() # Enclosing variable


def saludar():
    print("Hola bienvenido a python Jr")

saludar() # Hola bienvenido a python Jr

# Funciones con parámetros pero sin retorno
def mostrar_mensaje(nombre):
    print(f"hola {nombre}, sigue practicando")

mostrar_mensaje("Santiago")
 # hola Santiago sigue practicando

# con *args
def suma_varios(*args): 
    """
    info: *args: recibe múltiples valores como una tupla.
    """
    return sum(args)
print(suma_varios(2,6,4,5,8)) # 25


# con **kwargs
def mostrar_info(**kwargs): 
    """
    info: **kwargs: recibe múltiples valores con nombre (diccionario).
    """
    for clave,valor in kwargs.items():
        print(f"{clave} = {valor}")
mostrar_info(nombre='Ana', edad=22, ciudad='Guadalajara')
""" 
nombre = Ana
edad = 22
ciudad = Guadalajara 
"""

# Funciones anidadas y funciones como objetos
def potencia(exponente):
    """
    info:   Se pueden asignar a variables.
            Retornar desde otras funciones.
            Pasar como parámetros
    """
    def elevar(base):
        return base ** exponente
    return elevar
elevar_cuadrado = potencia(2)
print(elevar_cuadrado(5)) # 25

# Funciones anónimas (lambda)
cuadrado = lambda x: x**2
print(cuadrado(4))  # 16
