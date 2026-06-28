# 05. Funciones y Módulos

## 🎯 Objetivos de Aprendizaje

Al finalizar esta unidad, podrás:

- Crear y utilizar funciones personalizadas
- Manejar parámetros y valores de retorno
- Aplicar el concepto de alcance (scope) de variables
- Importar y usar módulos de Python
- Organizar código en módulos reutilizables
- Utilizar librerías externas con pip

## 🔧 ¿Qué son las Funciones?

Las **funciones** son bloques de código reutilizable que realizan una tarea específica. Son como "mini-programas" dentro de tu programa principal.

### ¿Por qué usar funciones?

1. **Reutilización**: Escribir una vez, usar muchas veces
2. **Organización**: Dividir problemas complejos en partes simples
3. **Mantenimiento**: Más fácil encontrar y corregir errores
4. **Legibilidad**: Código más claro y comprensible

### Analogía: Receta de Cocina

```python
# Sin funciones (repetitivo y desorganizado)
print("Precalentar horno a 180°C")
print("Mezclar harina, huevos y leche")
print("Hornear por 30 minutos")

print("Precalentar horno a 180°C")  # Se repite código
print("Mezclar harina, huevos y leche")  # Se repite código
print("Hornear por 30 minutos")  # Se repite código

# Con funciones (organizado y reutilizable)
def hacer_pastel():
    """Función para hacer un pastel."""
    print("Precalentar horno a 180°C")
    print("Mezclar harina, huevos y leche")
    print("Hornear por 30 minutos")

# Usar la función
hacer_pastel()  # Primera vez
hacer_pastel()  # Segunda vez - sin repetir código
```

## 📚 Creando Funciones

### Sintaxis Básica

```python
def nombre_funcion(parametros):
    """Documentación de la función (docstring)."""
    # Código de la función
    return valor_de_retorno  # Opcional
```

### Ejemplos Básicos

```python
# Función simple sin parámetros
def saludar():
    """Imprime un saludo."""
    print("¡Hola, mundo!")

# Llamar la función
saludar()  # Output: ¡Hola, mundo!

# Función con parámetros
def saludar_persona(nombre):
    """Saluda a una persona específica."""
    print(f"¡Hola, {nombre}!")

# Llamar con argumentos
saludar_persona("Ana")     # Output: ¡Hola, Ana!
saludar_persona("Carlos")  # Output: ¡Hola, Carlos!

# Función con múltiples parámetros
def presentar_persona(nombre, edad, ciudad):
    """Presenta a una persona con su información."""
    print(f"Hola, soy {nombre}")
    print(f"Tengo {edad} años")
    print(f"Vivo en {ciudad}")

# Llamar con múltiples argumentos
presentar_persona("María", 28, "Madrid")
```

## 🔄 Valores de Retorno

Las funciones pueden **devolver** valores que se pueden usar en otras partes del programa.

```python
# Función que calcula y retorna un valor
def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    resultado = a + b
    return resultado

# Usar el valor retornado
total = sumar(5, 3)
print(f"5 + 3 = {total}")  # Output: 5 + 3 = 8

# Función con múltiples returns
def analizar_numero(numero):
    """Analiza si un número es positivo, negativo o cero."""
    if numero > 0:
        return "positivo"
    elif numero < 0:
        return "negativo"
    else:
        return "cero"

# Uso
resultado = analizar_numero(-5)
print(f"El número -5 es {resultado}")  # Output: El número -5 es negativo

# Función que retorna múltiples valores (tupla)
def calcular_estadisticas(numeros):
    """Calcula promedio, mínimo y máximo de una lista."""
    if not numeros:  # Lista vacía
        return None, None, None
    
    promedio = sum(numeros) / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    
    return promedio, minimo, maximo

# Desempaquetar múltiples valores
datos = [10, 20, 30, 40, 50]
prom, min_val, max_val = calcular_estadisticas(datos)
print(f"Promedio: {prom}, Min: {min_val}, Max: {max_val}")
```

## ⚙️ Parámetros Avanzados

### Parámetros por Defecto

