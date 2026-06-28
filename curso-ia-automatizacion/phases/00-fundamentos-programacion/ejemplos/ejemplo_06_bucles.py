# ============================================================================
# EJEMPLO 06: BUCLES - REPETICIÓN DE CÓDIGO
# ============================================================================
# Tema: Estructuras de repetición - while y for
# Objetivo: Automatizar tareas repetitivas
# Nivel: Intermedio
# Prerrequisito: ejemplo_05_condicionales.py

print("=== CONTADOR DE PALABRAS EN TEXTO ===")

# Ejemplo con bucle while - Menú interactivo
opcion = ""
contador_analisis = 0

print("Analizador de texto interactivo")
print("Opciones disponibles:")
print("1. Analizar texto")
print("2. Ver estadísticas")
print("3. Salir")

# Bucle principal del programa
while opcion != "3":
    print(f"\n--- Análisis realizados: {contador_analisis} ---")
    opcion = input("Selecciona una opción (1-3): ")
    
    if opcion == "1":
        # Analizar texto
        texto = input("Ingresa un texto para analizar: ")
        
        # Estadísticas básicas
        num_caracteres = len(texto)
        num_caracteres_sin_espacios = len(texto.replace(" ", ""))
        
        # Contar palabras manualmente con bucle for
        palabras = texto.split()
        num_palabras = len(palabras)
        
        print("\n=== ANÁLISIS DEL TEXTO ===")
        print(f"Texto: '{texto}'")
        print(f"Caracteres totales: {num_caracteres}")
        print(f"Caracteres sin espacios: {num_caracteres_sin_espacios}")
        print(f"Número de palabras: {num_palabras}")
        
        # Analizar cada palabra con for
        print("\nAnálisis palabra por palabra:")
        for i, palabra in enumerate(palabras, 1):
            longitud = len(palabra)
            print(f"  {i}. '{palabra}' - {longitud} caracteres")
        
        # Encontrar la palabra más larga
        palabra_mas_larga = ""
        for palabra in palabras:
            if len(palabra) > len(palabra_mas_larga):
                palabra_mas_larga = palabra
        
        if palabra_mas_larga:
            print(f"Palabra más larga: '{palabra_mas_larga}' ({len(palabra_mas_larga)} caracteres)")
        
        # Contar vocales usando for
        vocales = "aeiouAEIOU"
        contador_vocales = 0
        for caracter in texto:
            if caracter in vocales:
                contador_vocales += 1
        
        print(f"Total de vocales: {contador_vocales}")
        
        contador_analisis += 1
        
    elif opcion == "2":
        # Mostrar estadísticas generales
        print("\n=== ESTADÍSTICAS GENERALES ===")
        print(f"Análisis realizados en esta sesión: {contador_analisis}")
        
        if contador_analisis > 0:
            print("¡Has estado activo analizando textos!")
        else:
            print("Aún no has realizado ningún análisis.")
            
    elif opcion == "3":
        print("¡Gracias por usar el analizador de texto!")
        
    else:
        print("Opción no válida. Por favor selecciona 1, 2 o 3.")

# Ejemplo adicional: Tabla de multiplicar con for
print("\n=== BONUS: TABLA DE MULTIPLICAR ===")
numero = int(input("¿De qué número quieres ver la tabla de multiplicar? "))

print(f"\nTabla del {numero}:")
for i in range(1, 11):  # del 1 al 10
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")

# Ejercicio: Crear un contador regresivo del 10 al 1 usando while