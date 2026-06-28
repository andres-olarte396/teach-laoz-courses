"""
🎓 EVALUACIÓN FASE 1: FUNDAMENTOS DE INTELIGENCIA ARTIFICIAL
===========================================================

📋 INSTRUCCIONES GENERALES:
• Esta evaluación integra todos los conocimientos de la Fase 1
• Duración total estimada: 3-4 horas (puede realizarse en múltiples sesiones)
• Puntaje total: 100 puntos
• Puntaje mínimo para aprobar: 70 puntos
• Puedes consultar tus notas y materiales del curso

🎯 OBJETIVOS DE EVALUACIÓN:
• Demostrar comprensión sólida de conceptos fundamentales de IA
• Aplicar conocimientos a situaciones prácticas y casos reales
• Analizar críticamente aplicaciones y limitaciones de la IA
• Evaluar implicaciones éticas y sociales de la tecnología
• Proponer soluciones creativas usando principios de IA

⚠️ IMPORTANTE:
• Lee cuidadosamente cada pregunta antes de responder
• Justifica tus respuestas con argumentos sólidos
• Usa ejemplos concretos cuando sea posible
• Sé honesto en tus respuestas - no hay respuestas "perfectas"
"""

import os
from datetime import datetime

# Configuración de la evaluación
ESTUDIANTE_NOMBRE = input("👤 Ingresa tu nombre completo: ")
FECHA_EVALUACION = datetime.now().strftime("%Y-%m-%d %H:%M")

print(f"""
{'='*70}
🎓 EVALUACIÓN FASE 1: FUNDAMENTOS DE INTELIGENCIA ARTIFICIAL
{'='*70}

👤 Estudiante: {ESTUDIANTE_NOMBRE}
📅 Fecha: {FECHA_EVALUACION}
⏱️ Duración estimada: 3-4 horas
📊 Puntaje total: 100 puntos
✅ Puntaje mínimo: 70 puntos

{'='*70}
""")

# Variables para almacenar respuestas y puntajes
respuestas = {}
puntajes = {}
puntaje_total = 0

# ============================================================================
# 📝 SECCIÓN I: CONCEPTOS FUNDAMENTALES (30 puntos)
# ============================================================================

def seccion_conceptos_fundamentales():
    """
    Evalúa la comprensión de conceptos básicos de IA
    """
    print("📝 SECCIÓN I: CONCEPTOS FUNDAMENTALES (30 puntos)")
    print("=" * 50)
    
    global respuestas, puntajes, puntaje_total
    
    # Pregunta 1 (8 puntos)
    print("\n🎯 PREGUNTA 1 (8 puntos)")
    print("Define Inteligencia Artificial con tus propias palabras.")
    print("Incluye al menos 3 características principales que debe tener un sistema de IA.")
    print("\nTu respuesta:")
    
    respuesta_1 = input(">>> ")
    respuestas['pregunta_1'] = respuesta_1
    
    print("\n📊 CRITERIOS DE EVALUACIÓN:")
    print("• Definición clara y precisa (3 puntos)")
    print("• Identifica 3+ características (3 puntos)")
    print("• Uso correcto de terminología (2 puntos)")
    
    # Pregunta 2 (8 puntos)
    print("\n🎯 PREGUNTA 2 (8 puntos)")
    print("Explica la relación jerárquica entre IA, Machine Learning y Deep Learning.")
    print("Proporciona un ejemplo concreto de cada nivel.")
    print("\nTu respuesta:")
    
    respuesta_2 = input(">>> ")
    respuestas['pregunta_2'] = respuesta_2
    
    print("\n📊 CRITERIOS DE EVALUACIÓN:")
    print("• Explica jerarquía correctamente (4 puntos)")
    print("• Proporciona ejemplos apropiados (3 puntos)")
    print("• Claridad de explicación (1 punto)")
    
    # Pregunta 3 (7 puntos)
    print("\n🎯 PREGUNTA 3 (7 puntos)")
    print("Menciona y describe brevemente los 5 componentes principales")
    print("de un sistema de IA (desde entrada hasta salida).")
    print("\nTu respuesta:")
    
    respuesta_3 = input(">>> ")
    respuestas['pregunta_3'] = respuesta_3
    
    print("\n📊 CRITERIOS DE EVALUACIÓN:")
    print("• Identifica 5 componentes correctos (5 puntos)")
    print("• Describe función de cada uno (2 puntos)")
    
    # Pregunta 4 (7 puntos)
    print("\n🎯 PREGUNTA 4 (7 puntos)")
    print("¿Cuáles son las 3 principales diferencias entre")
    print("inteligencia humana e inteligencia artificial?")
    print("Da un ejemplo de cada diferencia.")
    print("\nTu respuesta:")
    
    respuesta_4 = input(">>> ")
    respuestas['pregunta_4'] = respuesta_4
    
    print("\n📊 CRITERIOS DE EVALUACIÓN:")
    print("• Identifica 3 diferencias clave (3 puntos)")
    print("• Ejemplos apropiados para cada una (3 puntos)")
    print("• Comprensión de fortalezas/debilidades (1 punto)")