```python
def crear_perfil(nombre, edad, ciudad="Madrid", activo=True):
    """Crea un perfil de usuario con valores por defecto."""
    perfil = {
        "nombre": nombre,
        "edad": edad,
        "ciudad": ciudad,
        "activo": activo
    }
    return perfil

# Diferentes formas de llamar la función
perfil1 = crear_perfil("Ana", 25)  # Usa valores por defecto
print(perfil1)  # {'nombre': 'Ana', 'edad': 25, 'ciudad': 'Madrid', 'activo': True}

perfil2 = crear_perfil("Carlos", 30, "Barcelona")  # Especifica ciudad
print(perfil2)  # {'nombre': 'Carlos', 'edad': 30, 'ciudad': 'Barcelona', 'activo': True}

perfil3 = crear_perfil("Luis", 35, activo=False)  # Parámetro nombrado
print(perfil3)  # {'nombre': 'Luis', 'edad': 35, 'ciudad': 'Madrid', 'activo': False}
```

### Argumentos Variables (*args y **kwargs)

```python
# *args - Número variable de argumentos posicionales
def sumar_todos(*numeros):
    """Suma cualquier cantidad de números."""
    return sum(numeros)

print(sumar_todos(1, 2, 3))        # 6
print(sumar_todos(10, 20, 30, 40)) # 100
print(sumar_todos(5))              # 5

# **kwargs - Argumentos con nombre variable
def crear_usuario(**info):
    """Crea un usuario con información flexible."""
    usuario = {}
    for clave, valor in info.items():
        usuario[clave] = valor
    return usuario

usuario1 = crear_usuario(nombre="Ana", edad=25, email="ana@email.com")
usuario2 = crear_usuario(nombre="Carlos", profesion="Ingeniero", salario=50000)

print(usuario1)  # {'nombre': 'Ana', 'edad': 25, 'email': 'ana@email.com'}
print(usuario2)  # {'nombre': 'Carlos', 'profesion': 'Ingeniero', 'salario': 50000}

# Combinando *args y **kwargs
def funcion_completa(requerido, *opcionales, **nombrados):
    """Función que acepta todos los tipos de argumentos."""
    print(f"Requerido: {requerido}")
    print(f"Opcionales: {opcionales}")
    print(f"Nombrados: {nombrados}")

funcion_completa("valor", 1, 2, 3, nombre="Ana", edad=25)
# Output:
# Requerido: valor
# Opcionales: (1, 2, 3)
# Nombrados: {'nombre': 'Ana', 'edad': 25}
```

## 🌍 Alcance de Variables (Scope)

El **scope** determina dónde una variable puede ser accedida en el código.

```python
# Variable global
nombre_global = "Variable global"

def ejemplo_scope():
    # Variable local
    nombre_local = "Variable local"
    
    print(f"Dentro de la función: {nombre_global}")  # Puede acceder a global
    print(f"Dentro de la función: {nombre_local}")   # Puede acceder a local

# Llamar función
ejemplo_scope()

print(f"Fuera de la función: {nombre_global}")  # ✅ Funciona
# print(f"Fuera de la función: {nombre_local}")   # ❌ Error - no existe aquí

# Modificar variable global
contador = 0

def incrementar_contador():
    global contador  # Declarar que usamos la variable global
    contador += 1
    print(f"Contador: {contador}")

incrementar_contador()  # Contador: 1
incrementar_contador()  # Contador: 2
print(f"Contador final: {contador}")  # Contador final: 2
```

## 📦 Módulos en Python

Los **módulos** son archivos Python que contienen funciones, clases y variables que puedes usar en otros programas.

### Módulos Incorporados

```python
# Módulo math - Funciones matemáticas
import math

print(math.pi)                    # 3.141592653589793
print(math.sqrt(16))              # 4.0
print(math.ceil(4.3))             # 5 (redondeo hacia arriba)
print(math.floor(4.8))            # 4 (redondeo hacia abajo)
print(math.factorial(5))          # 120

# Importar funciones específicas
from math import pi, sqrt, sin

print(pi)           # 3.141592653589793
print(sqrt(25))     # 5.0
print(sin(pi/2))    # 1.0

# Módulo random - Números aleatorios
import random

print(random.random())              # Número entre 0 y 1
print(random.randint(1, 10))        # Entero entre 1 y 10
print(random.choice(['a', 'b', 'c']))  # Elemento aleatorio de lista

# Barajar una lista
cartas = ['As', 'Rey', 'Reina', 'Jota']
random.shuffle(cartas)
print(cartas)  # Lista barajada

# Módulo datetime - Fechas y horas
from datetime import datetime, date, timedelta

ahora = datetime.now()
print(f"Fecha y hora actual: {ahora}")

hoy = date.today()
print(f"Fecha de hoy: {hoy}")

# Operaciones con fechas
ayer = hoy - timedelta(days=1)
mañana = hoy + timedelta(days=1)
print(f"Ayer: {ayer}, Mañana: {mañana}")
```

