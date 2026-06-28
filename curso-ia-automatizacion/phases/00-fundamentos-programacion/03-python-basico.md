# 03. Python Básico

## 🎯 Objetivos de Aprendizaje

Al finalizar esta unidad, podrás:

- Dominar la sintaxis básica de Python
- Trabajar con variables y tipos de datos
- Utilizar operadores matemáticos y lógicos
- Manejar entrada y salida de datos
- Aplicar buenas prácticas de codificación en Python

## 🐍 ¿Por qué Python?

### Características que lo hacen especial

- **Sintaxis simple**: Fácil de leer y escribir
- **Interpretado**: No necesita compilación
- **Multiplataforma**: Funciona en Windows, Mac, Linux
- **Versatil**: Web, IA, análisis de datos, automatización
- **Gran comunidad**: Millones de desarrolladores worldwide

### Python vs Otros Lenguajes

```python
# Python - Simple y claro
nombre = "María"
edad = 25
print(f"Hola {nombre}, tienes {edad} años")
```

```java
// Java - Más verboso
public class Saludo {
    public static void main(String[] args) {
        String nombre = "María";
        int edad = 25;
        System.out.println("Hola " + nombre + ", tienes " + edad + " años");
    }
}
```

## 📊 Variables y Tipos de Datos

### Variables en Python

Las variables son "cajas" que almacenan información. En Python no necesitas declararlas explícitamente.

```python
# Asignación de variables
nombre = "Ana"           # String (texto)
edad = 28               # Integer (entero)
altura = 1.65           # Float (decimal)
es_estudiante = True    # Boolean (verdadero/falso)

# Python es dinámico - puedes cambiar el tipo
x = 10        # x es entero
x = "Hola"    # Ahora x es string
x = 3.14      # Ahora x es float
```

### Reglas para Nombres de Variables

```python
# ✅ Válidos
nombre = "Juan"
edad_usuario = 25
precio_1 = 19.99
_variable_privada = "secreto"
CONSTANTE = 100

# ❌ Inválidos
# 2nombre = "Error"     # No puede empezar con número
# mi-variable = 10      # No se permiten guiones
# class = "Python"      # 'class' es palabra reservada
```

### Tipos de Datos Básicos

#### 1. Números (Numbers)

```python
# Enteros (int)
edad = 25
temperatura = -10
gran_numero = 1000000

# Decimales (float)
precio = 19.99
pi = 3.14159
cientifico = 1.5e-4  # Notación científica

# Operaciones básicas
a = 10
b = 3

suma = a + b        # 13
resta = a - b       # 7
multiplicacion = a * b  # 30
division = a / b    # 3.333...
division_entera = a // b  # 3
modulo = a % b      # 1 (resto de la división)
potencia = a ** b   # 1000 (10 elevado a 3)

print(f"10 + 3 = {suma}")
print(f"10 / 3 = {division:.2f}")  # 2 decimales
print(f"10 ** 3 = {potencia}")
```

#### 2. Texto (Strings)

```python
# Diferentes formas de crear strings
saludo = "Hola mundo"
mensaje = 'Python es genial'
texto_largo = """
Este es un texto
que abarca varias
líneas
"""

# Operaciones con strings
nombre = "Carlos"
apellido = "García"

# Concatenación
nombre_completo = nombre + " " + apellido
print(nombre_completo)  # "Carlos García"

# Formateo moderno (f-strings)
edad = 30
presentacion = f"Mi nombre es {nombre} y tengo {edad} años"
print(presentacion)

# Métodos útiles de strings
texto = "Python Programming"
print(texto.upper())        # "PYTHON PROGRAMMING"
print(texto.lower())        # "python programming"
print(texto.title())        # "Python Programming"
print(len(texto))          # 18 (longitud)
print(texto.count("P"))    # 2 (apariciones de "P")
print(texto.replace("Python", "Java"))  # "Java Programming"
```

#### 3. Booleanos (Boolean)

```python
# Valores booleanos
es_mayor_edad = True
tiene_licencia = False

# Operaciones lógicas
a = True
b = False

print(a and b)    # False (ambos deben ser True)
print(a or b)     # True (al menos uno debe ser True)
print(not a)      # False (negación)

# Comparaciones que devuelven booleanos
edad = 20
print(edad >= 18)      # True
print(edad == 20)      # True
print(edad != 25)      # True
```

## 🔧 Operadores

### Operadores Aritméticos

