# 🧪 Test de Evaluación - Fase 00: Fundamentos de Programación

## 📋 Información General

- **Fase**: 00 - Fundamentos de Programación
- **Duración estimada**: 90-120 minutos
- **Modalidad**: Práctica con código
- **Puntaje total**: 100 puntos
- **Puntaje mínimo para aprobar**: 70 puntos

## 🎯 Objetivos de Evaluación

Este test evalúa tu dominio de:

✅ Variables y tipos de datos  
✅ Operadores y expresiones  
✅ Estructuras de control (condicionales y bucles)  
✅ Estructuras de datos (listas y diccionarios)  
✅ Funciones y modularización  
✅ Manejo básico de archivos  
✅ Resolución de problemas algorítmicos

## 📊 Distribución de Puntos

| Sección   | Ejercicios | Puntos      | Conceptos Evaluados        |
| --------- | ---------- | ----------- | -------------------------- |
| A         | 3          | 15 pts      | Variables y tipos de datos |
| B         | 3          | 15 pts      | Operadores y cálculos      |
| C         | 3          | 20 pts      | Condicionales y lógica     |
| D         | 2          | 15 pts      | Bucles y repetición        |
| E         | 2          | 15 pts      | Listas y manipulación      |
| F         | 2          | 10 pts      | Diccionarios               |
| G         | 1          | 10 pts      | Funciones                  |
| **Total** | **16**     | **100 pts** | **Todos los conceptos**    |

---

## 📝 SECCIÓN A: Variables y Tipos de Datos (15 puntos)

### A1. Análisis de Variables (5 puntos)

Dado el siguiente código, indica qué imprimirá cada línea:

```python
nombre = "Python"
version = 3.12
es_moderno = True
año = 2024

print(type(nombre))
print(len(nombre))
print(version + año)
print(es_moderno and version > 3)
```

**Tu respuesta:**

```
Línea 1: ________________
Línea 2: ________________
Línea 3: ________________
Línea 4: ________________
```

### A2. Conversión de Tipos (5 puntos)

Completa el código para que funcione correctamente:

```python
# Datos de entrada como strings
edad_str = "25"
altura_str = "1.75"
nombre = "Ana"

# Convierte a los tipos apropiados y calcula
edad = __________(edad_str)
altura = __________(altura_str)

# Calcula años que faltan para cumplir 30
años_faltantes = __________ - edad

print(f"{nombre} tiene {edad} años y mide {altura}m")
print(f"Le faltan {años_faltantes} años para cumplir 30")
```

### A3. Creación de Variables (5 puntos)

Crea variables apropiadas para almacenar la siguiente información de un producto:

- Nombre del producto: "Laptop Gamer"
- Precio: 15999.99
- En stock: True
- Categorías: ["Electrónicos", "Computadoras", "Gaming"]
- Especificaciones: RAM=16, Almacenamiento=512, Marca="TechBrand"

**Tu código:**

```python
# Escribe tu código aquí


```

---

## 🧮 SECCIÓN B: Operadores y Cálculos (15 puntos)

### B1. Calculadora de Descuentos (6 puntos)

Completa la función que calcula el precio final con descuento:

```python
def calcular_precio_final(precio_original, descuento_porcentaje, impuesto_porcentaje):
    """
    Calcula el precio final aplicando descuento e impuesto
    El descuento se aplica primero, luego el impuesto
    """
    # Tu código aquí
    precio_con_descuento = precio_original - (precio_original * _______ / 100)
    precio_final = precio_con_descuento + (precio_con_descuento * _______ / 100)

    return precio_final

# Prueba: precio=1000, descuento=20%, impuesto=16%
# Resultado esperado: 928.0
resultado = calcular_precio_final(1000, 20, 16)
print(resultado)
```

### B2. Operadores Lógicos (4 puntos)

¿Qué imprimirá cada expresión? Marca Verdadero (V) o Falso (F):

```python
a = 10
b = 5
c = 0

print(a > b and b > c)          # _____
print(a == 10 or b == 10)       # _____
print(not (a < b))              # _____
print(a > 5 and b < 3 or c == 0) # _____
```

### B3. Operaciones con Strings (5 puntos)

Completa el código para manipular texto:

```python
frase = "  Python es GENIAL para IA  "

# Limpia espacios y convierte a minúsculas
frase_limpia = frase.______().______()

# Reemplaza "genial" por "excelente"
frase_final = frase_limpia.______("genial", "excelente")

# Separa las palabras
palabras = frase_final.______(________)

print(f"Número de palabras: {len(palabras)}")
print(f"Primera palabra: {palabras[0]}")
print(f"Última palabra: {palabras[-1]}")
```

