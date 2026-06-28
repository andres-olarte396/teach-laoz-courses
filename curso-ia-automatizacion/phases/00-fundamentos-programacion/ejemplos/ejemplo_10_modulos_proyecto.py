# ============================================================================
# EJEMPLO 10: MÓDULOS Y LIBRERÍAS - CÓDIGO ORGANIZADO
# ============================================================================
# Tema: Importación y uso de módulos
# Objetivo: Organizar código en módulos y usar librerías externas
# Nivel: Avanzado
# Prerrequisito: ejemplo_09_funciones.py

# Importar módulos estándar de Python
import datetime
import random
import math
import os

print("=== PROYECTO INTEGRADOR: AGENDA PERSONAL ===")

# Clase para representar una tarea
class Tarea:
    def __init__(self, titulo, descripcion, fecha_limite=None, prioridad="media"):
        self.titulo = titulo
        self.descripcion = descripcion
        self.fecha_creacion = datetime.datetime.now()
        self.fecha_limite = fecha_limite
        self.prioridad = prioridad
        self.completada = False
        self.id = self.generar_id()
    
    def generar_id(self):
        """Genera un ID único para la tarea"""
        return random.randint(1000, 9999)
    
    def marcar_completada(self):
        """Marca la tarea como completada"""
        self.completada = True
    
    def dias_restantes(self):
        """Calcula cuántos días faltan para la fecha límite"""
        if not self.fecha_limite:
            return None
        
        hoy = datetime.date.today()
        diferencia = self.fecha_limite - hoy
        return diferencia.days
    
    def es_urgente(self):
        """Determina si la tarea es urgente (menos de 3 días)"""
        dias = self.dias_restantes()
        return dias is not None and dias <= 3 and dias >= 0
    
    def __str__(self):
        estado = "✅" if self.completada else "⏳"
        prioridad_emoji = {"alta": "🔴", "media": "🟡", "baja": "🟢"}
        
        info = f"{estado} [{self.id}] {self.titulo} - {prioridad_emoji.get(self.prioridad, '⚪')}"
        
        if self.fecha_limite:
            dias = self.dias_restantes()
            if dias is not None:
                if dias < 0:
                    info += f" (VENCIDA: {abs(dias)} días)"
                elif dias == 0:
                    info += " (HOY)"
                else:
                    info += f" ({dias} días restantes)"
        
        return info

