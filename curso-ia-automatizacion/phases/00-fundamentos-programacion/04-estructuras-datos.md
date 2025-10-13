# 04. Estructuras de Datos

## 🎯 Objetivos de Aprendizaje

Al finalizar esta unidad, podrás:

- Trabajar con listas para almacenar múltiples valores
- Utilizar diccionarios para organizar datos con claves
- Manejar tuplas para datos inmutables
- Aplicar conjuntos para eliminar duplicados
- Elegir la estructura de datos adecuada para cada situación

## 📚 ¿Qué son las Estructuras de Datos?

Las **estructuras de datos** son formas de organizar y almacenar información para acceder y modificarla de manera eficiente.

Imagina que tienes que organizar tu biblioteca:
- **Lista**: Libros en orden de llegada
- **Diccionario**: Libros organizados por categoría
- **Conjunto**: Lista única de autores (sin repetir)
- **Tupla**: Información fija del libro (ISBN, año publicación)

## 📋 Listas (Lists)

Las listas son **colecciones ordenadas y modificables** que pueden contener elementos de cualquier tipo.

### Crear y Acceder a Listas

```python
# Crear listas
frutas = ["manzana", "banana", "naranja"]
numeros = [1, 2, 3, 4, 5]
mixta = ["Pedro", 25, True, 3.14]
vacia = []

# Acceder por índice (empieza en 0)
print(frutas[0])     # "manzana"
print(frutas[1])     # "banana"
print(frutas[-1])    # "naranja" (último elemento)
print(frutas[-2])    # "banana" (penúltimo)

# Slicing (rebanadas)
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(numeros[2:5])    # [2, 3, 4] (desde índice 2 hasta 4)
print(numeros[:3])     # [0, 1, 2] (desde inicio hasta índice 2)
print(numeros[7:])     # [7, 8, 9] (desde índice 7 hasta final)
print(numeros[::2])    # [0, 2, 4, 6, 8] (cada 2 elementos)
```

### Métodos Útiles de Listas

```python
# Lista inicial
colores = ["rojo", "verde", "azul"]

# Agregar elementos
colores.append("amarillo")              # Al final
print(colores)  # ["rojo", "verde", "azul", "amarillo"]

colores.insert(1, "violeta")            # En posición específica
print(colores)  # ["rojo", "violeta", "verde", "azul", "amarillo"]

# Remover elementos
colores.remove("verde")                 # Por valor
print(colores)  # ["rojo", "violeta", "azul", "amarillo"]

ultimo = colores.pop()                  # Remueve y devuelve último
print(f"Removido: {ultimo}")           # "amarillo"
print(colores)  # ["rojo", "violeta", "azul"]

segundo = colores.pop(1)                # Remueve por índice
print(f"Removido: {segundo}")          # "violeta"

# Información de la lista
print(f"Longitud: {len(colores)}")     # 2
print(f"¿Contiene 'rojo'?: {'rojo' in colores}")  # True

# Ordenamiento
numeros = [3, 1, 4, 1, 5, 9, 2, 6]
numeros.sort()                          # Modifica la lista original
print(numeros)  # [1, 1, 2, 3, 4, 5, 6, 9]

palabras = ["python", "java", "c++", "javascript"]
palabras_ordenadas = sorted(palabras)   # Crea nueva lista ordenada
print(palabras_ordenadas)  # ['c++', 'java', 'javascript', 'python']
```

### Ejemplo Práctico: Lista de Tareas

