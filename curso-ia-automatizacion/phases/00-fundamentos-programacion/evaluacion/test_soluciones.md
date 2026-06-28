# 🔑 Soluciones del Test - Fase 00: Fundamentos de Programación

## 📋 Información de las Soluciones

- **Archivo**: Soluciones completas del test de evaluación
- **Uso**: Para instructores y auto-evaluación de estudiantes
- **Puntaje total**: 100 puntos distribuidos en 7 secciones

---

## 📝 SECCIÓN A: Variables y Tipos de Datos (15 puntos)

### A1. Análisis de Variables (5 puntos)

**Respuestas correctas:**

```
Línea 1: <class 'str'>
Línea 2: 6
Línea 3: 2027.12
Línea 4: True
```

**Explicación:**

- `type(nombre)` retorna el tipo de dato string
- `len(nombre)` cuenta los caracteres en "Python" = 6
- `version + año` suma 3.12 + 2024 = 2027.12
- `es_moderno and version > 3` evalúa True and True = True

### A2. Conversión de Tipos (5 puntos)

**Código completo:**

```python
# Datos de entrada como strings
edad_str = "25"
altura_str = "1.75"
nombre = "Ana"

# Convierte a los tipos apropiados y calcula
edad = int(edad_str)
altura = float(altura_str)

# Calcula años que faltan para cumplir 30
años_faltantes = 30 - edad

print(f"{nombre} tiene {edad} años y mide {altura}m")
print(f"Le faltan {años_faltantes} años para cumplir 30")
```

### A3. Creación de Variables (5 puntos)

**Código completo:**

```python
# Variables para información del producto
nombre_producto = "Laptop Gamer"
precio = 15999.99
en_stock = True
categorias = ["Electrónicos", "Computadoras", "Gaming"]
especificaciones = {
    "RAM": 16,
    "Almacenamiento": 512,
    "Marca": "TechBrand"
}
```

---

## 🧮 SECCIÓN B: Operadores y Cálculos (15 puntos)

### B1. Calculadora de Descuentos (6 puntos)

**Código completo:**

```python
def calcular_precio_final(precio_original, descuento_porcentaje, impuesto_porcentaje):
    """
    Calcula el precio final aplicando descuento e impuesto
    El descuento se aplica primero, luego el impuesto
    """
    precio_con_descuento = precio_original - (precio_original * descuento_porcentaje / 100)
    precio_final = precio_con_descuento + (precio_con_descuento * impuesto_porcentaje / 100)

    return precio_final

# Prueba: precio=1000, descuento=20%, impuesto=16%
# Resultado esperado: 928.0
resultado = calcular_precio_final(1000, 20, 16)
print(resultado)  # 928.0
```

### B2. Operadores Lógicos (4 puntos)

**Respuestas correctas:**

```python
a = 10
b = 5
c = 0

print(a > b and b > c)          # V (True)
print(a == 10 or b == 10)       # V (True)
print(not (a < b))              # V (True)
print(a > 5 and b < 3 or c == 0) # V (True)
```

### B3. Operaciones con Strings (5 puntos)

**Código completo:**

```python
frase = "  Python es GENIAL para IA  "

# Limpia espacios y convierte a minúsculas
frase_limpia = frase.strip().lower()

# Reemplaza "genial" por "excelente"
frase_final = frase_limpia.replace("genial", "excelente")

# Separa las palabras
palabras = frase_final.split(" ")

print(f"Número de palabras: {len(palabras)}")
print(f"Primera palabra: {palabras[0]}")
print(f"Última palabra: {palabras[-1]}")
```

---

## 🤔 SECCIÓN C: Condicionales y Lógica (20 puntos)

### C1. Sistema de Calificaciones (8 puntos)

**Código completo:**

```python
def obtener_letra_calificacion(promedio):
    """
    Convierte promedio numérico a letra:
    90-100: A, 80-89: B, 70-79: C, 60-69: D, <60: F
    """
    if promedio >= 90:
        return "A"
    elif promedio >= 80:
        return "B"
    elif promedio >= 70:
        return "C"
    elif promedio >= 60:
        return "D"
    else:
        return "F"

# Pruebas
print(obtener_letra_calificacion(95))  # A
print(obtener_letra_calificacion(73))  # C
print(obtener_letra_calificacion(45))  # F
```

### C2. Validador de Edad (6 puntos)

**Código completo:**

```python
def categorizar_edad(edad):
    """
    Categoriza por edad:
    0-12: Niño, 13-17: Adolescente, 18-64: Adulto, 65+: Adulto Mayor
    Maneja casos inválidos (edad negativa o mayor a 120)
    """
    if edad < 0 or edad > 120:
        return "Edad inválida"
    elif edad <= 12:
        return "Niño"
    elif edad <= 17:
        return "Adolescente"
    elif edad <= 64:
        return "Adulto"
    else:
        return "Adulto Mayor"
```