# ============================================================================
# 🕰️ SECCIÓN II: HISTORIA Y EVOLUCIÓN (20 puntos)
# ============================================================================

def seccion_historia_evolucion():
    """
    Evalúa conocimiento sobre la historia y evolución de la IA
    """
    print("\n🕰️ SECCIÓN II: HISTORIA Y EVOLUCIÓN (20 puntos)")
    print("=" * 50)
    
    global respuestas, puntajes, puntaje_total
    
    # Pregunta 5 (6 puntos)
    print("\n🎯 PREGUNTA 5 (6 puntos)")
    print("Ordena cronológicamente estos eventos históricos de la IA:")
    print("A) Test de Turing")
    print("B) Perceptrón de Rosenblatt") 
    print("C) Conferencia de Dartmouth")
    print("D) Boom del Deep Learning")
    print("E) Primer invierno de la IA")
    print("F) IBM Watson vence en Jeopardy")
    print("\nEscribe el orden correcto (ejemplo: A, C, B, F, E, D):")
    
    respuesta_5 = input(">>> ")
    respuestas['pregunta_5'] = respuesta_5
    
    print("\n✅ ORDEN CORRECTO: A(1950), C(1956), B(1957), E(1974-1980), F(2011), D(2012)")
    
    # Pregunta 6 (8 puntos)
    print("\n🎯 PREGUNTA 6 (8 puntos)")
    print("Explica qué son los 'inviernos de la IA' y por qué ocurrieron.")
    print("Menciona al menos 2 causas principales de estos períodos.")
    print("\nTu respuesta:")
    
    respuesta_6 = input(">>> ")
    respuestas['pregunta_6'] = respuesta_6
    
    print("\n📊 CRITERIOS DE EVALUACIÓN:")
    print("• Define correctamente 'inviernos de IA' (3 puntos)")
    print("• Identifica 2+ causas principales (4 puntos)")
    print("• Comprende el impacto histórico (1 punto)")
    
    # Pregunta 7 (6 puntos)
    print("\n🎯 PREGUNTA 7 (6 puntos)")
    print("¿Cuáles consideras que son los 3 factores principales")
    print("que han impulsado el boom actual de la IA (2010-presente)?")
    print("\nTu respuesta:")
    
    respuesta_7 = input(">>> ")
    respuestas['pregunta_7'] = respuesta_7
    
    print("\n📊 CRITERIOS DE EVALUACIÓN:")
    print("• Identifica 3 factores relevantes (4 puntos)")
    print("• Comprende la convergencia de factores (2 puntos)")

# ============================================================================
# 🧩 SECCIÓN III: TIPOS Y CLASIFICACIONES (20 puntos)
# ============================================================================