# Clase principal para gestionar la agenda
class AgendaPersonal:
    def __init__(self):
        self.tareas = []
        self.archivo_datos = "agenda_personal.txt"
        self.cargar_datos()
    
    def agregar_tarea(self, titulo, descripcion, fecha_limite_str=None, prioridad="media"):
        """Agrega una nueva tarea a la agenda"""
        fecha_limite = None
        
        if fecha_limite_str:
            try:
                # Convertir string a fecha (formato: YYYY-MM-DD)
                fecha_limite = datetime.datetime.strptime(fecha_limite_str, "%Y-%m-%d").date()
            except ValueError:
                print("Formato de fecha inválido. Use YYYY-MM-DD")
                return False
        
        tarea = Tarea(titulo, descripcion, fecha_limite, prioridad)
        self.tareas.append(tarea)
        self.guardar_datos()
        return True
    
    def listar_tareas(self, filtro=None):
        """Lista las tareas según el filtro especificado"""
        tareas_filtradas = self.tareas
        
        if filtro == "pendientes":
            tareas_filtradas = [t for t in self.tareas if not t.completada]
        elif filtro == "completadas":
            tareas_filtradas = [t for t in self.tareas if t.completada]
        elif filtro == "urgentes":
            tareas_filtradas = [t for t in self.tareas if t.es_urgente() and not t.completada]
        
        if not tareas_filtradas:
            print(f"No hay tareas {filtro if filtro else 'registradas'}")
            return
        
        print(f"\n=== TAREAS {filtro.upper() if filtro else 'TODAS'} ===")
        for tarea in tareas_filtradas:
            print(tarea)
            if filtro != "completadas":
                print(f"    📝 {tarea.descripcion}")
    
    def completar_tarea(self, tarea_id):
        """Marca una tarea como completada por su ID"""
        for tarea in self.tareas:
            if tarea.id == tarea_id and not tarea.completada:
                tarea.marcar_completada()
                self.guardar_datos()
                print(f"🎉 Tarea '{tarea.titulo}' marcada como completada!")
                return True
        
        print(f"No se encontró tarea pendiente con ID {tarea_id}")
        return False
    
    def eliminar_tarea(self, tarea_id):
        """Elimina una tarea por su ID"""
        for i, tarea in enumerate(self.tareas):
            if tarea.id == tarea_id:
                tarea_eliminada = self.tareas.pop(i)
                self.guardar_datos()
                print(f"🗑️ Tarea '{tarea_eliminada.titulo}' eliminada")
                return True
        
        print(f"No se encontró tarea con ID {tarea_id}")
        return False
    
    def estadisticas(self):
        """Muestra estadísticas de la agenda"""
        total = len(self.tareas)
        completadas = len([t for t in self.tareas if t.completada])
        pendientes = total - completadas
        urgentes = len([t for t in self.tareas if t.es_urgente() and not t.completada])
        
        print("\n=== ESTADÍSTICAS ===")
        print(f"📊 Total de tareas: {total}")
        print(f"✅ Completadas: {completadas}")
        print(f"⏳ Pendientes: {pendientes}")
        print(f"🚨 Urgentes: {urgentes}")
        
        if total > 0:
            porcentaje = (completadas / total) * 100
            print(f"📈 Progreso: {porcentaje:.1f}%")
            
            # Usar math para cálculos estadísticos
            if completadas > 0:
                promedio_dias = self.calcular_promedio_dias_completadas()
                if promedio_dias:
                    print(f"⏱️ Tiempo promedio para completar: {promedio_dias:.1f} días")
    
    def calcular_promedio_dias_completadas(self):
        """Calcula el promedio de días para completar tareas"""
        completadas = [t for t in self.tareas if t.completada]
        if not completadas:
            return None
        
        total_dias = 0
        contador = 0
        
        for tarea in completadas:
            if tarea.fecha_limite:
                dias_tomados = (tarea.fecha_limite - tarea.fecha_creacion.date()).days
                if dias_tomados > 0:
                    total_dias += dias_tomados
                    contador += 1
        
        return total_dias / contador if contador > 0 else None
    
    def guardar_datos(self):
        """Guarda las tareas en un archivo"""
        try:
            with open(self.archivo_datos, 'w', encoding='utf-8') as archivo:
                for tarea in self.tareas:
                    linea = f"{tarea.id}|{tarea.titulo}|{tarea.descripcion}|"
                    linea += f"{tarea.fecha_creacion.isoformat()}|"
                    linea += f"{tarea.fecha_limite.isoformat() if tarea.fecha_limite else 'None'}|"
                    linea += f"{tarea.prioridad}|{tarea.completada}\n"
                    archivo.write(linea)
        except Exception as e:
            print(f"Error al guardar datos: {e}")
    
    def cargar_datos(self):
        """Carga las tareas desde un archivo"""
        if not os.path.exists(self.archivo_datos):
            return
        
        try:
            with open(self.archivo_datos, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    partes = linea.strip().split('|')
                    if len(partes) == 7:
                        tarea = Tarea(partes[1], partes[2])
                        tarea.id = int(partes[0])
                        tarea.fecha_creacion = datetime.datetime.fromisoformat(partes[3])
                        
                        if partes[4] != 'None':
                            tarea.fecha_limite = datetime.date.fromisoformat(partes[4])
                        
                        tarea.prioridad = partes[5]
                        tarea.completada = partes[6] == 'True'
                        
                        self.tareas.append(tarea)
        except Exception as e:
            print(f"Error al cargar datos: {e}")

# Función principal del programa
def main():
    agenda = AgendaPersonal()
    
    print("¡Bienvenido a tu Agenda Personal!")
    print(f"Fecha actual: {datetime.date.today().strftime('%d/%m/%Y')}")
    
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Agregar tarea")
        print("2. Ver todas las tareas")
        print("3. Ver tareas pendientes")
        print("4. Ver tareas completadas")
        print("5. Ver tareas urgentes")
        print("6. Completar tarea")
        print("7. Eliminar tarea")
        print("8. Estadísticas")
        print("9. Generar tarea aleatoria (demo)")
        print("10. Salir")
        
        opcion = input("\nSelecciona una opción: ")
        
        if opcion == "1":
            titulo = input("Título de la tarea: ")
            descripcion = input("Descripción: ")
            fecha_str = input("Fecha límite (YYYY-MM-DD) [opcional]: ")
            
            print("Prioridad: 1=Baja, 2=Media, 3=Alta")
            prioridad_num = input("Prioridad [2]: ") or "2"
            prioridades = {"1": "baja", "2": "media", "3": "alta"}
            prioridad = prioridades.get(prioridad_num, "media")
            
            if agenda.agregar_tarea(titulo, descripcion, fecha_str or None, prioridad):
                print("✅ Tarea agregada exitosamente")
        
        elif opcion == "2":
            agenda.listar_tareas()
        elif opcion == "3":
            agenda.listar_tareas("pendientes")
        elif opcion == "4":
            agenda.listar_tareas("completadas")
        elif opcion == "5":
            agenda.listar_tareas("urgentes")
        
        elif opcion == "6":
            try:
                tarea_id = int(input("ID de la tarea a completar: "))
                agenda.completar_tarea(tarea_id)
            except ValueError:
                print("Por favor ingresa un ID válido (número)")
        
        elif opcion == "7":
            try:
                tarea_id = int(input("ID de la tarea a eliminar: "))
                agenda.eliminar_tarea(tarea_id)
            except ValueError:
                print("Por favor ingresa un ID válido (número)")
        
        elif opcion == "8":
            agenda.estadisticas()
        
        elif opcion == "9":
            # Generar tarea de demostración usando random
            tareas_demo = [
                ("Estudiar Python", "Revisar módulos y funciones"),
                ("Hacer ejercicio", "30 minutos de cardio"),
                ("Leer libro", "Continuar con el capítulo actual"),
                ("Llamar familia", "Ponerse al día con noticias"),
                ("Organizar escritorio", "Limpiar y ordenar documentos")
            ]
            
            titulo, descripcion = random.choice(tareas_demo)
            
            # Fecha aleatoria en los próximos 7 días
            dias_aleatorios = random.randint(1, 7)
            fecha_limite = datetime.date.today() + datetime.timedelta(days=dias_aleatorios)
            
            prioridad = random.choice(["baja", "media", "alta"])
            
            agenda.agregar_tarea(titulo, descripcion, fecha_limite.isoformat(), prioridad)
            print(f"🎲 Tarea demo generada: '{titulo}' (vence en {dias_aleatorios} días)")
        
        elif opcion == "10":
            print("¡Gracias por usar tu Agenda Personal!")
            print("Tus datos han sido guardados automáticamente.")
            break
        
        else:
            print("Opción no válida")

# Ejecutar el programa
if __name__ == "__main__":
    main()

# Ejercicio: Agregar funcionalidad para exportar tareas a CSV