```python
# Sistema simple de lista de tareas
def gestor_tareas():
    tareas = []
    
    while True:
        print("\n=== GESTOR DE TAREAS ===")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Completar tarea")
        print("4. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            if tareas:
                print("\nTus tareas:")
                for i, tarea in enumerate(tareas, 1):
                    print(f"{i}. {tarea}")
            else:
                print("No tienes tareas pendientes")
        
        elif opcion == "2":
            nueva_tarea = input("Escribe la nueva tarea: ")
            tareas.append(nueva_tarea)
            print(f"Tarea '{nueva_tarea}' agregada")
        
        elif opcion == "3":
            if tareas:
                for i, tarea in enumerate(tareas, 1):
                    print(f"{i}. {tarea}")
                try:
                    indice = int(input("¿Qué tarea completaste? (número): ")) - 1
                    tarea_completada = tareas.pop(indice)
                    print(f"¡Tarea '{tarea_completada}' completada!")
                except (ValueError, IndexError):
                    print("Número inválido")
            else:
                print("No tienes tareas pendientes")
        
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida")

# Ejecutar (descomenta para probar)
# gestor_tareas()
```

## 📖 Diccionarios (Dictionaries)

Los diccionarios almacenan datos en pares **clave-valor**. Son perfectos para organizar información relacionada.

### Crear y Usar Diccionarios

```python
# Crear diccionarios
estudiante = {
    "nombre": "María García",
    "edad": 22,
    "carrera": "Ingeniería en Sistemas",
    "semestre": 6,
    "activo": True
}

# Acceder a valores
print(estudiante["nombre"])     # "María García"
print(estudiante["edad"])       # 22

# Método get() (más seguro)
print(estudiante.get("nombre"))              # "María García"
print(estudiante.get("telefono", "No tiene")) # "No tiene" (valor por defecto)

# Modificar valores
estudiante["edad"] = 23
estudiante["telefono"] = "555-1234"  # Agregar nueva clave

print(estudiante)
```

### Métodos Útiles de Diccionarios

```python
# Diccionario de ejemplo
inventario = {
    "manzanas": 10,
    "bananas": 15,
    "naranjas": 8,
    "uvas": 20
}

# Obtener claves, valores y elementos
print(inventario.keys())    # dict_keys(['manzanas', 'bananas', 'naranjas', 'uvas'])
print(inventario.values())  # dict_values([10, 15, 8, 20])
print(inventario.items())   # dict_items([('manzanas', 10), ('bananas', 15), ...])

# Iterar sobre diccionarios
print("Inventario actual:")
for fruta, cantidad in inventario.items():
    print(f"{fruta}: {cantidad} unidades")

# Verificar existencia
if "manzanas" in inventario:
    print("Tenemos manzanas en stock")

# Remover elementos
del inventario["uvas"]              # Eliminar clave específica
ultima_fruta = inventario.pop("naranjas", 0)  # Remover y obtener valor
print(f"Removimos {ultima_fruta} naranjas")

# Actualizar diccionario
nuevos_productos = {"peras": 12, "kiwis": 5}
inventario.update(nuevos_productos)
print(inventario)
```

### Ejemplo Práctico: Agenda de Contactos