def seccion_tipos_clasificaciones():
    """
    Evalúa comprensión de tipos y clasificaciones de IA
    """
    print("\n🧩 SECCIÓN III: TIPOS Y CLASIFICACIONES (20 puntos)")
    print("=" * 50)
    
    global respuestas, puntajes, puntaje_total
    
    # Pregunta 8 (8 puntos)
    print("\n🎯 PREGUNTA 8 (8 puntos)")
    print("Clasifica estos sistemas según su nivel de autonomía (0-5):")
    print("• Netflix recommendations")
    print("• Tesla Autopilot")
    print("• Calculadora científica")
    print("• GitHub Copilot")
    print("• Waymo (vehículo autónomo)")
    print("• Alexa/Siri")
    print("\nFormato: Sistema - Nivel (justificación breve)")
    print("Ejemplo: ChatGPT - Nivel 3 (asiste aumentando capacidades significativamente)")
    
    respuesta_8 = input(">>> ")
    respuestas['pregunta_8'] = respuesta_8
    
    print("\n📊 CRITERIOS DE EVALUACIÓN:")
    print("• Clasificación correcta de niveles (4 puntos)")
    print("• Justificaciones apropiadas (4 puntos)")
    
    # Pregunta 9 (6 puntos)
    print("\n🎯 PREGUNTA 9 (6 puntos)")
    print("¿Cuál es la principal diferencia entre IA débil y IA fuerte?")
    print("Da un ejemplo de cada tipo (real o hipotético).")
    print("\nTu respuesta:")
    
    respuesta_9 = input(">>> ")
    respuestas['pregunta_9'] = respuesta_9
    
    print("\n📊 CRITERIOS DE EVALUACIÓN:")
    print("• Define diferencia correctamente (3 puntos)")
    print("• Ejemplos apropiados (2 puntos)")
    print("• Comprende estado actual vs futuro (1 punto)")
    
    # Pregunta 10 (6 puntos)
    print("\n🎯 PREGUNTA 10 (6 puntos)")
    print("Menciona 3 enfoques técnicos para implementar IA")
    print("y explica cuándo es mejor usar cada uno.")
    print("\nTu respuesta:")
    
    respuesta_10 = input(">>> ")
    respuestas['pregunta_10'] = respuesta_10
    
    print("\n📊 CRITERIOS DE EVALUACIÓN:")
    print("• Identifica 3 enfoques correctos (3 puntos)")
    print("• Explica casos de uso apropiados (3 puntos)")

# ============================================================================
# 🌟 SECCIÓN IV: APLICACIONES PRÁCTICAS (15 puntos)
# ============================================================================

def seccion_aplicaciones_practicas():
    """
    Evalúa conocimiento sobre aplicaciones reales de IA
    """
    print("\n🌟 SECCIÓN IV: APLICACIONES PRÁCTICAS (15 puntos)")
    print("=" * 50)
    
    global respuestas, puntajes, puntaje_total
    
    # Pregunta 11 (8 puntos)
    print("\n🎯 PREGUNTA 11 (8 puntos)")
    print("Analiza el caso de IBM Watson for Oncology:")
    print("a) ¿Cuál era su objetivo principal?")
    print("b) Menciona 2 problemas que enfrentó")
    print("c) ¿Qué lecciones podemos aprender de este caso?")
    print("\nTu respuesta:")
    
    respuesta_11 = input(">>> ")
    respuestas['pregunta_11'] = respuesta_11
    
    print("\n📊 CRITERIOS DE EVALUACIÓN:")
    print("• Comprende el objetivo del sistema (2 puntos)")
    print("• Identifica problemas reales (4 puntos)")
    print("• Extrae lecciones valiosas (2 puntos)")
    
    # Pregunta 12 (7 puntos)
    print("\n🎯 PREGUNTA 12 (7 puntos)")
    print("En vehículos autónomos, ¿cómo debe programarse la IA")
    print("para decidir en situaciones de dilema ético?")
    print("(Por ejemplo: elegir entre atropellar 1 persona vs 5)")
    print("Justifica tu posición con argumentos éticos.")
    print("\nTu respuesta:")
    
    respuesta_12 = input(">>> ")
    respuestas['pregunta_12'] = respuesta_12
    
    print("\n📊 CRITERIOS DE EVALUACIÓN:")
    print("• Comprende la complejidad del dilema (3 puntos)")
    print("• Propone enfoque ético coherente (3 puntos)")
    print("• Considera implicaciones prácticas (1 punto)")

