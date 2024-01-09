# Funciones en Python

# Función sin parámetros ni retorno
def saludo():
    print("¡Hola, mundo!")

saludo()

# Función con un parámetro
def saludo_personalizado(nombre):
    print(f"¡Hola, {nombre}!")

saludo_personalizado("Python")

# Función con retorno
def suma(a, b):
    return a + b

print(suma(5, 3))

# Función dentro de función
def operaciones(a, b):
    def suma():
        return a + b
    def resta():
        return a - b
    return suma(), resta()

print(operaciones(5, 3))

# Variable global
variable_global = "Soy global"

def prueba_global():
    # Variable local
    variable_local = "Soy local"
    print(variable_global)
    print(variable_local)

prueba_global()

# DIFICULTAD EXTRA
def imprime_cadenas(cadena1, cadena2):
    contador = 0
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print(cadena1 + cadena2)
        elif i % 3 == 0:
            print(cadena1)
        elif i % 5 == 0:
            print(cadena2)
        else:
            print(i)
            contador += 1
    return contador

print(imprime_cadenas("Hola", "Mundo"))