```python
x = 15
y = 4

print(f"Suma: {x} + {y} = {x + y}")           # 19
print(f"Resta: {x} - {y} = {x - y}")          # 11
print(f"Multiplicación: {x} * {y} = {x * y}") # 60
print(f"División: {x} / {y} = {x / y}")       # 3.75
print(f"División entera: {x} // {y} = {x // y}") # 3
print(f"Módulo: {x} % {y} = {x % y}")         # 3
print(f"Potencia: {x} ** {y} = {x ** y}")     # 50625
```

### Operadores de Comparación

```python
a = 10
b = 20

print(f"{a} == {b}: {a == b}")  # False (igual)
print(f"{a} != {b}: {a != b}")  # True (diferente)
print(f"{a} < {b}: {a < b}")    # True (menor que)
print(f"{a} > {b}: {a > b}")    # False (mayor que)
print(f"{a} <= {b}: {a <= b}")  # True (menor o igual)
print(f"{a} >= {b}: {a >= b}")  # False (mayor o igual)
```

### Operadores Lógicos

```python
# Simulación de sistema de acceso
edad = 22
tiene_id = True
es_miembro = False

# Puede entrar si es mayor de edad Y tiene ID
puede_entrar = edad >= 18 and tiene_id
print(f"¿Puede entrar? {puede_entrar}")  # True

# Descuento si es miembro O mayor de 65
edad_descuento = 70
descuento = es_miembro or edad_descuento >= 65
print(f"¿Tiene descuento? {descuento}")  # True

# Negación
no_es_miembro = not es_miembro
print(f"¿No es miembro? {no_es_miembro}")  # True
```

## 📥📤 Entrada y Salida de Datos

### Función `input()` - Recibir datos del usuario

```python
# Entrada básica (siempre devuelve string)
nombre = input("¿Cuál es tu nombre? ")
print(f"Hola, {nombre}!")

# Convertir a números
edad_str = input("¿Cuántos años tienes? ")
edad = int(edad_str)  # Convertir string a entero

# Forma más concisa
edad = int(input("¿Cuántos años tienes? "))
altura = float(input("¿Cuál es tu altura en metros? "))

# Ejemplo: Calculadora de IMC
peso = float(input("Ingresa tu peso en kg: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = peso / (altura ** 2)
print(f"Tu IMC es: {imc:.2f}")

if imc < 18.5:
    categoria = "Bajo peso"
elif imc < 25:
    categoria = "Peso normal"
elif imc < 30:
    categoria = "Sobrepeso"
else:
    categoria = "Obesidad"

print(f"Categoría: {categoria}")
```

### Función `print()` - Mostrar datos

```python
# Print básico
print("Hola mundo")

# Print con variables
nombre = "Luis"
edad = 25
print("Nombre:", nombre, "Edad:", edad)

# Print con separadores personalizados
print("Python", "es", "genial", sep=" - ")  # Python - es - genial
print("Línea 1", end=" | ")  # No salto de línea automático
print("Línea 2")  # Línea 1 | Línea 2

# F-strings (recomendado)
precio = 29.99
producto = "Libro de Python"
print(f"El {producto} cuesta ${precio:.2f}")

# Formateo avanzado
pi = 3.14159265359
print(f"Pi con 2 decimales: {pi:.2f}")        # 3.14
print(f"Pi en porcentaje: {pi:.1%}")          # 314.2%
print(f"Número con comas: {1234567:,}")       # 1,234,567
```

## 🎨 Buenas Prácticas de Codificación

### 1. Nombres Descriptivos

```python
# ❌ Nombres poco claros
x = 25
y = 1.75
z = x / (y * y)

# ✅ Nombres descriptivos
edad = 25
altura_metros = 1.75
indice_masa_corporal = edad / (altura_metros * altura_metros)
```

### 2. Comentarios Útiles

```python
# ❌ Comentarios obvios
x = x + 1  # Incrementar x

# ✅ Comentarios que explican el "por qué"
x = x + 1  # Compensar por el índice base-cero

# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    
    Args:
        radio (float): Radio del círculo en unidades
        
    Returns:
        float: Área del círculo
    """
    import math
    return math.pi * radio ** 2
```

### 3. Espaciado y Formato

```python
# ❌ Código mal formateado
def calcular(a,b,c):
    resultado=a+b*c
    if resultado>100:
        return resultado
    else:
        return 0

# ✅ Código bien formateado
def calcular(a, b, c):
    resultado = a + b * c
    
    if resultado > 100:
        return resultado
    else:
        return 0
```

## 💡 Ejercicios Prácticos