### Crear Módulos Personalizados

Crea un archivo `utilidades.py`:

```python
# utilidades.py
"""Módulo de utilidades matemáticas y de texto."""

def calcular_area_circulo(radio):
    """Calcula el área de un círculo."""
    import math
    return math.pi * radio ** 2

def calcular_area_rectangulo(largo, ancho):
    """Calcula el área de un rectángulo."""
    return largo * ancho

def limpiar_texto(texto):
    """Limpia y formatea un texto."""
    return texto.strip().title()

def contar_palabras(texto):
    """Cuenta las palabras en un texto."""
    return len(texto.split())

# Variable del módulo
VERSION = "1.0.0"
AUTOR = "Tu Nombre"
```

Usar el módulo personalizado:

```python
# programa_principal.py
import utilidades

# Usar funciones del módulo
area_circulo = utilidades.calcular_area_circulo(5)
print(f"Área del círculo: {area_circulo:.2f}")

area_rectangulo = utilidades.calcular_area_rectangulo(10, 6)
print(f"Área del rectángulo: {area_rectangulo}")

texto_limpio = utilidades.limpiar_texto("  hola mundo  ")
print(f"Texto limpio: '{texto_limpio}'")

# Acceder a variables del módulo
print(f"Versión: {utilidades.VERSION}")
print(f"Autor: {utilidades.AUTOR}")

# Importar funciones específicas
from utilidades import calcular_area_circulo, contar_palabras

area = calcular_area_circulo(3)
palabras = contar_palabras("Python es un lenguaje genial")
print(f"Área: {area:.2f}, Palabras: {palabras}")
```

## 📚 Librerías Externas con pip

**pip** es el gestor de paquetes de Python que permite instalar librerías externas.

### Instalar Librerías

```bash
# Instalar una librería
pip install requests

# Instalar múltiples librerías
pip install matplotlib pandas numpy

# Ver librerías instaladas
pip list

# Actualizar una librería
pip install --upgrade requests

# Desinstalar
pip uninstall requests
```

### Ejemplo: Usando requests para APIs

```python
# Primero instalar: pip install requests
import requests
import json

def obtener_datos_pokemon(nombre):
    """Obtiene información de un Pokémon usando la API pública."""
    url = f"https://pokeapi.co/api/v2/pokemon/{nombre.lower()}"
    
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()  # Lanza excepción si hay error HTTP
        
        datos = respuesta.json()
        
        # Extraer información relevante
        info_pokemon = {
            "nombre": datos["name"].title(),
            "altura": datos["height"] / 10,  # Convertir a metros
            "peso": datos["weight"] / 10,    # Convertir a kg
            "tipos": [tipo["type"]["name"] for tipo in datos["types"]],
            "habilidades": [hab["ability"]["name"] for hab in datos["abilities"]]
        }
        
        return info_pokemon
    
    except requests.exceptions.RequestException as e:
        return {"error": f"Error al obtener datos: {e}"}
    except KeyError as e:
        return {"error": f"Datos incompletos: {e}"}

# Usar la función
pokemon_info = obtener_datos_pokemon("pikachu")
if "error" not in pokemon_info:
    print(f"Nombre: {pokemon_info['nombre']}")
    print(f"Altura: {pokemon_info['altura']} m")
    print(f"Peso: {pokemon_info['peso']} kg")
    print(f"Tipos: {', '.join(pokemon_info['tipos'])}")
    print(f"Habilidades: {', '.join(pokemon_info['habilidades'])}")
else:
    print(pokemon_info["error"])
```

## 🎯 Ejemplo Integrador: Calculadora Avanzada

