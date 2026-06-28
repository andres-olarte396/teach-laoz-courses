# ============================================================================
# EJEMPLO 04: ENTRADA DE DATOS DEL USUARIO
# ============================================================================
# Tema: Interacción con el usuario usando input()
# Objetivo: Crear programas interactivos
# Nivel: Principiante
# Prerrequisito: ejemplo_03_operaciones_basicas.py

print("=== CALCULADORA DE IMC INTERACTIVA ===")
print("Esta calculadora te ayudará a conocer tu Índice de Masa Corporal")

# Solicitar datos al usuario
nombre = input("¿Cuál es tu nombre? ")
print(f"¡Hola {nombre}! Vamos a calcular tu IMC.")

# Obtener peso y altura (convertir string a número)
peso_str = input("Ingresa tu peso en kilogramos: ")
peso = float(peso_str)

altura_str = input("Ingresa tu altura en metros (ej: 1.75): ")
altura = float(altura_str)

# Calcular IMC
imc = peso / (altura ** 2)

# Mostrar resultado
print(f"\n=== RESULTADOS PARA {nombre.upper()} ===")
print(f"Peso: {peso} kg")
print(f"Altura: {altura} m")
print(f"Tu IMC es: {imc:.2f}")

# Interpretación básica del IMC
print("\nInterpretación:")
if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"
    
print(f"Categoría: {categoria}")

# Ejercicio: Pregunta la edad y calcula cuántos días ha vivido la persona
print("\n--- Ejercicio adicional ---")
edad_str = input("¿Cuántos años tienes? ")
edad = int(edad_str)
dias_vividos = edad * 365
print(f"¡Has vivido aproximadamente {dias_vividos} días!")