"""
🤖 EJEMPLO 01: Conceptos Básicos de IA
=====================================

📚 OBJETIVOS DE APRENDIZAJE:
• Comprender qué es la Inteligencia Artificial
• Diferenciar IA, Machine Learning y Deep Learning
• Identificar características de sistemas inteligentes
• Reconocer componentes básicos de un sistema de IA

🎯 NIVEL: Básico - Conceptos fundamentales
⏱️ TIEMPO ESTIMADO: 30-45 minutos
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from collections import Counter
import numpy as np

# ============================================================================
# 🧠 PARTE 1: DEFINICIONES Y CONCEPTOS BÁSICOS
# ============================================================================

def mostrar_definiciones():
    """
    Muestra las definiciones fundamentales de IA y campos relacionados
    """
    print("=" * 60)
    print("🧠 DEFINICIONES FUNDAMENTALES")
    print("=" * 60)
    
    definiciones = {
        "🤖 Inteligencia Artificial (IA)": 
            "Capacidad de las máquinas para realizar tareas que normalmente requieren inteligencia humana",
        
        "📊 Machine Learning (ML)": 
            "Subcampo de IA que permite a las máquinas aprender patrones a partir de datos",
        
        "🧠 Deep Learning (DL)": 
            "Subcampo de ML que usa redes neuronales profundas inspiradas en el cerebro",
        
        "📈 Data Science": 
            "Disciplina que extrae conocimiento e insights de datos estructurados y no estructurados",
        
        "🔧 Algoritmo": 
            "Conjunto de reglas o instrucciones para resolver un problema específico"
    }
    
    for concepto, definicion in definiciones.items():
        print(f"\n{concepto}")
        print(f"   ➤ {definicion}")
    
    print("\n" + "=" * 60)

def visualizar_jerarquia_ia():
    """
    Crea un diagrama visual de la jerarquía IA > ML > DL
    """
    fig, ax = plt.subplots(1, 1, figsize=(12, 8))
    
    # Círculos concéntricos para mostrar la jerarquía
    # IA (círculo más grande)
    circle_ia = patches.Circle((0.5, 0.5), 0.45, linewidth=3, 
                              edgecolor='blue', facecolor='lightblue', alpha=0.3)
    ax.add_patch(circle_ia)
    
    # ML (círculo medio)
    circle_ml = patches.Circle((0.5, 0.5), 0.3, linewidth=3, 
                              edgecolor='green', facecolor='lightgreen', alpha=0.5)
    ax.add_patch(circle_ml)
    
    # DL (círculo pequeño)
    circle_dl = patches.Circle((0.5, 0.5), 0.15, linewidth=3, 
                              edgecolor='red', facecolor='lightcoral', alpha=0.7)
    ax.add_patch(circle_dl)
    
    # Etiquetas
    ax.text(0.15, 0.85, 'INTELIGENCIA\nARTIFICIAL', fontsize=14, fontweight='bold',
            ha='center', va='center', color='blue')
    ax.text(0.2, 0.25, 'MACHINE\nLEARNING', fontsize=12, fontweight='bold',
            ha='center', va='center', color='green')
    ax.text(0.5, 0.5, 'DEEP\nLEARNING', fontsize=10, fontweight='bold',
            ha='center', va='center', color='red')
    
    # Ejemplos en cada área
    ax.text(0.85, 0.85, '• Sistemas Expertos\n• Robótica\n• NLP\n• Visión Computacional', 
            fontsize=9, ha='left', va='top', bbox=dict(boxstyle="round,pad=0.3", facecolor="lightblue"))
    
    ax.text(0.85, 0.5, '• Regresión Linear\n• Random Forest\n• SVM\n• K-means', 
            fontsize=9, ha='left', va='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="lightgreen"))
    
    ax.text(0.85, 0.15, '• CNN\n• RNN\n• Transformers\n• GPT/BERT', 
            fontsize=9, ha='left', va='bottom', bbox=dict(boxstyle="round,pad=0.3", facecolor="lightcoral"))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_title('🧠 Jerarquía: IA > Machine Learning > Deep Learning', 
                fontsize=16, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.show()

# ============================================================================
# 🔍 PARTE 2: CARACTERÍSTICAS DE SISTEMAS INTELIGENTES
# ============================================================================

def evaluar_inteligencia_artificial():
    """
    Función interactiva para evaluar si un sistema tiene características de IA
    """
    print("\n" + "=" * 60)
    print("🔍 EVALUADOR DE INTELIGENCIA ARTIFICIAL")
    print("=" * 60)
    
    caracteristicas_ia = {
        "Percepción": "¿Puede recibir y procesar información del entorno?",
        "Razonamiento": "¿Puede analizar información y sacar conclusiones?",
        "Aprendizaje": "¿Puede mejorar su rendimiento con la experiencia?",
        "Planificación": "¿Puede crear estrategias para alcanzar objetivos?",
        "Comunicación": "¿Puede interactuar usando lenguaje natural?",
        "Creatividad": "¿Puede generar soluciones originales?",
        "Adaptación": "¿Puede ajustarse a situaciones nuevas?"
    }
    
    sistemas_ejemplo = {
        "Calculadora": [False, True, False, False, False, False, False],
        "GPS con tráfico": [True, True, True, True, False, False, True],
        "ChatGPT": [True, True, True, False, True, True, True],
        "Termostato inteligente": [True, True, True, True, False, False, True],
        "Robot aspiradora": [True, True, True, True, False, False, True]
    }
    
    print(f"{'Sistema':<20} {'Puntuación IA':<15} {'Nivel de IA'}")
    print("-" * 50)
    
    for sistema, capacidades in sistemas_ejemplo.items():
        puntuacion = sum(capacidades)
        if puntuacion <= 2:
            nivel = "Básico"
        elif puntuacion <= 4:
            nivel = "Intermedio"
        else:
            nivel = "Avanzado"
        
        print(f"{sistema:<20} {puntuacion}/7 ({puntuacion/7*100:.0f}%)<5} {nivel}")
    
    # Visualización
    sistemas = list(sistemas_ejemplo.keys())
    puntuaciones = [sum(capacidades) for capacidades in sistemas_ejemplo.values()]
    
    plt.figure(figsize=(12, 6))
    colors = ['red' if p <= 2 else 'orange' if p <= 4 else 'green' for p in puntuaciones]
    bars = plt.bar(sistemas, puntuaciones, color=colors, alpha=0.7)
    
    # Añadir valores en las barras
    for bar, puntuacion in zip(bars, puntuaciones):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{puntuacion}/7', ha='center', va='bottom', fontweight='bold')
    
    plt.title('🤖 Nivel de Inteligencia Artificial por Sistema', fontsize=14, fontweight='bold')
    plt.ylabel('Puntuación IA (0-7)')
    plt.xlabel('Sistemas')
    plt.ylim(0, 8)
    plt.xticks(rotation=45, ha='right')
    
    # Leyenda de colores
    plt.axhline(y=2.5, color='red', linestyle='--', alpha=0.5, label='IA Básica')
    plt.axhline(y=4.5, color='orange', linestyle='--', alpha=0.5, label='IA Intermedia')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

# ============================================================================
# 🎯 PARTE 3: TIPOS DE PROBLEMAS QUE RESUELVE LA IA
# ============================================================================

def clasificar_problemas_ia():
    """
    Muestra diferentes tipos de problemas que puede resolver la IA
    """
    print("\n" + "=" * 60)
    print("🎯 TIPOS DE PROBLEMAS QUE RESUELVE LA IA")
    print("=" * 60)
    
    tipos_problemas = {
        "🔍 Clasificación": [
            "Detectar spam en emails",
            "Reconocer objetos en imágenes",
            "Diagnosticar enfermedades",
            "Análisis de sentimientos"
        ],
        "📈 Predicción": [
            "Pronóstico del tiempo",
            "Precios de acciones",
            "Demanda de productos",
            "Fallas de equipos"
        ],
        "🎯 Optimización": [
            "Rutas de entrega",
            "Asignación de recursos",
            "Programación de horarios",
            "Diseño de productos"
        ],
        "🎨 Generación": [
            "Crear arte digital",
            "Componer música",
            "Escribir texto",
            "Generar código"
        ],
        "🕵️ Detección de Patrones": [
            "Fraude financiero",
            "Comportamiento anómalo",
            "Tendencias de mercado",
            "Patrones de usuario"
        ]
    }
    
    # Mostrar clasificación
    for tipo, ejemplos in tipos_problemas.items():
        print(f"\n{tipo}")
        for ejemplo in ejemplos:
            print(f"   • {ejemplo}")
    
    # Crear visualización de distribución
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    
    # Gráfico de barras de tipos de problemas
    tipos = list(tipos_problemas.keys())
    cantidades = [len(ejemplos) for ejemplos in tipos_problemas.values()]
    
    ax1.barh(tipos, cantidades, color=['skyblue', 'lightgreen', 'orange', 'pink', 'lavender'])
    ax1.set_xlabel('Número de Ejemplos')
    ax1.set_title('🎯 Distribución de Tipos de Problemas IA')
    
    # Gráfico circular de industrias que usan IA
    industrias = ['Tecnología', 'Salud', 'Finanzas', 'Transporte', 'Retail', 'Manufactura', 'Otros']
    porcentajes = [25, 20, 15, 12, 10, 8, 10]
    
    ax2.pie(porcentajes, labels=industrias, autopct='%1.1f%%', startangle=90)
    ax2.set_title('🏭 Adopción de IA por Industria')
    
    plt.tight_layout()
    plt.show()

# ============================================================================
# 🧪 PARTE 4: SIMULADOR SIMPLE DE IA
# ============================================================================

def simulador_sistema_experto():
    """
    Simulador simple de un sistema experto para diagnóstico básico
    """
    print("\n" + "=" * 60)
    print("🧪 SIMULADOR: SISTEMA EXPERTO SIMPLE")
    print("=" * 60)
    print("Un sistema experto para recomendar actividades según el clima")
    
    # Base de conocimiento (reglas simples)
    reglas = {
        "soleado": {
            "temperatura_alta": "Ir a la playa o piscina",
            "temperatura_media": "Hacer picnic en el parque",
            "temperatura_baja": "Caminar al aire libre"
        },
        "lluvioso": {
            "temperatura_alta": "Ir al centro comercial",
            "temperatura_media": "Leer un libro en casa",
            "temperatura_baja": "Ver películas en casa"
        },
        "nublado": {
            "temperatura_alta": "Hacer ejercicio al aire libre",
            "temperatura_media": "Visitar un museo",
            "temperatura_baja": "Quedarse en casa y cocinar"
        }
    }
    
    def obtener_recomendacion(clima, temperatura):
        """Sistema experto simple con reglas if-then"""
        if clima in reglas and temperatura in reglas[clima]:
            return reglas[clima][temperatura]
        else:
            return "No hay recomendación disponible para estas condiciones"
    
    # Simulación interactiva
    print("\n🌤️ CASOS DE PRUEBA:")
    casos_prueba = [
        ("soleado", "temperatura_alta"),
        ("lluvioso", "temperatura_baja"),
        ("nublado", "temperatura_media"),
        ("nevando", "temperatura_baja")  # Caso no contemplado
    ]
    
    for clima, temp in casos_prueba:
        recomendacion = obtener_recomendacion(clima, temp)
        print(f"   Clima: {clima.title()}, Temperatura: {temp.replace('_', ' ')}")
        print(f"   ➤ Recomendación: {recomendacion}\n")
    
    # Mostrar estructura del sistema experto
    print("🔧 COMPONENTES DEL SISTEMA EXPERTO:")
    print("   • Base de conocimiento: Reglas if-then")
    print("   • Motor de inferencia: Lógica de decisión")
    print("   • Interfaz de usuario: Entrada y salida")
    print("   • Base de hechos: Información actual (clima, temperatura)")

# ============================================================================
# 🎓 PARTE 5: EVALUACIÓN INTERACTIVA
# ============================================================================

def quiz_conceptos_basicos():
    """
    Quiz interactivo sobre conceptos básicos de IA
    """
    print("\n" + "=" * 60)
    print("🎓 QUIZ: CONCEPTOS BÁSICOS DE IA")
    print("=" * 60)
    
    preguntas = [
        {
            "pregunta": "¿Cuál es la relación correcta entre IA, ML y DL?",
            "opciones": [
                "A) Son términos equivalentes",
                "B) IA ⊃ ML ⊃ DL (IA contiene ML, ML contiene DL)",
                "C) DL ⊃ ML ⊃ IA (DL contiene ML, ML contiene IA)",
                "D) No están relacionados"
            ],
            "respuesta_correcta": "B",
            "explicacion": "IA es el campo más amplio, ML es un subcampo de IA, y DL es un subcampo de ML."
        },
        {
            "pregunta": "¿Cuál de estas NO es una característica típica de sistemas de IA?",
            "opciones": [
                "A) Capacidad de aprendizaje",
                "B) Procesamiento de información",
                "C) Operación completamente determinística",
                "D) Adaptación a nuevas situaciones"
            ],
            "respuesta_correcta": "C",
            "explicacion": "Los sistemas de IA suelen ser adaptativos y pueden tomar decisiones probabilísticas, no determinísticas."
        },
        {
            "pregunta": "¿Qué tipo de problema de IA es 'predecir el precio de una casa'?",
            "opciones": [
                "A) Clasificación",
                "B) Regresión",
                "C) Clustering",
                "D) Generación"
            ],
            "respuesta_correcta": "B",
            "explicacion": "Predecir valores numéricos continuos (como precios) es un problema de regresión."
        }
    ]
    
    puntuacion = 0
    for i, pregunta in enumerate(preguntas, 1):
        print(f"\n❓ Pregunta {i}: {pregunta['pregunta']}")
        for opcion in pregunta['opciones']:
            print(f"   {opcion}")
        
        respuesta = input("\n   Tu respuesta (A/B/C/D): ").upper().strip()
        
        if respuesta == pregunta['respuesta_correcta']:
            print("   ✅ ¡Correcto!")
            puntuacion += 1
        else:
            print(f"   ❌ Incorrecto. La respuesta correcta es {pregunta['respuesta_correcta']}")
        
        print(f"   💡 Explicación: {pregunta['explicacion']}")
    
    print(f"\n🏆 PUNTUACIÓN FINAL: {puntuacion}/{len(preguntas)} ({puntuacion/len(preguntas)*100:.0f}%)")
    
    if puntuacion == len(preguntas):
        print("   🎉 ¡Excelente! Dominas los conceptos básicos de IA")
    elif puntuacion >= len(preguntas) * 0.7:
        print("   👍 ¡Bien! Tienes una buena comprensión básica")
    else:
        print("   📚 Revisa los conceptos y vuelve a intentarlo")

# ============================================================================
# 🎯 FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Función principal que ejecuta todo el ejemplo paso a paso
    """
    print("🤖 EJEMPLO 01: CONCEPTOS BÁSICOS DE INTELIGENCIA ARTIFICIAL")
    print("=" * 70)
    
    # Mostrar menú interactivo
    while True:
        print("\n📋 MENÚ DE ACTIVIDADES:")
        print("1. 📚 Ver definiciones fundamentales")
        print("2. 🧠 Visualizar jerarquía IA > ML > DL")
        print("3. 🔍 Evaluar sistemas inteligentes")
        print("4. 🎯 Clasificar tipos de problemas IA")
        print("5. 🧪 Simulador de sistema experto")
        print("6. 🎓 Quiz de conceptos básicos")
        print("7. 🚪 Salir")
        
        opcion = input("\n¿Qué te gustaría explorar? (1-7): ").strip()
        
        if opcion == "1":
            mostrar_definiciones()
        elif opcion == "2":
            visualizar_jerarquia_ia()
        elif opcion == "3":
            evaluar_inteligencia_artificial()
        elif opcion == "4":
            clasificar_problemas_ia()
        elif opcion == "5":
            simulador_sistema_experto()
        elif opcion == "6":
            quiz_conceptos_basicos()
        elif opcion == "7":
            print("\n🎉 ¡Gracias por explorar los conceptos básicos de IA!")
            print("📚 Próximo paso: ejemplo_02_historia_ia.py")
            break
        else:
            print("❌ Opción no válida. Por favor, elige entre 1-7.")

# ============================================================================
# 🚀 EJECUCIÓN
# ============================================================================

if __name__ == "__main__":
    # Configurar matplotlib para mostrar gráficos
    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['font.size'] = 10
    
    # Ejecutar programa principal
    main()

"""
📚 CONCEPTOS CLAVE APRENDIDOS:

✅ Definición de Inteligencia Artificial
✅ Diferencias entre IA, ML y DL
✅ Características de sistemas inteligentes
✅ Tipos de problemas que resuelve la IA
✅ Componentes básicos de sistemas expertos

🚀 PRÓXIMO PASO:
Ejecuta ejemplo_02_historia_ia.py para explorar la evolución histórica de la IA
"""