```python
def agenda_contactos():
    """Sistema de agenda de contactos con diccionarios."""
    contactos = {}
    
    while True:
        print("\n=== AGENDA DE CONTACTOS ===")
        print("1. Ver todos los contactos")
        print("2. Buscar contacto")
        print("3. Agregar contacto")
        print("4. Actualizar contacto")
        print("5. Eliminar contacto")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            if contactos:
                print("\n--- TODOS LOS CONTACTOS ---")
                for nombre, info in contactos.items():
                    print(f"Nombre: {nombre}")
                    print(f"Teléfono: {info['telefono']}")
                    print(f"Email: {info['email']}")
                    print("-" * 30)
            else:
                print("No hay contactos guardados")
        
        elif opcion == "2":
            nombre = input("Nombre a buscar: ").title()
            if nombre in contactos:
                info = contactos[nombre]
                print(f"\n--- CONTACTO ENCONTRADO ---")
                print(f"Nombre: {nombre}")
                print(f"Teléfono: {info['telefono']}")
                print(f"Email: {info['email']}")
            else:
                print("Contacto no encontrado")
        
        elif opcion == "3":
            nombre = input("Nombre: ").title()
            telefono = input("Teléfono: ")
            email = input("Email: ")
            
            contactos[nombre] = {
                "telefono": telefono,
                "email": email
            }
            print(f"Contacto {nombre} agregado exitosamente")
        
        elif opcion == "4":
            nombre = input("Nombre del contacto a actualizar: ").title()
            if nombre in contactos:
                print(f"Datos actuales de {nombre}:")
                print(f"Teléfono: {contactos[nombre]['telefono']}")
                print(f"Email: {contactos[nombre]['email']}")
                
                nuevo_telefono = input("Nuevo teléfono (Enter para mantener actual): ")
                nuevo_email = input("Nuevo email (Enter para mantener actual): ")
                
                if nuevo_telefono:
                    contactos[nombre]["telefono"] = nuevo_telefono
                if nuevo_email:
                    contactos[nombre]["email"] = nuevo_email
                
                print(f"Contacto {nombre} actualizado")
            else:
                print("Contacto no encontrado")
        
        elif opcion == "5":
            nombre = input("Nombre del contacto a eliminar: ").title()
            if nombre in contactos:
                confirmacion = input(f"¿Estás seguro de eliminar a {nombre}? (s/n): ")
                if confirmacion.lower() == "s":
                    del contactos[nombre]
                    print(f"Contacto {nombre} eliminado")
            else:
                print("Contacto no encontrado")
        
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        
        else:
            print("Opción inválida")

# Ejecutar (descomenta para probar)
# agenda_contactos()
```

## 🔒 Tuplas (Tuples)

Las tuplas son **colecciones ordenadas e inmutables**. Una vez creadas, no se pueden modificar.

### Crear y Usar Tuplas

```python
# Crear tuplas
coordenadas = (10, 20)
colores_rgb = (255, 128, 0)
informacion_persona = ("Juan", "Pérez", 30, "Ingeniero")

# Tupla de un elemento (nota la coma)
un_elemento = (42,)

# Acceder elementos (igual que listas)
print(coordenadas[0])    # 10
print(colores_rgb[-1])   # 0 (último elemento)

# Desempaquetado de tuplas
x, y = coordenadas
print(f"X: {x}, Y: {y}")  # X: 10, Y: 20

nombre, apellido, edad, profesion = informacion_persona
print(f"{nombre} {apellido} es {profesion} y tiene {edad} años")

# Intercambio de variables usando tuplas
a = 5
b = 10
a, b = b, a  # Intercambio elegante
print(f"a: {a}, b: {b}")  # a: 10, b: 5
```

### Cuándo Usar Tuplas

```python
# Coordenadas geográficas (no cambian)
ubicaciones = [
    ("Madrid", 40.4168, -3.7038),
    ("Barcelona", 41.3851, 2.1734),
    ("Valencia", 39.4699, -0.3763)
]

# Función que retorna múltiples valores
def calcular_estadisticas(numeros):
    """Retorna promedio, mínimo y máximo."""
    promedio = sum(numeros) / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    
    return promedio, minimo, maximo  # Retorna tupla

# Uso
datos = [10, 20, 30, 40, 50]
prom, min_val, max_val = calcular_estadisticas(datos)
print(f"Promedio: {prom}, Mín: {min_val}, Máx: {max_val}")
```

## 🎯 Conjuntos (Sets)

Los conjuntos almacenan elementos **únicos y no ordenados**. Perfectos para eliminar duplicados.

### Crear y Usar Conjuntos

```python
# Crear conjuntos
frutas = {"manzana", "banana", "naranja"}
numeros = {1, 2, 3, 4, 5}
mixto = {1, "hola", 3.14, True}

# Conjunto vacío
vacio = set()  # No usar {} porque crea diccionario vacío

# Eliminar duplicados de una lista
lista_con_duplicados = [1, 2, 2, 3, 3, 3, 4, 5, 5]
sin_duplicados = list(set(lista_con_duplicados))
print(sin_duplicados)  # [1, 2, 3, 4, 5]

# Operaciones de conjuntos
frutas.add("kiwi")           # Agregar elemento
frutas.remove("banana")      # Remover elemento (error si no existe)
frutas.discard("pera")       # Remover elemento (no error si no existe)

print("manzana" in frutas)   # True
print(len(frutas))           # Cantidad de elementos
```