```python
# calculadora_avanzada.py
"""Calculadora avanzada con funciones organizadas."""

import math
from datetime import datetime

def mostrar_menu():
    """Muestra el menú principal de opciones."""
    print("\n" + "="*40)
    print("      CALCULADORA AVANZADA")
    print("="*40)
    print("1. Operaciones básicas")
    print("2. Operaciones avanzadas")
    print("3. Conversiones")
    print("4. Historial")
    print("5. Salir")
    print("-"*40)

def operaciones_basicas():
    """Maneja operaciones matemáticas básicas."""
    print("\n--- OPERACIONES BÁSICAS ---")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    opcion = input("Selecciona operación: ")
    
    try:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        
        if opcion == "1":
            resultado = sumar(a, b)
            operacion = f"{a} + {b}"
        elif opcion == "2":
            resultado = restar(a, b)
            operacion = f"{a} - {b}"
        elif opcion == "3":
            resultado = multiplicar(a, b)
            operacion = f"{a} × {b}"
        elif opcion == "4":
            resultado = dividir(a, b)
            operacion = f"{a} ÷ {b}"
        else:
            print("Opción inválida")
            return None
        
        print(f"Resultado: {operacion} = {resultado}")
        return {"operacion": operacion, "resultado": resultado, "timestamp": datetime.now()}
        
    except ValueError:
        print("Error: Ingresa números válidos")
        return None
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
        return None

def operaciones_avanzadas():
    """Maneja operaciones matemáticas avanzadas."""
    print("\n--- OPERACIONES AVANZADAS ---")
    print("1. Potencia")
    print("2. Raíz cuadrada")
    print("3. Logaritmo")
    print("4. Seno")
    print("5. Coseno")
    
    opcion = input("Selecciona operación: ")
    
    try:
        if opcion in ["1"]:  # Potencia necesita dos números
            base = float(input("Base: "))
            exponente = float(input("Exponente: "))
            resultado = potencia(base, exponente)
            operacion = f"{base}^{exponente}"
        else:  # Otras operaciones necesitan un número
            numero = float(input("Número: "))
            
            if opcion == "2":
                resultado = raiz_cuadrada(numero)
                operacion = f"√{numero}"
            elif opcion == "3":
                resultado = logaritmo(numero)
                operacion = f"log({numero})"
            elif opcion == "4":
                resultado = seno(numero)
                operacion = f"sin({numero})"
            elif opcion == "5":
                resultado = coseno(numero)
                operacion = f"cos({numero})"
            else:
                print("Opción inválida")
                return None
        
        print(f"Resultado: {operacion} = {resultado}")
        return {"operacion": operacion, "resultado": resultado, "timestamp": datetime.now()}
        
    except ValueError as e:
        print(f"Error: {e}")
        return None

def conversiones():
    """Maneja conversiones de unidades."""
    print("\n--- CONVERSIONES ---")
    print("1. Celsius a Fahrenheit")
    print("2. Fahrenheit a Celsius")
    print("3. Metros a Kilómetros")
    print("4. Kilómetros a Metros")
    
    opcion = input("Selecciona conversión: ")
    
    try:
        valor = float(input("Valor a convertir: "))
        
        if opcion == "1":
            resultado = celsius_a_fahrenheit(valor)
            operacion = f"{valor}°C a °F"
        elif opcion == "2":
            resultado = fahrenheit_a_celsius(valor)
            operacion = f"{valor}°F a °C"
        elif opcion == "3":
            resultado = metros_a_kilometros(valor)
            operacion = f"{valor}m a km"
        elif opcion == "4":
            resultado = kilometros_a_metros(valor)
            operacion = f"{valor}km a m"
        else:
            print("Opción inválida")
            return None
        
        print(f"Resultado: {operacion} = {resultado}")
        return {"operacion": operacion, "resultado": resultado, "timestamp": datetime.now()}
        
    except ValueError:
        print("Error: Ingresa un número válido")
        return None

# Funciones de cálculo
def sumar(a, b):
    """Suma dos números."""
    return a + b

def restar(a, b):
    """Resta dos números."""
    return a - b

def multiplicar(a, b):
    """Multiplica dos números."""
    return a * b

def dividir(a, b):
    """Divide dos números."""
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b

def potencia(base, exponente):
    """Calcula base elevado a exponente."""
    return base ** exponente

def raiz_cuadrada(numero):
    """Calcula la raíz cuadrada."""
    if numero < 0:
        raise ValueError("No se puede calcular raíz cuadrada de número negativo")
    return math.sqrt(numero)

def logaritmo(numero):
    """Calcula el logaritmo natural."""
    if numero <= 0:
        raise ValueError("No se puede calcular logaritmo de número no positivo")
    return math.log(numero)

def seno(angulo):
    """Calcula el seno (ángulo en grados)."""
    return math.sin(math.radians(angulo))

def coseno(angulo):
    """Calcula el coseno (ángulo en grados)."""
    return math.cos(math.radians(angulo))

# Funciones de conversión
def celsius_a_fahrenheit(celsius):
    """Convierte Celsius a Fahrenheit."""
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):
    """Convierte Fahrenheit a Celsius."""
    return (fahrenheit - 32) * 5/9

def metros_a_kilometros(metros):
    """Convierte metros a kilómetros."""
    return metros / 1000

def kilometros_a_metros(kilometros):
    """Convierte kilómetros a metros."""
    return kilometros * 1000

def mostrar_historial(historial):
    """Muestra el historial de operaciones."""
    if not historial:
        print("No hay operaciones en el historial")
        return
    
    print(f"\n--- HISTORIAL ({len(historial)} operaciones) ---")
    for i, entrada in enumerate(historial[-10:], 1):  # Últimas 10
        tiempo = entrada["timestamp"].strftime("%H:%M:%S")
        print(f"{i}. [{tiempo}] {entrada['operacion']} = {entrada['resultado']}")

def main():
    """Función principal de la calculadora."""
    historial = []
    
    print("¡Bienvenido a la Calculadora Avanzada!")
    
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            resultado = operaciones_basicas()
        elif opcion == "2":
            resultado = operaciones_avanzadas()
        elif opcion == "3":
            resultado = conversiones()
        elif opcion == "4":
            mostrar_historial(historial)
            resultado = None
        elif opcion == "5":
            print("¡Gracias por usar la calculadora!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")
            resultado = None
        
        # Agregar al historial si hay resultado
        if resultado:
            historial.append(resultado)

# Ejecutar calculadora
if __name__ == "__main__":
    main()
```