### C3. Analizador de Password (6 puntos)

**Código completo:**

```python
def es_password_segura(password):
    """
    Una contraseña es segura si:
    - Tiene al menos 8 caracteres
    - Contiene al menos una mayúscula
    - Contiene al menos una minúscula
    - Contiene al menos un número
    """
    if len(password) < 8:
        return False

    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False

    for caracter in password:
        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True

    return tiene_mayuscula and tiene_minuscula and tiene_numero

# Pruebas
print(es_password_segura("MiPassword123"))  # True
print(es_password_segura("password"))       # False
print(es_password_segura("PASSWORD123"))    # False
```

---

## 🔄 SECCIÓN D: Bucles y Repetición (15 puntos)

### D1. Contador de Vocales (8 puntos)

**Código completo:**

```python
def contar_vocales(texto):
    """
    Cuenta el número de vocales (a,e,i,o,u) en un texto
    Considera mayúsculas y minúsculas
    """
    vocales = "aeiouAEIOU"
    contador = 0

    for caracter in texto:
        if caracter in vocales:
            contador += 1

    return contador

# Prueba
resultado = contar_vocales("Hola Mundo")
print(f"Vocales encontradas: {resultado}")  # 4
```

### D2. Generador de Tabla de Multiplicar (7 puntos)

**Código completo:**

```python
def generar_tabla_multiplicar(numero, hasta=10):
    """
    Genera la tabla de multiplicar del número dado
    Retorna una lista con los resultados
    """
    tabla = []

    for i in range(1, hasta + 1):
        resultado = numero * i
        tabla.append(resultado)

    return tabla

# Prueba
tabla_5 = generar_tabla_multiplicar(5)
print(tabla_5)  # [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
```

---

## 📋 SECCIÓN E: Listas y Manipulación (15 puntos)

### E1. Analizador de Números (8 puntos)

**Código completo:**

```python
def analizar_numeros(numeros):
    """
    Analiza una lista de números y retorna un diccionario con estadísticas
    """
    if not numeros:  # Lista vacía
        return None

    pares = []
    for num in numeros:
        if num % 2 == 0:
            pares.append(num)

    resultado = {
        'total': sum(numeros),
        'promedio': sum(numeros) / len(numeros),
        'mayor': max(numeros),
        'menor': min(numeros),
        'pares': pares
    }

    return resultado

# Prueba
datos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
analisis = analizar_numeros(datos)
print(analisis)
```

### E2. Filtro de Lista (7 puntos)

**Código completo:**

```python
estudiantes = ["Ana García", "Luis López", "María Martínez", "Carlos Castro", "Ana Ruiz"]

def filtrar_por_inicial(lista, inicial):
    """Retorna elementos que empiecen con la inicial dada"""
    resultado = []
    for elemento in lista:
        if elemento.startswith(inicial):
            resultado.append(elemento)
    return resultado

def filtrar_por_longitud(lista, min_longitud):
    """Retorna elementos con longitud mínima especificada"""
    resultado = []
    for elemento in lista:
        if len(elemento) >= min_longitud:
            resultado.append(elemento)
    return resultado

# Pruebas
print(filtrar_por_inicial(estudiantes, "A"))    # ["Ana García", "Ana Ruiz"]
print(filtrar_por_longitud(estudiantes, 12))    # ["María Martínez", "Carlos Castro"]
```

---

## 🗂️ SECCIÓN F: Diccionarios (10 puntos)

### F1. Gestor de Inventario (5 puntos)

**Código completo:**

```python
inventario = {
    "manzanas": {"cantidad": 50, "precio": 2.5},
    "peras": {"cantidad": 30, "precio": 3.0},
    "naranjas": {"cantidad": 25, "precio": 2.0}
}

def valor_total_inventario(inventario):
    """Calcula el valor total del inventario"""
    total = 0
    for producto, datos in inventario.items():
        total += datos["cantidad"] * datos["precio"]

    return total

def producto_mas_caro(inventario):
    """Encuentra el producto con mayor precio unitario"""
    precio_maximo = 0
    producto_caro = ""

    for producto, datos in inventario.items():
        if datos["precio"] > precio_maximo:
            precio_maximo = datos["precio"]
            producto_caro = producto

    return producto_caro

print(f"Valor total: ${valor_total_inventario(inventario)}")  # $265.0
print(f"Producto más caro: {producto_mas_caro(inventario)}")  # peras
```