# ============================================================================
# 🤖 SECCIÓN V: MACHINE LEARNING BÁSICO (15 puntos)
# ============================================================================

def seccion_machine_learning():
    """
    Evalúa comprensión básica de Machine Learning
    """
    print("\n🤖 SECCIÓN V: MACHINE LEARNING BÁSICO (15 puntos)")
    print("=" * 50)
    
    global respuestas, puntajes, puntaje_total
    
    # Pregunta 13 (8 puntos)
    print("\n🎯 PREGUNTA 13 (8 puntos)")
    print("Describe las 8 fases del proceso de Machine Learning")
    print("y explica por qué es importante cada una.")
    print("\nTu respuesta:")
    
    respuesta_13 = input(">>> ")
    respuestas['pregunta_13'] = respuesta_13
    
    print("\n📊 CRITERIOS DE EVALUACIÓN:")
    print("• Identifica las 8 fases correctamente (4 puntos)")
    print("• Explica importancia de cada fase (4 puntos)")
    
    # Pregunta 14 (7 puntos)
    print("\n🎯 PREGUNTA 14 (7 puntos)")
    print("¿Qué es el overfitting en Machine Learning?")
    print("¿Cómo se puede detectar y prevenir?")
    print("Da un ejemplo práctico.")
    print("\nTu respuesta:")
    
    respuesta_14 = input(">>> ")
    respuestas['pregunta_14'] = respuesta_14
    
    print("\n📊 CRITERIOS DE EVALUACIÓN:")
    print("• Define overfitting correctamente (3 puntos)")
    print("• Métodos de detección/prevención (3 puntos)")
    print("• Ejemplo práctico apropiado (1 punto)")

# ============================================================================
# 💭 EVALUACIÓN FINAL Y RETROALIMENTACIÓN
# ============================================================================

def evaluacion_final():
    """
    Proporciona evaluación final y retroalimentación
    """
    print("\n💭 EVALUACIÓN FINAL")
    print("=" * 50)
    
    print("🎉 ¡Has completado la evaluación!")
    print("Ahora realizaremos una autoevaluación de tu desempeño.")
    
    # Autoevaluación del estudiante
    print("\n🤔 AUTOEVALUACIÓN:")
    
    auto_comprension = int(input("¿Qué tan bien comprendes los conceptos de IA? (1-10): "))
    auto_aplicacion = int(input("¿Qué tan bien puedes aplicar estos conocimientos? (1-10): "))
    auto_confianza = int(input("¿Qué tan confiado te sientes con la IA? (1-10): "))
    
    areas_dificiles = input("¿Qué temas te resultaron más difíciles? ")
    areas_interesantes = input("¿Qué temas te resultaron más interesantes? ")
    
    print(f"\n📊 TU AUTOEVALUACIÓN:")
    print(f"   Comprensión de conceptos: {auto_comprension}/10")
    print(f"   Capacidad de aplicación: {auto_aplicacion}/10")
    print(f"   Nivel de confianza: {auto_confianza}/10")
    print(f"   Promedio general: {(auto_comprension + auto_aplicacion + auto_confianza)/3:.1f}/10")
    
    # Feedback personalizado
    promedio_auto = (auto_comprension + auto_aplicacion + auto_confianza) / 3
    
    if promedio_auto >= 8:
        print("\n🌟 ¡Excelente autoevaluación! Pareces tener una base muy sólida.")
    elif promedio_auto >= 6:
        print("\n👍 Buena autoevaluación. Tienes una base sólida con áreas de mejora identificadas.")
    else:
        print("\n📚 Tu autoevaluación sugiere que necesitas más práctica y repaso.")
    
    # Recomendaciones personalizadas
    print(f"\n💡 RECOMENDACIONES BASADAS EN TU AUTOEVALUACIÓN:")
    
    if auto_comprension < 7:
        print("   📖 Repasa los conceptos fundamentales con los ejemplos interactivos")
    
    if auto_aplicacion < 7:
        print("   🛠️ Practica más con los ejemplos prácticos de la fase")
    
    if auto_confianza < 7:
        print("   💪 Realiza ejercicios adicionales para ganar confianza")
    
    if areas_dificiles:
        print(f"   🎯 Enfócate especialmente en: {areas_dificiles}")
    
    if areas_interesantes:
        print(f"   🚀 Explora más sobre: {areas_interesantes}")