## 💡 Ejercicios Prácticos

### Ejercicio 1: Funciones de Validación

```python
def validar_email(email):
    """
    Valida si un email tiene formato básico correcto.
    Debe contener @ y al menos un punto después del @
    """
    # Tu código aquí
    pass

def validar_telefono(telefono):
    """
    Valida si un teléfono tiene formato correcto (solo números y guiones).
    """
    # Tu código aquí
    pass

def validar_codigo_postal(codigo):
    """
    Valida si un código postal español es válido (5 dígitos).
    """
    # Tu código aquí
    pass

# Tests
print(validar_email("usuario@email.com"))     # True
print(validar_email("usuario@email"))         # False
print(validar_telefono("123-456-789"))        # True
print(validar_codigo_postal("28001"))         # True
```

### Ejercicio 2: Módulo de Estadísticas

Crea un archivo `estadisticas.py`:

```python
# estadisticas.py
"""Módulo para cálculos estadísticos básicos."""

def media(numeros):
    """Calcula la media aritmética."""
    # Tu código aquí
    pass

def mediana(numeros):
    """Calcula la mediana."""
    # Tu código aquí
    pass

def moda(numeros):
    """Encuentra el valor más frecuente."""
    # Tu código aquí
    pass

def desviacion_estandar(numeros):
    """Calcula la desviación estándar."""
    # Tu código aquí
    pass
```

Luego úsalo en tu programa principal:

```python
import estadisticas

datos = [1, 2, 3, 4, 5, 5, 6, 7, 8, 9]
print(f"Media: {estadisticas.media(datos)}")
print(f"Mediana: {estadisticas.mediana(datos)}")
print(f"Moda: {estadisticas.moda(datos)}")
```

## 🎯 Puntos Clave

- ✅ Las funciones organizan y reutilizan código eficientemente
- ✅ Los parámetros por defecto hacen funciones más flexibles
- ✅ El scope determina donde las variables son accesibles
- ✅ Los módulos permiten organizar código en archivos separados
- ✅ pip instala librerías externas para expandir funcionalidad
- ✅ La documentación (docstrings) es esencial para código mantenible

## 🚀 Siguiente Paso

¡Felicidades! Has completado los fundamentos de programación en Python. En la siguiente fase aprenderemos sobre **Fundamentos de IA**, donde aplicaremos estos conocimientos para crear sistemas inteligentes.

---

### 📚 Recursos Adicionales

- [Python Functions Documentation](https://docs.python.org/3/tutorial/controlflow.html#defining-functions)
- [Python Module Documentation](https://docs.python.org/3/tutorial/modules.html)
- [PyPI - Python Package Index](https://pypi.org/)