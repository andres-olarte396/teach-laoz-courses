# ============================================================================
# EJEMPLO 05: CONDICIONALES - DECISIONES EN EL CÓDIGO
# ============================================================================
# Tema: Estructuras de control - if/elif/else
# Objetivo: Crear lógica de decisiones en programas
# Nivel: Principiante-Intermedio
# Prerrequisito: ejemplo_04_entrada_datos.py

print("=== SISTEMA DE CALIFICACIONES ===")
print("Ingresa las calificaciones de un estudiante")

# Obtener datos del estudiante
nombre_estudiante = input("Nombre del estudiante: ")
materia = input("Materia: ")

# Obtener calificaciones (asumimos escala 0-100)
calif1 = float(input("Primera calificación (0-100): "))
calif2 = float(input("Segunda calificación (0-100): "))
calif3 = float(input("Tercera calificación (0-100): "))

# Calcular promedio
promedio = (calif1 + calif2 + calif3) / 3

print(f"\n=== REPORTE DE {nombre_estudiante.upper()} ===")
print(f"Materia: {materia}")
print(f"Calificaciones: {calif1}, {calif2}, {calif3}")
print(f"Promedio: {promedio:.2f}")

# Determinar letra de calificación
if promedio >= 90:
    letra = "A"
    comentario = "¡Excelente trabajo!"
elif promedio >= 80:
    letra = "B"
    comentario = "Buen trabajo"
elif promedio >= 70:
    letra = "C"
    comentario = "Trabajo satisfactorio"
elif promedio >= 60:
    letra = "D"
    comentario = "Necesita mejorar"
else:
    letra = "F"
    comentario = "Debe repetir la materia"

print(f"Calificación: {letra}")
print(f"Comentario: {comentario}")

# Verificaciones adicionales con operadores lógicos
print("\n=== ANÁLISIS ADICIONAL ===")

# ¿Aprobó?
aprobo = promedio >= 70
print(f"¿Aprobó? {'Sí' if aprobo else 'No'}")

# ¿Tuvo calificaciones consistentes?
rango = max(calif1, calif2, calif3) - min(calif1, calif2, calif3)
es_consistente = rango <= 10
print(f"¿Calificaciones consistentes? {'Sí' if es_consistente else 'No'} (rango: {rango:.1f})")

# ¿Mejoró en el último examen?
mejoro = calif3 > calif1 and calif3 > calif2
print(f"¿Mejoró en el último examen? {'Sí' if mejoro else 'No'}")

# Recomendaciones
print("\n=== RECOMENDACIONES ===")
if promedio >= 90 and es_consistente:
    print("¡Estudiante ejemplar! Considera tomar cursos avanzados.")
elif promedio >= 70 and not es_consistente:
    print("Buen nivel pero trabaja en la consistencia.")
elif promedio < 70 and mejoro:
    print("Aunque el promedio es bajo, muestra mejora. ¡Sigue así!")
else:
    print("Necesita apoyo adicional y plan de estudios personalizado.")

# Ejercicio: Agrega una verificación para "estudiante en riesgo"
# (promedio < 65 y ninguna calificación individual > 70)