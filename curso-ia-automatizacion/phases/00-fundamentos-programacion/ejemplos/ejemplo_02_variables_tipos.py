# ============================================================================
# EJEMPLO 02: VARIABLES Y TIPOS DE DATOS
# ============================================================================
# Tema: Variables y tipos básicos
# Objetivo: Entender los diferentes tipos de datos en Python
# Nivel: Principiante
# Prerrequisito: ejemplo_01_hola_mundo.py

# Variables numéricas
edad = 25
altura = 1.75
peso = 70.5

print(f"Edad: {edad} años")
print(f"Altura: {altura} metros")
print(f"Peso: {peso} kg")

# Variables de texto (string)
nombre = "Ana García"
apellido = "López"
nombre_completo = nombre + " " + apellido

print(f"Nombre completo: {nombre_completo}")

# Variables booleanas
es_estudiante = True
tiene_trabajo = False

print(f"¿Es estudiante? {es_estudiante}")
print(f"¿Tiene trabajo? {tiene_trabajo}")

# Verificar tipos de datos
print("\nTipos de datos:")
print(f"edad es tipo: {type(edad)}")
print(f"altura es tipo: {type(altura)}")
print(f"nombre es tipo: {type(nombre)}")
print(f"es_estudiante es tipo: {type(es_estudiante)}")

# Ejercicio: Crea variables para describir tu mascota ideal
# (nombre, especie, edad, es_domestico)