### F2. Contador de Palabras (5 puntos)

**Código completo:**

```python
def contar_palabras(texto):
    """
    Cuenta la frecuencia de cada palabra en el texto
    Retorna un diccionario con palabra: frecuencia
    """
    palabras = texto.split()
    conteo = {}

    for palabra in palabras:
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1

    return conteo

# Prueba
frase = "python es genial python es fácil python es poderoso"
resultado = contar_palabras(frase)
print(resultado)  # {'python': 3, 'es': 3, 'genial': 1, 'fácil': 1, 'poderoso': 1}
```

---

## ⚙️ SECCIÓN G: Funciones (10 puntos)

### G1. Mini Calculadora con Funciones (10 puntos)

**Código completo:**

```python
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

## 📊 Rúbrica de Evaluación Detallada

### Distribución de Puntos por Criterio

| Sección | Funcionalidad | Sintaxis | Lógica | Estilo | Total  |
| ------- | ------------- | -------- | ------ | ------ | ------ |
| A       | 40%           | 30%      | 20%    | 10%    | 15 pts |
| B       | 50%           | 25%      | 20%    | 5%     | 15 pts |
| C       | 60%           | 20%      | 15%    | 5%     | 20 pts |
| D       | 55%           | 25%      | 15%    | 5%     | 15 pts |
| E       | 60%           | 20%      | 15%    | 5%     | 15 pts |
| F       | 50%           | 25%      | 20%    | 5%     | 10 pts |
| G       | 70%           | 15%      | 10%    | 5%     | 10 pts |

### Comentarios de Evaluación Típicos

#### ✅ **Excelente (90-100%)**

- "Solución completa y eficiente"
- "Manejo correcto de casos edge"
- "Código limpio y bien documentado"
- "Demuestra dominio completo del concepto"

#### ✅ **Bueno (70-89%)**

- "Funciona correctamente con errores menores"
- "Lógica correcta, puede mejorar eficiencia"
- "Sintaxis apropiada con pequeños detalles"

#### ⚠️ **Regular (50-69%)**

- "Funciona parcialmente"
- "Concepto entendido pero implementación incompleta"
- "Necesita revisar algunos fundamentos"

#### ❌ **Insuficiente (<50%)**

- "No funciona o no demuestra comprensión"
- "Errores fundamentales de concepto"
- "Requiere estudio adicional antes de continuar"

---

## 🎯 Recomendaciones para Instructores

### ⏰ **Tiempo de Corrección Estimado**

- **Por estudiante**: 20-30 minutos
- **Grupos de 20**: 8-10 horas
- **Feedback detallado**: +15 minutos por estudiante

### 📋 **Checklist de Revisión**

Para cada sección, verificar:

- [ ] **Funcionalidad**: ¿El código funciona como se esperaba?
- [ ] **Sintaxis**: ¿Hay errores de Python que impidan la ejecución?
- [ ] **Lógica**: ¿El enfoque es correcto y eficiente?
- [ ] **Casos edge**: ¿Maneja situaciones especiales?
- [ ] **Estilo**: ¿El código es legible y bien organizado?

### 🔄 **Proceso de Retroalimentación**

1. **Corrección automática**: Ejecutar código y verificar outputs
2. **Revisión manual**: Evaluar lógica y estilo
3. **Feedback constructivo**: Comentarios específicos para mejora
4. **Sugerencias**: Recursos adicionales si es necesario

---

## 📈 Análisis de Resultados Esperados

### 🎯 **Distribución Típica de Calificaciones**

- **90-100 puntos**: 20% de estudiantes (Excelente)
- **80-89 puntos**: 35% de estudiantes (Bueno)
- **70-79 puntos**: 30% de estudiantes (Satisfactorio)
- **60-69 puntos**: 10% de estudiantes (Necesita refuerzo)
- **<60 puntos**: 5% de estudiantes (Requiere repetir)

### 📊 **Secciones con Mayor Dificultad (típicamente)**

1. **Sección C (Condicionales)**: Lógica compleja
2. **Sección G (Funciones)**: Modularización
3. **Sección E (Listas)**: Manipulación avanzada

### 💡 **Errores Comunes por Sección**

- **Sección A**: Confusión entre tipos de datos
- **Sección B**: Orden de operaciones incorrecto
- **Sección C**: Condiciones mal estructuradas
- **Sección D**: Lógica de bucles incorrecta
- **Sección E**: Indexación y métodos de listas
- **Sección F**: Sintaxis de diccionarios
- **Sección G**: Scope y parámetros de funciones

---

**Esta guía de soluciones proporciona todas las respuestas correctas y criterios de evaluación para una corrección justa y consistente del test de Fase 00.**