### Ejercicio 1: Información Personal

```python
def recopilar_informacion():
    """
    Programa que recopila y muestra información personal del usuario.
    """
    print("=== RECOPILACIÓN DE INFORMACIÓN ===")
    
    # Tu código aquí:
    # 1. Pedir nombre, edad, ciudad
    # 2. Calcular año de nacimiento aproximado
    # 3. Mostrar un resumen formateado
    pass

# Ejecutar
recopilar_informacion()
```

### Ejercicio 2: Calculadora de Propinas

```python
def calculadora_propinas():
    """
    Calcula la propina y el total a pagar.
    """
    print("=== CALCULADORA DE PROPINAS ===")
    
    # Tu código aquí:
    # 1. Pedir monto de la cuenta
    # 2. Pedir porcentaje de propina (15%, 18%, 20%)
    # 3. Calcular propina y total
    # 4. Mostrar desglose
    pass

# Ejecutar
calculadora_propinas()
```

### Ejercicio 3: Conversor de Unidades

```python
def conversor_unidades():
    """
    Convierte entre diferentes unidades de medida.
    """
    print("=== CONVERSOR DE UNIDADES ===")
    print("1. Metros a Kilómetros")
    print("2. Celsius a Fahrenheit")
    print("3. Kilogramos a Libras")
    
    # Tu código aquí:
    # 1. Mostrar menú de opciones
    # 2. Pedir selección del usuario
    # 3. Realizar la conversión correspondiente
    # 4. Mostrar el resultado
    pass

# Ejecutar
conversor_unidades()
```

## 🧪 Proyecto Integrador: Sistema de Calificaciones

```python
def sistema_calificaciones():
    """
    Sistema completo para calcular calificaciones de un estudiante.
    """
    print("=== SISTEMA DE CALIFICACIONES ===")
    
    # Datos del estudiante
    nombre = input("Nombre del estudiante: ")
    materia = input("Materia: ")
    
    # Calificaciones
    print("\nIngresa las calificaciones (0-100):")
    parcial_1 = float(input("Primer parcial (30%): "))
    parcial_2 = float(input("Segundo parcial (30%): "))
    tareas = float(input("Promedio de tareas (20%): "))
    examen_final = float(input("Examen final (20%): "))
    
    # Calcular promedio ponderado
    promedio = (parcial_1 * 0.30 + 
                parcial_2 * 0.30 + 
                tareas * 0.20 + 
                examen_final * 0.20)
    
    # Determinar letra y estado
    if promedio >= 90:
        letra = "A"
        estado = "Excelente"
    elif promedio >= 80:
        letra = "B"
        estado = "Muy bueno"
    elif promedio >= 70:
        letra = "C"
        estado = "Bueno"
    elif promedio >= 60:
        letra = "D"
        estado = "Regular"
    else:
        letra = "F"
        estado = "Reprobado"
    
    # Mostrar reporte
    print(f"\n{'='*40}")
    print(f"REPORTE DE CALIFICACIONES")
    print(f"{'='*40}")
    print(f"Estudiante: {nombre}")
    print(f"Materia: {materia}")
    print(f"{'─'*40}")
    print(f"Primer parcial (30%): {parcial_1:.1f}")
    print(f"Segundo parcial (30%): {parcial_2:.1f}")
    print(f"Tareas (20%): {tareas:.1f}")
    print(f"Examen final (20%): {examen_final:.1f}")
    print(f"{'─'*40}")
    print(f"PROMEDIO FINAL: {promedio:.2f}")
    print(f"CALIFICACIÓN: {letra}")
    print(f"ESTADO: {estado}")
    print(f"{'='*40}")

# Ejecutar sistema
sistema_calificaciones()
```

## 🎯 Puntos Clave

- ✅ Python tiene sintaxis simple y clara
- ✅ Las variables no necesitan declaración de tipo
- ✅ Los f-strings son la mejor forma de formatear texto
- ✅ `input()` siempre devuelve string, hay que convertir si es necesario
- ✅ Los nombres descriptivos mejoran la legibilidad del código
- ✅ Los comentarios deben explicar el "por qué", no el "qué"

## 🚀 Siguiente Paso

En la siguiente unidad aprenderemos sobre **Estructuras de Datos**, donde veremos listas, diccionarios y otras formas de organizar información de manera eficiente.

---

### 📚 Recursos Adicionales

- [Python Documentation](https://docs.python.org/3/)
- [Real Python Tutorials](https://realpython.com/)
- [Python String Formatting](https://pyformat.info/)