---

## 🤔 SECCIÓN C: Condicionales y Lógica (20 puntos)

### C1. Sistema de Calificaciones (8 puntos)

Escribe una función que determine la letra de calificación:

```python
def obtener_letra_calificacion(promedio):
    """
    Convierte promedio numérico a letra:
    90-100: A, 80-89: B, 70-79: C, 60-69: D, <60: F
    """
    # Tu código aquí




# Pruebas
print(obtener_letra_calificacion(95))  # Debe imprimir: A
print(obtener_letra_calificacion(73))  # Debe imprimir: C
print(obtener_letra_calificacion(45))  # Debe imprimir: F
```

### C2. Validador de Edad (6 puntos)

Completa la función que valida y categoriza edades:

```python
def categorizar_edad(edad):
    """
    Categoriza por edad:
    0-12: Niño, 13-17: Adolescente, 18-64: Adulto, 65+: Adulto Mayor
    Maneja casos inválidos (edad negativa o mayor a 120)
    """
    if _______:
        return "Edad inválida"
    elif _______:
        return "Niño"
    elif _______:
        return "Adolescente"
    elif _______:
        return "Adulto"
    else:
        return "Adulto Mayor"
```

### C3. Analizador de Password (6 puntos)

Escribe código que determine si una contraseña es segura:

```python
def es_password_segura(password):
    """
    Una contraseña es segura si:
    - Tiene al menos 8 caracteres
    - Contiene al menos una mayúscula
    - Contiene al menos una minúscula
    - Contiene al menos un número
    """
    # Tu código aquí





# Pruebas
print(es_password_segura("MiPassword123"))  # True
print(es_password_segura("password"))       # False
print(es_password_segura("PASSWORD123"))    # False
```

---

## 🔄 SECCIÓN D: Bucles y Repetición (15 puntos)

### D1. Contador de Vocales (8 puntos)

Escribe una función que cuente vocales en un texto:

```python
def contar_vocales(texto):
    """
    Cuenta el número de vocales (a,e,i,o,u) en un texto
    Considera mayúsculas y minúsculas
    """
    vocales = "aeiouAEIOU"
    contador = 0

    # Tu código aquí (usa un bucle for)



    return contador

# Prueba
resultado = contar_vocales("Hola Mundo")
print(f"Vocales encontradas: {resultado}")  # Debe ser: 4
```

### D2. Generador de Tabla de Multiplicar (7 puntos)

Completa el código que genera tablas de multiplicar:

```python
def generar_tabla_multiplicar(numero, hasta=10):
    """
    Genera la tabla de multiplicar del número dado
    Retorna una lista con los resultados
    """
    tabla = []

    # Tu código aquí (usa range y un bucle)
    for i in range(_____, _____ + 1):
        resultado = _____ * _____
        tabla.append(resultado)

    return tabla

# Prueba
tabla_5 = generar_tabla_multiplicar(5)
print(tabla_5)  # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
```

---

## 📋 SECCIÓN E: Listas y Manipulación (15 puntos)

### E1. Analizador de Números (8 puntos)

Escribe una función que analice una lista de números:

```python
def analizar_numeros(numeros):
    """
    Analiza una lista de números y retorna un diccionario con:
    - 'total': suma de todos los números
    - 'promedio': promedio de los números
    - 'mayor': el número más grande
    - 'menor': el número más pequeño
    - 'pares': lista de números pares
    """
    if not numeros:  # Lista vacía
        return None

    # Tu código aquí
    resultado = {
        'total': ____________,
        'promedio': ____________,
        'mayor': ____________,
        'menor': ____________,
        'pares': ____________
    }

    return resultado

# Prueba
datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
analisis = analizar_numeros(datos)
print(analisis)
```

### E2. Filtro de Lista (7 puntos)

Completa las funciones de filtrado:

```python
estudiantes = ["Ana García", "Luis López", "María Martínez", "Carlos Castro", "Ana Ruiz"]

def filtrar_por_inicial(lista, inicial):
    """Retorna elementos que empiecen con la inicial dada"""
    # Tu código aquí



def filtrar_por_longitud(lista, min_longitud):
    """Retorna elementos con longitud mínima especificada"""
    # Tu código aquí



# Pruebas
print(filtrar_por_inicial(estudiantes, "A"))    # ["Ana García", "Ana Ruiz"]
print(filtrar_por_longitud(estudiantes, 12))    # Nombres con 12+ caracteres
```