### Operaciones Matemáticas con Conjuntos

```python
# Conjuntos de ejemplo
estudiantes_matematicas = {"Ana", "Carlos", "Elena", "David"}
estudiantes_fisica = {"Carlos", "Elena", "Fernando", "Gabriela"}

# Unión (estudiantes en cualquier materia)
todos_estudiantes = estudiantes_matematicas | estudiantes_fisica
print(f"Todos los estudiantes: {todos_estudiantes}")

# Intersección (estudiantes en ambas materias)
en_ambas = estudiantes_matematicas & estudiantes_fisica
print(f"En ambas materias: {en_ambas}")

# Diferencia (solo en matemáticas)
solo_matematicas = estudiantes_matematicas - estudiantes_fisica
print(f"Solo en matemáticas: {solo_matematicas}")

# Diferencia simétrica (en una materia pero no en ambas)
en_una_sola = estudiantes_matematicas ^ estudiantes_fisica
print(f"En una sola materia: {en_una_sola}")
```

## 🎪 Ejemplo Integrador: Sistema de Biblioteca

```python
def sistema_biblioteca():
    """Sistema de gestión de biblioteca usando todas las estructuras de datos."""
    
    # Diccionario principal de libros
    biblioteca = {}
    
    # Conjunto de géneros disponibles
    generos_disponibles = {"ficción", "no ficción", "ciencia", "historia", "biografía", "tecnología"}
    
    # Lista de usuarios activos
    usuarios_activos = []
    
    def agregar_libro():
        isbn = input("ISBN del libro: ")
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input(f"Género {generos_disponibles}: ").lower()
        
        if genero not in generos_disponibles:
            print("Género no válido")
            return
        
        # Información como tupla (inmutable)
        info_libro = (titulo, autor, genero, True)  # True = disponible
        biblioteca[isbn] = info_libro
        print(f"Libro '{titulo}' agregado exitosamente")
    
    def buscar_libro():
        termino = input("Buscar por título o autor: ").lower()
        encontrados = []
        
        for isbn, (titulo, autor, genero, disponible) in biblioteca.items():
            if termino in titulo.lower() or termino in autor.lower():
                estado = "Disponible" if disponible else "Prestado"
                encontrados.append(f"{titulo} - {autor} ({genero}) - {estado}")
        
        if encontrados:
            print("\nLibros encontrados:")
            for libro in encontrados:
                print(f"- {libro}")
        else:
            print("No se encontraron libros")
    
    def prestar_libro():
        isbn = input("ISBN del libro a prestar: ")
        usuario = input("Nombre del usuario: ")
        
        if isbn in biblioteca:
            titulo, autor, genero, disponible = biblioteca[isbn]
            if disponible:
                # Actualizar disponibilidad
                biblioteca[isbn] = (titulo, autor, genero, False)
                # Agregar usuario a lista activa si no está
                if usuario not in usuarios_activos:
                    usuarios_activos.append(usuario)
                print(f"Libro '{titulo}' prestado a {usuario}")
            else:
                print("El libro no está disponible")
        else:
            print("Libro no encontrado")
    
    def devolver_libro():
        isbn = input("ISBN del libro a devolver: ")
        
        if isbn in biblioteca:
            titulo, autor, genero, disponible = biblioteca[isbn]
            if not disponible:
                biblioteca[isbn] = (titulo, autor, genero, True)
                print(f"Libro '{titulo}' devuelto exitosamente")
            else:
                print("Este libro no estaba prestado")
        else:
            print("Libro no encontrado")
    
    def mostrar_estadisticas():
        if not biblioteca:
            print("No hay libros en la biblioteca")
            return
        
        # Contadores usando diccionario
        stats_generos = {}
        libros_disponibles = 0
        libros_prestados = 0
        
        for isbn, (titulo, autor, genero, disponible) in biblioteca.items():
            # Contar por género
            stats_generos[genero] = stats_generos.get(genero, 0) + 1
            
            # Contar disponibilidad
            if disponible:
                libros_disponibles += 1
            else:
                libros_prestados += 1
        
        print(f"\n=== ESTADÍSTICAS DE LA BIBLIOTECA ===")
        print(f"Total de libros: {len(biblioteca)}")
        print(f"Disponibles: {libros_disponibles}")
        print(f"Prestados: {libros_prestados}")
        print(f"Usuarios activos: {len(usuarios_activos)}")
        
        print(f"\nLibros por género:")
        for genero, cantidad in stats_generos.items():
            print(f"- {genero.title()}: {cantidad}")
    
    # Menú principal
    while True:
        print("\n=== SISTEMA DE BIBLIOTECA ===")
        print("1. Agregar libro")
        print("2. Buscar libro")
        print("3. Prestar libro")
        print("4. Devolver libro")
        print("5. Ver estadísticas")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            agregar_libro()
        elif opcion == "2":
            buscar_libro()
        elif opcion == "3":
            prestar_libro()
        elif opcion == "4":
            devolver_libro()
        elif opcion == "5":
            mostrar_estadisticas()
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida")

# Ejecutar (descomenta para probar)
# sistema_biblioteca()
```

