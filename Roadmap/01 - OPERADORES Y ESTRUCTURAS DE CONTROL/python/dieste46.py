# Operadores en Python

# Operadores aritméticos
suma = 5 + 3
resta = 5 - 3
multiplicacion = 5 * 3
division = 5 / 3
modulo = 5 % 3
exponente = 5 ** 3
division_entera = 5 // 3

print(suma, resta, multiplicacion, division, modulo, exponente, division_entera)

# Operadores de comparación
print(5 == 3)  # Falso
print(5 != 3)  # Verdadero
print(5 > 3)   # Verdadero
print(5 < 3)   # Falso
print(5 >= 3)  # Verdadero
print(5 <= 3)  # Falso

# Operadores de asignación
x = 5
x += 3
print(x)  # 8

# Operadores lógicos
print(True and False)  # Falso
print(True or False)   # Verdadero
print(not True)        # Falso

# Operadores de identidad
print(5 is 3)  # Falso
print(5 is not 3)  # Verdadero

# Operadores de pertenencia
print(5 in [1, 2, 3, 4, 5])  # Verdadero
print(5 not in [1, 2, 3, 4, 5])  # Falso

# Operadores de bits
print(5 & 3)  # AND
print(5 | 3)  # OR
print(5 ^ 3)  # XOR
print(~5)     # NOT
print(5 << 3) # Desplazamiento a la izquierda
print(5 >> 3) # Desplazamiento a la derecha

# Estructuras de control en Python

# Condicionales
if 5 > 3:
    print("5 es mayor que 3")
else:
    print("5 no es mayor que 3")

# Iterativas
for i in range(5):
    print(i)

# Excepciones
try:
    print(5 / 0)
except ZeroDivisionError:
    print("No se puede dividir por cero")

# DIFICULTAD EXTRA
for i in range(10, 56):
    if i % 2 == 0 and i != 16 and i % 3 != 0:
        print(i)