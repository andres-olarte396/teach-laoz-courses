# ============================================================================
# EJEMPLO 09: FUNCIONES - CÓDIGO REUTILIZABLE
# ============================================================================
# Tema: Funciones y modularización
# Objetivo: Crear código organizado y reutilizable
# Nivel: Intermedio-Avanzado
# Prerrequisito: ejemplo_08_diccionarios.py

print("=== CALCULADORA CIENTÍFICA MODULAR ===")

# Funciones matemáticas básicas
def sumar(a, b):
    """Suma dos números"""
    return a + b

def restar(a, b):
    """Resta dos números"""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números"""
    return a * b

def dividir(a, b):
    """Divide dos números (maneja división por cero)"""
    if b == 0:
        return "Error: División por cero"
    return a / b

# Funciones avanzadas
def potencia(base, exponente):
    """Calcula base elevado a la potencia del exponente"""
    return base ** exponente

def raiz_cuadrada(numero):
    """Calcula la raíz cuadrada de un número"""
    if numero < 0:
        return "Error: No se puede calcular raíz cuadrada de número negativo"
    return numero ** 0.5

def factorial(n):
    """Calcula el factorial de un número"""
    if n < 0:
        return "Error: Factorial no definido para números negativos"
    if n == 0 or n == 1:
        return 1
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

# Funciones de análisis estadístico
def calcular_promedio(numeros):
    """Calcula el promedio de una lista de números"""
    if not numeros:
        return "Error: Lista vacía"
    return sum(numeros) / len(numeros)

def encontrar_mayor(numeros):
    """Encuentra el número mayor en una lista"""
    if not numeros:
        return "Error: Lista vacía"
    
    mayor = numeros[0]
    for numero in numeros:
        if numero > mayor:
            mayor = numero
    return mayor

def encontrar_menor(numeros):
    """Encuentra el número menor en una lista"""
    if not numeros:
        return "Error: Lista vacía"
    
    menor = numeros[0]
    for numero in numeros:
        if numero < menor:
            menor = numero
    return menor

def calcular_rango(numeros):
    """Calcula el rango (diferencia entre mayor y menor)"""
    if not numeros:
        return "Error: Lista vacía"
    return encontrar_mayor(numeros) - encontrar_menor(numeros)

# Función para obtener números del usuario
def obtener_numeros():
    """Obtiene una lista de números del usuario"""
    numeros = []
    print("Ingresa números (presiona Enter sin escribir nada para terminar):")
    
    while True:
        entrada = input("Número: ")
        if entrada == "":
            break
        try:
            numero = float(entrada)
            numeros.append(numero)
        except ValueError:
            print("Por favor ingresa un número válido")
    
    return numeros

# Función para mostrar menú
def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n=== CALCULADORA CIENTÍFICA ===")
    print("1. Operaciones básicas")
    print("2. Operaciones avanzadas") 
    print("3. Análisis estadístico")
    print("4. Convertidor de unidades")
    print("5. Salir")

# Función para operaciones básicas
def menu_operaciones_basicas():
    """Menú para operaciones matemáticas básicas"""
    print("\nOperaciones básicas:")
    print("1. Suma")
    print("2. Resta") 
    print("3. Multiplicación")
    print("4. División")
    
    opcion = input("Selecciona operación: ")
    
    if opcion in ["1", "2", "3", "4"]:
        try:
            a = float(input("Primer número: "))
            b = float(input("Segundo número: "))
            
            if opcion == "1":
                resultado = sumar(a, b)
                operacion = "suma"
            elif opcion == "2":
                resultado = restar(a, b)
                operacion = "resta"
            elif opcion == "3":
                resultado = multiplicar(a, b)
                operacion = "multiplicación"
            else:  # opcion == "4"
                resultado = dividir(a, b)
                operacion = "división"
            
            print(f"Resultado de la {operacion}: {resultado}")
            
        except ValueError:
            print("Error: Ingresa números válidos")
    else:
        print("Opción no válida")

# Función para operaciones avanzadas
def menu_operaciones_avanzadas():
    """Menú para operaciones matemáticas avanzadas"""
    print("\nOperaciones avanzadas:")
    print("1. Potencia")
    print("2. Raíz cuadrada")
    print("3. Factorial")
    
    opcion = input("Selecciona operación: ")
    
    try:
        if opcion == "1":
            base = float(input("Base: "))
            exponente = float(input("Exponente: "))
            resultado = potencia(base, exponente)
            print(f"{base} elevado a la {exponente} = {resultado}")
            
        elif opcion == "2":
            numero = float(input("Número: "))
            resultado = raiz_cuadrada(numero)
            print(f"Raíz cuadrada de {numero} = {resultado}")
            
        elif opcion == "3":
            numero = int(input("Número (entero): "))
            resultado = factorial(numero)
            print(f"Factorial de {numero} = {resultado}")
            
        else:
            print("Opción no válida")
            
    except ValueError:
        print("Error: Ingresa números válidos")

# Función para análisis estadístico
def menu_analisis_estadistico():
    """Menú para análisis estadístico de datos"""
    numeros = obtener_numeros()
    
    if not numeros:
        print("No se ingresaron números")
        return
    
    print(f"\nNúmeros ingresados: {numeros}")
    print(f"Cantidad de números: {len(numeros)}")
    print(f"Promedio: {calcular_promedio(numeros):.2f}")
    print(f"Número mayor: {encontrar_mayor(numeros)}")
    print(f"Número menor: {encontrar_menor(numeros)}")
    print(f"Rango: {calcular_rango(numeros)}")
    print(f"Suma total: {sum(numeros)}")

# Funciones de conversión
def celsius_a_fahrenheit(celsius):
    """Convierte Celsius a Fahrenheit"""
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    """Convierte Fahrenheit a Celsius"""
    return (fahrenheit - 32) * 5/9

def metros_a_pies(metros):
    """Convierte metros a pies"""
    return metros * 3.28084

def pies_a_metros(pies):
    """Convierte pies a metros"""
    return pies / 3.28084

# Función para convertidor de unidades
def menu_convertidor():
    """Menú para conversión de unidades"""
    print("\nConvertidor de unidades:")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Metros a Pies")
    print("4. Pies a Metros")
    
    opcion = input("Selecciona conversión: ")
    
    try:
        if opcion == "1":
            celsius = float(input("Temperatura en Celsius: "))
            fahrenheit = celsius_a_fahrenheit(celsius)
            print(f"{celsius}°C = {fahrenheit:.2f}°F")
            
        elif opcion == "2":
            fahrenheit = float(input("Temperatura en Fahrenheit: "))
            celsius = fahrenheit_a_celsius(fahrenheit)
            print(f"{fahrenheit}°F = {celsius:.2f}°C")
            
        elif opcion == "3":
            metros = float(input("Distancia en metros: "))
            pies = metros_a_pies(metros)
            print(f"{metros} metros = {pies:.2f} pies")
            
        elif opcion == "4":
            pies = float(input("Distancia en pies: "))
            metros = pies_a_metros(pies)
            print(f"{pies} pies = {metros:.2f} metros")
            
        else:
            print("Opción no válida")
            
    except ValueError:
        print("Error: Ingresa un número válido")

# Programa principal
def main():
    """Función principal del programa"""
    print("¡Bienvenido a la Calculadora Científica!")
    
    while True:
        mostrar_menu()
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            menu_operaciones_basicas()
        elif opcion == "2":
            menu_operaciones_avanzadas()
        elif opcion == "3":
            menu_analisis_estadistico()
        elif opcion == "4":
            menu_convertidor()
        elif opcion == "5":
            print("¡Gracias por usar la calculadora!")
            break
        else:
            print("Opción no válida")

# Ejecutar programa principal
if __name__ == "__main__":
    main()

# Ejercicio: Agregar funciones para calcular área y perímetro de figuras geométricas