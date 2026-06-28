# ============================================================================
# EJEMPLO 07: LISTAS - COLECCIONES DE DATOS
# ============================================================================
# Tema: Estructuras de datos - Listas
# Objetivo: Organizar y manipular colecciones de elementos
# Nivel: Intermedio
# Prerrequisito: ejemplo_06_bucles.py

print("=== GESTOR DE LISTA DE TAREAS ===")

# Inicializar lista de tareas
tareas = []
tareas_completadas = []

# Función auxiliar para mostrar menú
def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Agregar tarea")
    print("2. Ver todas las tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Ver tareas completadas")
    print("6. Estadísticas")
    print("7. Salir")

# Programa principal
while True:
    mostrar_menu()
    opcion = input("\nSelecciona una opción: ")
    
    if opcion == "1":
        # Agregar tarea
        nueva_tarea = input("Describe la nueva tarea: ")
        tareas.append(nueva_tarea)
        print(f"✅ Tarea '{nueva_tarea}' agregada correctamente")
        
    elif opcion == "2":
        # Ver todas las tareas
        print("\n=== LISTA DE TAREAS PENDIENTES ===")
        if len(tareas) == 0:
            print("No tienes tareas pendientes. ¡Buen trabajo!")
        else:
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
                
    elif opcion == "3":
        # Marcar como completada
        if len(tareas) == 0:
            print("No hay tareas pendientes para completar.")
        else:
            print("\nTareas pendientes:")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
            
            try:
                indice = int(input("¿Qué tarea completaste? (número): ")) - 1
                if 0 <= indice < len(tareas):
                    tarea_completada = tareas.pop(indice)  # Elimina y retorna
                    tareas_completadas.append(tarea_completada)
                    print(f"🎉 ¡Felicidades! Completaste: '{tarea_completada}'")
                else:
                    print("Número de tarea no válido.")
            except ValueError:
                print("Por favor ingresa un número válido.")
                
    elif opcion == "4":
        # Eliminar tarea
        if len(tareas) == 0:
            print("No hay tareas para eliminar.")
        else:
            print("\nTareas actuales:")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")
            
            try:
                indice = int(input("¿Qué tarea quieres eliminar? (número): ")) - 1
                if 0 <= indice < len(tareas):
                    tarea_eliminada = tareas.pop(indice)
                    print(f"🗑️ Tarea eliminada: '{tarea_eliminada}'")
                else:
                    print("Número de tarea no válido.")
            except ValueError:
                print("Por favor ingresa un número válido.")
                
    elif opcion == "5":
        # Ver tareas completadas
        print("\n=== TAREAS COMPLETADAS ===")
        if len(tareas_completadas) == 0:
            print("Aún no has completado ninguna tarea.")
        else:
            for i, tarea in enumerate(tareas_completadas, 1):
                print(f"✅ {i}. {tarea}")
                
    elif opcion == "6":
        # Estadísticas
        total_pendientes = len(tareas)
        total_completadas = len(tareas_completadas)
        total_tareas = total_pendientes + total_completadas
        
        print("\n=== ESTADÍSTICAS ===")
        print(f"Tareas pendientes: {total_pendientes}")
        print(f"Tareas completadas: {total_completadas}")
        print(f"Total de tareas creadas: {total_tareas}")
        
        if total_tareas > 0:
            porcentaje_completado = (total_completadas / total_tareas) * 100
            print(f"Porcentaje completado: {porcentaje_completado:.1f}%")
            
            # Análisis de productividad
            if porcentaje_completado >= 80:
                print("🌟 ¡Excelente productividad!")
            elif porcentaje_completado >= 50:
                print("👍 Buena productividad, sigue así")
            else:
                print("💪 Puedes mejorar tu productividad")
                
    elif opcion == "7":
        print("¡Gracias por usar el gestor de tareas!")
        break
        
    else:
        print("Opción no válida. Intenta de nuevo.")

# Ejercicio adicional: Implementar búsqueda de tareas
print("\n--- BÚSQUEDA DE TAREAS ---")
if len(tareas) > 0:
    busqueda = input("Buscar tarea (ingresa una palabra clave): ").lower()
    tareas_encontradas = []
    
    for tarea in tareas:
        if busqueda in tarea.lower():
            tareas_encontradas.append(tarea)
    
    if len(tareas_encontradas) > 0:
        print(f"Tareas encontradas con '{busqueda}':")
        for tarea in tareas_encontradas:
            print(f"  - {tarea}")
    else:
        print(f"No se encontraron tareas con '{busqueda}'")