def generar_reporte_evaluacion():
    """
    Genera reporte final de la evaluación
    """
    print("\n📋 GENERANDO REPORTE DE EVALUACIÓN...")
    
    # Crear archivo de reporte
    nombre_archivo = f"evaluacion_fase1_{ESTUDIANTE_NOMBRE.replace(' ', '_')}_{datetime.now().strftime('%Y%m%d_%H%M')}.txt"
    
    with open(nombre_archivo, 'w', encoding='utf-8') as archivo:
        archivo.write("🎓 REPORTE DE EVALUACIÓN - FASE 1: FUNDAMENTOS DE IA\n")
        archivo.write("=" * 60 + "\n\n")
        archivo.write(f"👤 Estudiante: {ESTUDIANTE_NOMBRE}\n")
        archivo.write(f"📅 Fecha: {FECHA_EVALUACION}\n")
        archivo.write(f"⏱️ Duración: {datetime.now().strftime('%H:%M')}\n\n")
        
        archivo.write("📝 RESPUESTAS:\n")
        archivo.write("-" * 40 + "\n")
        
        for i, (pregunta, respuesta) in enumerate(respuestas.items(), 1):
            archivo.write(f"\nPregunta {i}:\n{respuesta}\n")
        
        archivo.write(f"\n💭 REFLEXIÓN FINAL:\n")
        archivo.write("Esta evaluación cubre los fundamentos esenciales de la IA.\n")
        archivo.write("Las respuestas reflejan tu comprensión actual del tema.\n")
        archivo.write("\n🚀 PRÓXIMOS PASOS:\n")
        archivo.write("• Revisa las áreas donde sientes menos confianza\n")
        archivo.write("• Practica con ejemplos adicionales\n")
        archivo.write("• Prepárate para la Fase 2: Aplicaciones Específicas\n")
    
    print(f"✅ Reporte guardado como: {nombre_archivo}")
    
    return nombre_archivo

# ============================================================================
# 🚀 FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Ejecuta la evaluación completa de la Fase 1
    """
    print("¡Bienvenido a la evaluación de Fundamentos de IA!")
    print("Responde con honestidad y detalle. ¡Buena suerte! 🍀\n")
    
    # Ejecutar secciones de evaluación
    seccion_conceptos_fundamentales()
    seccion_historia_evolucion()
    seccion_tipos_clasificaciones()
    seccion_aplicaciones_practicas()
    seccion_machine_learning()
    evaluacion_final()
    
    # Generar reporte
    archivo_reporte = generar_reporte_evaluacion()
    
    print(f"\n🎉 ¡EVALUACIÓN COMPLETADA!")
    print(f"📄 Reporte guardado: {archivo_reporte}")
    print("\n📚 RECURSOS PARA CONTINUAR:")
    print("   • Revisa tus respuestas y reflexiona sobre ellas")
    print("   • Repasa conceptos donde sientes menos confianza")
    print("   • Explora los ejemplos interactivos adicionales")
    print("   • Prepárate para las fases avanzadas del curso")
    
    print(f"\n🌟 ¡Felicidades {ESTUDIANTE_NOMBRE}!")
    print("Has completado la evaluación de Fundamentos de IA.")
    print("Continúa practicando y explorando este fascinante campo.")

if __name__ == "__main__":
    main()