---

## 🗂️ SECCIÓN F: Diccionarios (10 puntos)

### F1. Gestor de Inventario (5 puntos)

Completa las operaciones con diccionarios:

```python
inventario = {
    "manzanas": {"cantidad": 50, "precio": 2.5},
    "peras": {"cantidad": 30, "precio": 3.0},
    "naranjas": {"cantidad": 25, "precio": 2.0}
}

def valor_total_inventario(inventario):
    """Calcula el valor total del inventario"""
    total = 0
    # Tu código aquí
    for producto, datos in inventario.items():
        ___________________

    return total

def producto_mas_caro(inventario):
    """Encuentra el producto con mayor precio unitario"""
    # Tu código aquí



print(f"Valor total: ${valor_total_inventario(inventario)}")
print(f"Producto más caro: {producto_mas_caro(inventario)}")
```

### F2. Contador de Palabras (5 puntos)

Escribe una función que cuente palabras en un texto:

```python
def contar_palabras(texto):
    """
    Cuenta la frecuencia de cada palabra en el texto
    Retorna un diccionario con palabra: frecuencia
    """
    # Tu código aquí




# Prueba
frase = "python es genial python es fácil python es poderoso"
resultado = contar_palabras(frase)
print(resultado)  # {'python': 3, 'es': 3, 'genial': 1, 'fácil': 1, 'poderoso': 1}
```

---

## ⚙️ SECCIÓN G: Funciones (10 puntos)

### G1. Mini Calculadora con Funciones (10 puntos)

Crea un sistema de calculadora modular:

```python
def sumar(a, b):
    """Suma dos números"""
    # Tu código aquí


def restar(a, b):
    """Resta dos números"""
    # Tu código aquí


def multiplicar(a, b):
    """Multiplica dos números"""
    # Tu código aquí


def dividir(a, b):
    """Divide dos números (maneja división por cero)"""
    # Tu código aquí



def calculadora(operacion, num1, num2):
    """
    Función principal que usa las funciones auxiliares
    operacion: "suma", "resta", "multiplicacion", "division"
    """
    if operacion == "suma":
        return sumar(num1, num2)
    elif operacion == "resta":
        return restar(num1, num2)
    elif operacion == "multiplicacion":
        return multiplicar(num1, num2)
    elif operacion == "division":
        return dividir(num1, num2)
    else:
        return "Operación no válida"

# Pruebas
print(calculadora("suma", 10, 5))          # 15
print(calculadora("division", 10, 0))      # "Error: División por cero"
print(calculadora("multiplicacion", 4, 7)) # 28
```

---

## 🎯 Instrucciones de Entrega

### 📋 Formato de Entrega

1. **Archivo**: Guarda tu test como `test_fase00_[tu_nombre].py`
2. **Comentarios**: Incluye comentarios explicando tu lógica
3. **Pruebas**: Verifica que tu código funcione correctamente
4. **Organización**: Mantén el orden de las secciones

### ✅ Criterios de Evaluación

| Aspecto           | Excelente (100%)               | Bueno (80%)                  | Regular (60%)                | Insuficiente (40%)   |
| ----------------- | ------------------------------ | ---------------------------- | ---------------------------- | -------------------- |
| **Funcionalidad** | Código funciona perfectamente  | Funciona con errores menores | Funciona parcialmente        | No funciona          |
| **Sintaxis**      | Sin errores de sintaxis        | 1-2 errores menores          | Varios errores               | Muchos errores       |
| **Lógica**        | Lógica correcta y eficiente    | Lógica correcta              | Lógica parcialmente correcta | Lógica incorrecta    |
| **Estilo**        | Código limpio y bien comentado | Código ordenado              | Código básico                | Código desorganizado |

### 🕒 Tiempo Sugerido por Sección

- **Sección A**: 15 minutos
- **Sección B**: 15 minutos
- **Sección C**: 25 minutos
- **Sección D**: 20 minutos
- **Sección E**: 20 minutos
- **Sección F**: 15 minutos
- **Sección G**: 15 minutos
- **Revisión**: 15 minutos

---

## 🎉 ¡Buena Suerte

Recuerda:

- Lee cada pregunta cuidadosamente
- Prueba tu código antes de finalizar
- Usa nombres de variables descriptivos
- Incluye comentarios cuando sea necesario
- ¡Confía en lo que has aprendido!

**Al completar este test exitosamente, estarás listo para avanzar a la Fase 01: Fundamentos de IA** 🚀