## 🎯 Cuándo Usar Cada Estructura

| Estructura | Cuándo usar | Ejemplo |
|------------|-------------|---------|
| **Lista** | Elementos ordenados que pueden cambiar | Lista de tareas, historial |
| **Diccionario** | Datos relacionados clave-valor | Información de usuario, configuración |
| **Tupla** | Datos inmutables relacionados | Coordenadas, información fija |
| **Conjunto** | Elementos únicos, operaciones matemáticas | Tags, categorías únicas |

## 💡 Ejercicios Prácticos

### Ejercicio 1: Análisis de Texto

```python
def analizar_texto():
    """
    Analiza un texto y proporciona estadísticas usando diferentes estructuras.
    """
    texto = input("Escribe un texto para analizar: ")
    
    # Tu código aquí:
    # 1. Contar palabras totales (lista)
    # 2. Encontrar palabras únicas (conjunto)
    # 3. Contar frecuencia de cada palabra (diccionario)
    # 4. Mostrar la palabra más común
    pass

# Ejecutar
analizar_texto()
```

### Ejercicio 2: Gestión de Inventario

```python
def inventario_tienda():
    """
    Sistema de inventario que usa diccionarios anidados.
    """
    # Estructura: {"producto": {"precio": X, "stock": Y, "categoria": Z}}
    inventario = {}
    
    # Tu código aquí:
    # 1. Agregar productos con precio, stock y categoría
    # 2. Actualizar stock
    # 3. Buscar productos por categoría
    # 4. Calcular valor total del inventario
    pass

# Ejecutar
inventario_tienda()
```

## 🎯 Puntos Clave

- ✅ Las listas son ordenadas y modificables - perfectas para secuencias
- ✅ Los diccionarios organizan datos con claves - ideales para información relacionada
- ✅ Las tuplas son inmutables - excelentes para datos que no cambian
- ✅ Los conjuntos eliminan duplicados - útiles para elementos únicos
- ✅ Elegir la estructura correcta mejora el rendimiento y claridad del código

## 🚀 Siguiente Paso

En la siguiente unidad aprenderemos sobre **Funciones y Módulos**, donde organizaremos nuestro código en bloques reutilizables y aprenderemos a usar librerías externas.

---

### 📚 Recursos Adicionales

- [Python Data Structures Documentation](https://docs.python.org/3/tutorial/datastructures.html)
- [Real Python - Python Lists and Tuples](https://realpython.com/python-lists-tuples/)
- [Real Python - Dictionaries](https://realpython.com/python-dicts/)