# 01. Introducción a la Programación

## 🎯 Objetivos de Aprendizaje

Al finalizar esta unidad, podrás:

- Comprender qué es la programación y su importancia
- Conocer los conceptos fundamentales de la programación
- Identificar diferentes paradigmas de programación
- Entender el rol de la programación en IA y automatización
- Configurar tu primer entorno de desarrollo

## 🧠 ¿Qué es la Programación?

### Definición

La **programación** es el proceso de crear instrucciones para que una computadora realice tareas específicas. Es como escribir una receta detallada que la máquina puede seguir paso a paso.

```python
# Ejemplo simple: Saludo personalizado
nombre = "Estudiante"
print(f"¡Hola {nombre}! Bienvenido a la programación")
```

### ¿Por qué Programar?

1. **Automatización**: Eliminar tareas repetitivas
2. **Eficiencia**: Procesar grandes cantidades de datos
3. **Creatividad**: Crear soluciones innovadoras
4. **Oportunidades**: Acceso a carreras tecnológicas

## 🏗️ Conceptos Fundamentales

### 1. Algoritmo

Un **algoritmo** es una secuencia de pasos lógicos para resolver un problema.

**Ejemplo**: Algoritmo para hacer café
1. Llenar la cafetera con agua
2. Agregar café molido al filtro
3. Encender la cafetera
4. Esperar a que termine
5. Servir el café

### 2. Programa

Un **programa** es la implementación de un algoritmo en un lenguaje que la computadora entiende.

```python
# Algoritmo de saludo implementado en Python
def saludar_usuario():
    nombre = input("¿Cuál es tu nombre? ")
    edad = int(input("¿Cuál es tu edad? "))
    
    if edad >= 18:
        print(f"Hola {nombre}, eres mayor de edad")
    else:
        print(f"Hola {nombre}, eres menor de edad")

# Ejecutar el programa
saludar_usuario()
```

### 3. Lenguaje de Programación

Es un conjunto de reglas y sintaxis que permite comunicarse con la computadora.

**Ejemplos populares**:
- **Python**: Fácil de aprender, ideal para IA
- **JavaScript**: Para desarrollo web
- **Java**: Para aplicaciones empresariales
- **C++**: Para sistemas de alto rendimiento

## 🎨 Paradigmas de Programación

### 1. Programación Imperativa

Se enfoca en **cómo** hacer las cosas, paso a paso.

```python
# Ejemplo imperativo: Sumar números del 1 al 5
suma = 0
for i in range(1, 6):
    suma = suma + i
print(f"La suma es: {suma}")
```

### 2. Programación Funcional

Se enfoca en **qué** hacer usando funciones.

```python
# Ejemplo funcional: Misma tarea usando funciones
def sumar_numeros(n):
    return sum(range(1, n + 1))

resultado = sumar_numeros(5)
print(f"La suma es: {resultado}")
```

### 3. Programación Orientada a Objetos

Organiza el código en objetos que representan entidades del mundo real.

```python
# Ejemplo OOP: Clase para representar una cuenta bancaria
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito de ${cantidad}. Nuevo saldo: ${self.saldo}")
    
    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retiro de ${cantidad}. Nuevo saldo: ${self.saldo}")
        else:
            print("Fondos insuficientes")

# Uso de la clase
cuenta = CuentaBancaria("Juan Pérez", 1000)
cuenta.depositar(500)
cuenta.retirar(200)
```

## 🤖 Programación en IA y Automatización

### ¿Por qué Python para IA?

1. **Sintaxis simple**: Fácil de leer y escribir
2. **Librerías potentes**: NumPy, Pandas, TensorFlow, scikit-learn
3. **Comunidad activa**: Mucho soporte y recursos
4. **Versatilidad**: Desde scripts simples hasta sistemas complejos

### Ejemplo: IA Simple

```python
import random

# Simulador de IA básica para recomendar actividades
def recomendar_actividad(clima, hora):
    actividades_interiores = ["leer", "programar", "cocinar", "ejercicio en casa"]
    actividades_exteriores = ["caminar", "correr", "parque", "bicicleta"]
    
    if clima == "lluvioso":
        return random.choice(actividades_interiores)
    elif hora < 8 or hora > 20:
        return random.choice(actividades_interiores)
    else:
        return random.choice(actividades_exteriores)

# Uso de la "IA"
clima_actual = "soleado"
hora_actual = 14
recomendacion = recomendar_actividad(clima_actual, hora_actual)
print(f"Te recomiendo: {recomendacion}")
```

## 🛠️ Configuración del Entorno

### 1. Instalación de Python

**Windows**:

1. Descargar desde [python.org](https://python.org)
2. Ejecutar instalador
3. ✅ Marcar "Add Python to PATH"

**Verificación**:

```bash
python --version
pip --version
```

### 2. Editor de Código

**VS Code** (Recomendado):

1. Descargar desde [code.visualstudio.com](https://code.visualstudio.com)
2. Instalar extensión de Python
3. Configurar interpretador

### 3. Primer Programa

Crea un archivo `hola_mundo.py`:

```python
# Mi primer programa en Python
print("¡Hola, mundo de la programación!")

# Variables básicas
nombre = "Tu nombre aquí"
edad = 25
es_estudiante = True

# Mostrar información
print(f"Nombre: {nombre}")
print(f"Edad: {edad}")
print(f"¿Es estudiante?: {es_estudiante}")

# Operación matemática simple
a = 10
b = 5
suma = a + b
print(f"{a} + {b} = {suma}")
```

## 📝 Ejercicio Práctico

### Reto: Calculadora Personal

Crea un programa que:

1. Pida dos números al usuario
2. Muestre un menú de operaciones (+, -, *, /)
3. Realice la operación seleccionada
4. Muestre el resultado

```python
# Tu código aquí
# Pista: usa input() para obtener datos del usuario
# Pista: usa if/elif/else para el menú
```

## 🎯 Puntos Clave

- ✅ La programación es crear instrucciones para computadoras
- ✅ Los algoritmos son la base de todo programa
- ✅ Python es ideal para IA por su simplicidad y librerías
- ✅ Existen diferentes paradigmas de programación
- ✅ La práctica constante es clave para el aprendizaje

## 🚀 Siguiente Paso

En la siguiente unidad aprenderemos sobre **Lógica y Algoritmos**, donde profundizaremos en el pensamiento computacional y la resolución de problemas.

---

### 📚 Recursos Adicionales

- [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- [Automate the Boring Stuff](https://automatetheboringstuff.com/)
- [Python for Everybody](https://www.py4e.com/)