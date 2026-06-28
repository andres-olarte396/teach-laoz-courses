"""
📅 EJEMPLO 02: Historia y Evolución de la IA
==========================================

📚 OBJETIVOS DE APRENDIZAJE:
• Conocer los hitos históricos más importantes de la IA
• Comprender los ciclos de "inviernos" y "primaveras" de la IA
• Identificar a los pioneros y sus contribuciones
• Analizar las causas del boom actual de la IA

🎯 NIVEL: Básico - Contexto histórico
⏱️ TIEMPO ESTIMADO: 45-60 minutos
"""

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from datetime import datetime
import random

# ============================================================================
# 📅 PARTE 1: LÍNEA DE TIEMPO INTERACTIVA DE LA IA
# ============================================================================

def crear_timeline_ia():
    """
    Crea una línea de tiempo interactiva con los hitos más importantes de la IA
    """
    print("=" * 70)
    print("📅 LÍNEA DE TIEMPO DE LA INTELIGENCIA ARTIFICIAL")
    print("=" * 70)
    
    # Datos históricos organizados por eras
    hitos_historicos = {
        # Era de los Fundamentos (1940-1956)
        1943: "McCulloch & Pitts: Primer modelo de neurona artificial",
        1950: "Alan Turing: Test de Turing y 'Computing Machinery and Intelligence'",
        1956: "Conferencia de Dartmouth: Nacimiento oficial de la IA",
        
        # Primera Primavera (1956-1974)
        1957: "Newell & Simon: General Problem Solver (GPS)",
        1965: "DENDRAL: Primer sistema experto exitoso",
        1966: "ELIZA: Primer chatbot de la historia",
        1969: "SHAKEY: Primer robot móvil inteligente",
        
        # Primer Invierno (1974-1980)
        1973: "Lighthill Report: Crítica devastadora a la IA",
        1976: "Minsky & Papert: Limitaciones de perceptrones",
        
        # Segunda Primavera (1980-1987)
        1980: "R1/XCON: Sistema experto comercial exitoso",
        1982: "Proyecto Quinta Generación de Japón",
        1986: "Backpropagation: Renacimiento de redes neuronales",
        
        # Segundo Invierno (1987-1993)
        1987: "Colapso del mercado de máquinas Lisp",
        1990: "Crisis de sistemas expertos",
        
        # Renacimiento Silencioso (1993-2011)
        1997: "Deep Blue vence a Kasparov en ajedrez",
        2005: "Stanley gana DARPA Grand Challenge (vehículos autónomos)",
        2011: "Watson de IBM gana en Jeopardy!",
        
        # Boom Actual (2012-presente)
        2012: "AlexNet revoluciona visión por computadora",
        2016: "AlphaGo vence al campeón mundial de Go",
        2017: "Transformers: 'Attention Is All You Need'",
        2020: "GPT-3: Revolución en procesamiento de lenguaje",
        2022: "ChatGPT: IA accesible para el público general",
        2023: "GPT-4: Capacidades multimodales avanzadas"
    }
    
    # Crear visualización de timeline
    años = list(hitos_historicos.keys())
    eventos = list(hitos_historicos.values())
    
    # Definir eras con colores
    eras = {
        "Fundamentos (1940-1956)": {"color": "blue", "años": range(1940, 1957)},
        "1ª Primavera (1956-1974)": {"color": "green", "años": range(1956, 1975)},
        "1º Invierno (1974-1980)": {"color": "red", "años": range(1974, 1981)},
        "2ª Primavera (1980-1987)": {"color": "orange", "años": range(1980, 1988)},
        "2º Invierno (1987-1993)": {"color": "red", "años": range(1987, 1994)},
        "Renacimiento (1993-2011)": {"color": "purple", "años": range(1993, 2012)},
        "Boom Actual (2012-presente)": {"color": "gold", "años": range(2012, 2025)}
    }
    
    # Crear gráfico
    fig, ax = plt.subplots(1, 1, figsize=(16, 10))
    
    # Dibujar línea de tiempo base
    ax.plot([min(años), max(años)], [0, 0], 'k-', linewidth=2)
    
    # Añadir eventos
    for i, (año, evento) in enumerate(hitos_historicos.items()):
        # Determinar color según la era
        color = "black"
        for era, info in eras.items():
            if año in info["años"]:
                color = info["color"]
                break
        
        # Alternar posición de eventos (arriba/abajo)
        y_pos = 1 if i % 2 == 0 else -1
        
        # Dibujar línea vertical
        ax.plot([año, año], [0, y_pos * 0.8], color=color, linewidth=2)
        
        # Añadir punto
        ax.scatter(año, 0, color=color, s=100, zorder=3)
        
        # Añadir texto del evento
        ax.text(año, y_pos * 1.2, f"{año}\n{evento}", 
                ha='center', va='center' if y_pos > 0 else 'top',
                fontsize=8, bbox=dict(boxstyle="round,pad=0.3", 
                                     facecolor=color, alpha=0.3),
                rotation=0, wrap=True)
    
    # Configurar ejes
    ax.set_xlim(1940, 2025)
    ax.set_ylim(-2, 2)
    ax.set_xlabel('Año', fontsize=12, fontweight='bold')
    ax.set_title('📅 Historia de la Inteligencia Artificial: Hitos Principales', 
                fontsize=16, fontweight='bold', pad=20)
    ax.grid(True, alpha=0.3)
    ax.set_yticks([])
    
    # Añadir leyenda de eras
    legend_elements = []
    for era, info in eras.items():
        legend_elements.append(plt.Line2D([0], [0], color=info["color"], 
                                        lw=4, label=era))
    ax.legend(handles=legend_elements, loc='upper left', bbox_to_anchor=(0, 1))
    
    plt.tight_layout()
    plt.show()
    
    return hitos_historicos

def analizar_ciclos_ia():
    """
    Analiza los ciclos de primaveras e inviernos de la IA
    """
    print("\n" + "=" * 70)
    print("🔄 ANÁLISIS DE CICLOS: PRIMAVERAS E INVIERNOS DE LA IA")
    print("=" * 70)
    
    ciclos = {
        "1ª Primavera (1956-1974)": {
            "duración": 18,
            "caracteristicas": [
                "Optimismo extremo sobre el futuro de la IA",
                "Financiamiento abundante de gobiernos",
                "Desarrollo de primeros programas exitosos",
                "Predicciones ambiciosas (IA humana en 20 años)"
            ],
            "razones_fin": [
                "Limitaciones computacionales de la época",
                "Problemas más complejos de lo esperado",
                "Falta de datos suficientes",
                "Críticas académicas (Lighthill Report)"
            ]
        },
        "1º Invierno (1974-1980)": {
            "duración": 6,
            "impacto": [
                "Reducción drástica de financiamiento",
                "Investigadores cambian a otros campos",
                "Reputación de la IA como 'ciencia fallida'",
                "Enfoque en aplicaciones más prácticas"
            ]
        },
        "2ª Primavera (1980-1987)": {
            "duración": 7,
            "caracteristicas": [
                "Era de los sistemas expertos",
                "Primeras aplicaciones comerciales exitosas",
                "Inversión de empresas japonesas",
                "Hardware especializado (máquinas Lisp)"
            ],
            "razones_fin": [
                "Sistemas expertos demasiado frágiles",
                "Hardware especializado obsoleto",
                "Mantenimiento costoso y complejo",
                "Llegada de PCs más potentes"
            ]
        },
        "2º Invierno (1987-1993)": {
            "duración": 6,
            "impacto": [
                "Colapso del mercado de IA comercial",
                "Abandono de hardware especializado",
                "Cambio hacia métodos estadísticos",
                "Término 'IA' evitado en propuestas"
            ]
        }
    }
    
    # Mostrar análisis detallado
    for ciclo, info in ciclos.items():
        print(f"\n🌡️ {ciclo}")
        print(f"   Duración: {info.get('duración', 'N/A')} años")
        
        if 'caracteristicas' in info:
            print("   📈 Características:")
            for caracteristica in info['caracteristicas']:
                print(f"      • {caracteristica}")
        
        if 'razones_fin' in info:
            print("   📉 Razones del declive:")
            for razon in info['razones_fin']:
                print(f"      • {razon}")
        
        if 'impacto' in info:
            print("   ❄️ Impacto:")
            for impacto in info['impacto']:
                print(f"      • {impacto}")
    
    # Visualizar duración de ciclos
    nombres_ciclos = []
    duraciones = []
    colores = []
    
    for ciclo, info in ciclos.items():
        if 'duración' in info:
            nombres_ciclos.append(ciclo.split(' (')[0])
            duraciones.append(info['duración'])
            if 'Primavera' in ciclo:
                colores.append('green')
            else:
                colores.append('red')
    
    plt.figure(figsize=(12, 6))
    bars = plt.bar(nombres_ciclos, duraciones, color=colores, alpha=0.7)
    
    # Añadir valores en las barras
    for bar, duracion in zip(bars, duraciones):
        plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{duracion} años', ha='center', va='bottom', fontweight='bold')
    
    plt.title('🔄 Duración de Ciclos Históricos de la IA', fontsize=14, fontweight='bold')
    plt.ylabel('Duración (años)')
    plt.xlabel('Ciclos Históricos')
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.show()

# ============================================================================
# 👥 PARTE 2: PIONEROS DE LA IA
# ============================================================================

def presentar_pioneros_ia():
    """
    Presenta a los pioneros más importantes de la IA y sus contribuciones
    """
    print("\n" + "=" * 70)
    print("👥 PIONEROS DE LA INTELIGENCIA ARTIFICIAL")
    print("=" * 70)
    
    pioneros = {
        "Alan Turing (1912-1954)": {
            "contribuciones": [
                "Test de Turing (1950) - criterio de inteligencia",
                "Máquina de Turing - modelo de computación",
                "Trabajo en códigos durante WWII",
                "Visión sobre aprendizaje automático"
            ],
            "frase": "Una computadora merecería ser llamada inteligente si pudiera engañar a un humano haciéndole creer que es humana",
            "legado": "Padre teórico de la IA y la computación"
        },
        "John McCarthy (1927-2011)": {
            "contribuciones": [
                "Acuñó el término 'Inteligencia Artificial' (1956)",
                "Organizador de la Conferencia de Dartmouth",
                "Creador del lenguaje LISP",
                "Concepto de time-sharing en computación"
            ],
            "frase": "La IA es la ciencia e ingeniería de hacer máquinas inteligentes",
            "legado": "Padre fundador y evangelista de la IA"
        },
        "Marvin Minsky (1927-2016)": {
            "contribuciones": [
                "Fundador del MIT AI Laboratory",
                "Investigación en redes neuronales",
                "Teoría de marcos (frames) para representación",
                "Crítica constructiva de limitaciones de IA"
            ],
            "frase": "La inteligencia artificial es la ciencia de hacer que las máquinas hagan cosas que requerirían inteligencia si fueran hechas por humanos",
            "legado": "Visionario y crítico constructivo de la IA"
        },
        "Herbert Simon (1916-2001)": {
            "contribuciones": [
                "Logic Theorist - primer programa de IA",
                "General Problem Solver (GPS)",
                "Nobel de Economía por teoría de decisiones",
                "Concepto de 'satisficing' vs optimización"
            ],
            "frase": "Las máquinas serán capaces, dentro de veinte años, de hacer cualquier trabajo que un hombre pueda hacer",
            "legado": "Pionero en solución de problemas con IA"
        },
        "Geoffrey Hinton (1947-presente)": {
            "contribuciones": [
                "Redescubrimiento del backpropagation",
                "Redes neuronales convolucionales",
                "Deep learning y neural networks",
                "Boltzmann machines y autoencoders"
            ],
            "frase": "El cerebro tiene alrededor de 10^14 sinapsis y solo vivimos alrededor de 10^9 segundos. Así que tenemos muchas más sinapsis que segundos",
            "legado": "Padrino del Deep Learning moderno"
        },
        "Yann LeCun (1960-presente)": {
            "contribuciones": [
                "Redes neuronales convolucionales (CNN)",
                "Reconocimiento de dígitos escritos",
                "Aprendizaje auto-supervisado",
                "Chief AI Scientist en Meta/Facebook"
            ],
            "frase": "La inteligencia artificial es la nueva electricidad",
            "legado": "Pionero en visión por computadora con IA"
        }
    }
    
    # Mostrar información de cada pionero
    for nombre, info in pioneros.items():
        print(f"\n🧠 {nombre}")
        print(f"   📜 Frase célebre: \"{info['frase']}\"")
        print(f"   🏆 Legado: {info['legado']}")
        print("   💡 Contribuciones principales:")
        for contribucion in info['contribuciones']:
            print(f"      • {contribucion}")
    
    # Crear visualización de eras de pioneros
    nombres = list(pioneros.keys())
    # Extraer años de nacimiento para crear timeline
    años_nacimiento = [1912, 1927, 1927, 1916, 1947, 1960]
    
    plt.figure(figsize=(14, 8))
    
    # Crear scatter plot con años
    scatter = plt.scatter(años_nacimiento, range(len(nombres)), 
                         s=[200 if año < 1950 else 150 for año in años_nacimiento],
                         c=['blue' if año < 1930 else 'green' if año < 1950 else 'red' 
                           for año in años_nacimiento],
                         alpha=0.7)
    
    # Añadir nombres
    for i, (nombre, año) in enumerate(zip(nombres, años_nacimiento)):
        plt.annotate(nombre.split(' (')[0], (año, i), 
                    xytext=(10, 0), textcoords='offset points',
                    fontsize=10, va='center')
    
    plt.yticks(range(len(nombres)), [nombre.split(' (')[0] for nombre in nombres])
    plt.xlabel('Año de Nacimiento')
    plt.title('👥 Línea de Tiempo de Pioneros de la IA', fontsize=14, fontweight='bold')
    plt.grid(True, alpha=0.3)
    
    # Añadir leyenda de generaciones
    from matplotlib.lines import Line2D
    legend_elements = [
        Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', 
               markersize=10, label='Fundadores (pre-1930)'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='green', 
               markersize=10, label='Primera Generación (1930-1950)'),
        Line2D([0], [0], marker='o', color='w', markerfacecolor='red', 
               markersize=10, label='Era Moderna (post-1950)')
    ]
    plt.legend(handles=legend_elements, loc='upper left')
    
    plt.tight_layout()
    plt.show()

# ============================================================================
# 💰 PARTE 3: ANÁLISIS ECONÓMICO DE LA IA
# ============================================================================

def analizar_impacto_economico():
    """
    Analiza el impacto económico y la inversión en IA a lo largo del tiempo
    """
    print("\n" + "=" * 70)
    print("💰 IMPACTO ECONÓMICO DE LA IA A TRAVÉS DEL TIEMPO")
    print("=" * 70)
    
    # Datos simulados pero realistas de inversión en IA
    años = list(range(1960, 2024, 5))
    inversión_gobierno = [10, 50, 200, 100, 50, 80, 150, 300, 800, 2000, 5000, 12000, 25000]
    inversión_privada = [5, 20, 100, 300, 200, 400, 800, 2000, 8000, 25000, 75000, 180000, 400000]
    
    # Crear gráfico de inversión
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
    # Gráfico 1: Inversión en IA
    ax1.plot(años, inversión_gobierno, 'b-o', label='Inversión Gubernamental', linewidth=2)
    ax1.plot(años, inversión_privada, 'r-s', label='Inversión Privada', linewidth=2)
    ax1.set_ylabel('Inversión (Millones USD)')
    ax1.set_title('💰 Inversión en IA: Gobierno vs Sector Privado', fontsize=14, fontweight='bold')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.set_yscale('log')  # Escala logarítmica para mejor visualización
    
    # Marcar inviernos de IA
    ax1.axvspan(1974, 1980, alpha=0.3, color='lightcoral', label='1º Invierno IA')
    ax1.axvspan(1987, 1993, alpha=0.3, color='lightcoral', label='2º Invierno IA')
    
    # Gráfico 2: Hitos de financiamiento
    eventos_financiamiento = {
        1958: "DARPA fundada - primeros fondos para IA",
        1973: "Lighthill Report - recortes masivos UK",
        1982: "Japón invierte $850M en 5ª Generación",
        1987: "Colapso mercado máquinas Lisp",
        2010: "Inicio inversión masiva en Deep Learning",
        2016: "Inversión VC en IA supera $5B anuales",
        2023: "ChatGPT dispara inversión a $25B+"
    }
    
    # Mostrar datos económicos actuales
    print("\n📊 DATOS ECONÓMICOS ACTUALES (2023):")
    print(f"   💰 Mercado global de IA: $150 mil millones")
    print(f"   📈 Crecimiento anual: 37% CAGR")
    print(f"   🏢 Empresas de IA: 50,000+ startups")
    print(f"   👨‍💼 Empleos en IA: 2.3 millones de puestos")
    print(f"   🎓 Inversión en educación IA: $2.8 mil millones")
    
    # Crear barras para eventos importantes
    eventos_años = list(eventos_financiamiento.keys())
    eventos_valores = [100, 50, 850, 200, 5000, 15000, 25000]  # Valores aproximados
    
    ax2.bar(eventos_años, eventos_valores, alpha=0.6, color='green')
    ax2.set_ylabel('Impacto Financiero (Millones USD)')
    ax2.set_xlabel('Año')
    ax2.set_title('🏛️ Hitos Importantes de Financiamiento en IA', fontsize=14, fontweight='bold')
    ax2.grid(True, alpha=0.3)
    
    # Rotar etiquetas del eje x
    plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')
    
    plt.tight_layout()
    plt.show()
    
    # Proyección futura
    print("\n🔮 PROYECCIONES FUTURAS:")
    print("   2025: Mercado de $390 mil millones")
    print("   2030: Mercado de $1.35 billones")
    print("   2035: IA contribuirá $13 billones al PIB global")

# ============================================================================
# 🎯 PARTE 4: SIMULADOR DE DECISIONES HISTÓRICAS
# ============================================================================

def simulador_decisiones_historicas():
    """
    Simulador interactivo de decisiones históricas importantes en IA
    """
    print("\n" + "=" * 70)
    print("🎯 SIMULADOR: DECISIONES HISTÓRICAS DE LA IA")
    print("=" * 70)
    print("¿Qué habría pasado si se hubieran tomado decisiones diferentes?")
    
    escenarios = [
        {
            "año": 1973,
            "situación": "Eres un político británico revisando el Lighthill Report que critica duramente la IA.",
            "pregunta": "¿Qué decides hacer con el financiamiento de IA?",
            "opciones": {
                "A": "Cortar todo el financiamiento (decisión histórica real)",
                "B": "Reducir financiamiento pero mantener investigación básica",
                "C": "Mantener financiamiento e intensificar investigación"
            },
            "consecuencias": {
                "A": "Primer invierno de IA: Reino Unido pierde liderazgo tecnológico por décadas",
                "B": "Desarrollo más lento pero sostenido: Reino Unido mantiene competitividad",
                "C": "Posible liderazgo británico en IA: podría haber evitado el primer invierno"
            }
        },
        {
            "año": 1987,
            "situación": "Eres CEO de una empresa de máquinas Lisp viendo llegar las PCs más potentes.",
            "pregunta": "¿Cuál es tu estrategia?",
            "opciones": {
                "A": "Mantener enfoque en hardware especializado (decisión histórica)",
                "B": "Pivotar hacia software para PCs estándar",
                "C": "Desarrollar híbrido: hardware+software optimizado"
            },
            "consecuencias": {
                "A": "Colapso del negocio: contribuye al segundo invierno de IA",
                "B": "Supervivencia: empresa se adapta y prospera en nueva era",
                "C": "Liderazgo tecnológico: posible dominio del mercado IA"
            }
        },
        {
            "año": 2010,
            "situación": "Eres un investigador con una idea sobre 'deep learning' pero necesitas financiamiento.",
            "pregunta": "¿Cómo presentas tu propuesta?",
            "opciones": {
                "A": "Enfocarse en aplicaciones prácticas inmediatas",
                "B": "Prometer revolución completa de la IA (riesgoso)",
                "C": "Presentar como evolución natural de métodos existentes"
            },
            "consecuencias": {
                "A": "Financiamiento limitado: progreso más lento",
                "B": "Gran financiamiento pero altas expectativas: riesgo de nuevo invierno",
                "C": "Financiamiento sostenido: desarrollo equilibrado y duradero"
            }
        }
    ]
    
    puntuacion_total = 0
    
    for i, escenario in enumerate(escenarios, 1):
        print(f"\n🎭 ESCENARIO {i}: AÑO {escenario['año']}")
        print(f"📖 Situación: {escenario['situación']}")
        print(f"❓ {escenario['pregunta']}")
        
        for opcion, descripción in escenario['opciones'].items():
            print(f"   {opcion}) {descripción}")
        
        respuesta = input("\n¿Cuál es tu decisión? (A/B/C): ").upper().strip()
        
        if respuesta in escenario['consecuencias']:
            print(f"\n📊 CONSECUENCIA: {escenario['consecuencias'][respuesta]}")
            
            # Sistema de puntuación simple
            if respuesta == "A":
                puntos = 1  # Decisión conservadora/histórica
            elif respuesta == "B":
                puntos = 2  # Decisión moderada
            else:
                puntos = 3  # Decisión innovadora
            
            puntuacion_total += puntos
            print(f"🎯 Puntos obtenidos: {puntos}/3")
        else:
            print("❌ Opción no válida.")
    
    # Evaluar puntuación final
    print(f"\n🏆 PUNTUACIÓN FINAL: {puntuacion_total}/{len(escenarios)*3}")
    
    if puntuacion_total >= 8:
        print("🎉 ¡Visionario! Tus decisiones habrían acelerado el desarrollo de la IA")
    elif puntuacion_total >= 6:
        print("👍 ¡Equilibrado! Tus decisiones habrían mantenido un progreso sostenido")
    else:
        print("📚 Conservador: Tus decisiones siguieron el curso histórico")

# ============================================================================
# 🎓 PARTE 5: QUIZ HISTÓRICO INTERACTIVO
# ============================================================================

def quiz_historia_ia():
    """
    Quiz interactivo sobre la historia de la IA
    """
    print("\n" + "=" * 70)
    print("🎓 QUIZ: HISTORIA DE LA INTELIGENCIA ARTIFICIAL")
    print("=" * 70)
    
    preguntas = [
        {
            "pregunta": "¿En qué año se considera que nació oficialmente la IA?",
            "opciones": ["A) 1943", "B) 1950", "C) 1956", "D) 1969"],
            "respuesta": "C",
            "explicacion": "1956 fue el año de la Conferencia de Dartmouth, donde se acuñó el término 'Inteligencia Artificial'."
        },
        {
            "pregunta": "¿Quién acuñó el término 'Inteligencia Artificial'?",
            "opciones": ["A) Alan Turing", "B) John McCarthy", "C) Marvin Minsky", "D) Herbert Simon"],
            "respuesta": "B",
            "explicacion": "John McCarthy acuñó el término en la propuesta para la Conferencia de Dartmouth de 1956."
        },
        {
            "pregunta": "¿Cuántos 'inviernos de la IA' ha habido históricamente?",
            "opciones": ["A) Uno", "B) Dos", "C) Tres", "D) Ninguno"],
            "respuesta": "B",
            "explicacion": "Ha habido dos inviernos principales: 1974-1980 y 1987-1993."
        },
        {
            "pregunta": "¿Qué programa venció a Garry Kasparov en ajedrez en 1997?",
            "opciones": ["A) Deep Thought", "B) Deep Blue", "C) AlphaZero", "D) Stockfish"],
            "respuesta": "B",
            "explicacion": "Deep Blue de IBM venció a Kasparov en 1997, marcando un hito histórico."
        },
        {
            "pregunta": "¿Qué evento marcó el inicio del boom actual de IA en 2012?",
            "opciones": ["A) Creación de Siri", "B) Victoria de AlexNet en ImageNet", "C) Lanzamiento de Watson", "D) IPO de Facebook"],
            "respuesta": "B",
            "explicacion": "AlexNet revolucionó la visión por computadora y marcó el inicio de la era del deep learning."
        }
    ]
    
    puntuacion = 0
    for i, pregunta in enumerate(preguntas, 1):
        print(f"\n❓ Pregunta {i}: {pregunta['pregunta']}")
        for opcion in pregunta['opciones']:
            print(f"   {opcion}")
        
        respuesta = input("\nTu respuesta: ").upper().strip()
        
        if respuesta == pregunta['respuesta']:
            print("✅ ¡Correcto!")
            puntuacion += 1
        else:
            print(f"❌ Incorrecto. La respuesta correcta es {pregunta['respuesta']}")
        
        print(f"💡 {pregunta['explicacion']}")
    
    print(f"\n🏆 PUNTUACIÓN FINAL: {puntuacion}/{len(preguntas)} ({puntuacion/len(preguntas)*100:.0f}%)")
    
    if puntuacion == len(preguntas):
        print("🎉 ¡Historiador de IA! Conoces perfectamente la evolución de la IA")
    elif puntuacion >= len(preguntas) * 0.8:
        print("👍 ¡Muy bien! Tienes sólidos conocimientos históricos")
    elif puntuacion >= len(preguntas) * 0.6:
        print("📖 Bien, pero puedes mejorar tu conocimiento histórico")
    else:
        print("📚 Necesitas repasar más la historia de la IA")

# ============================================================================
# 🎯 FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Función principal que ejecuta todo el ejemplo histórico
    """
    print("📅 EJEMPLO 02: HISTORIA Y EVOLUCIÓN DE LA INTELIGENCIA ARTIFICIAL")
    print("=" * 80)
    
    while True:
        print("\n📋 MENÚ HISTÓRICO:")
        print("1. 📅 Ver línea de tiempo interactiva")
        print("2. 🔄 Analizar ciclos de primaveras e inviernos")
        print("3. 👥 Conocer a los pioneros de la IA")
        print("4. 💰 Impacto económico a través del tiempo")
        print("5. 🎯 Simulador de decisiones históricas")
        print("6. 🎓 Quiz de historia de la IA")
        print("7. 🚪 Salir")
        
        opcion = input("\n¿Qué período histórico te interesa explorar? (1-7): ").strip()
        
        if opcion == "1":
            crear_timeline_ia()
        elif opcion == "2":
            analizar_ciclos_ia()
        elif opcion == "3":
            presentar_pioneros_ia()
        elif opcion == "4":
            analizar_impacto_economico()
        elif opcion == "5":
            simulador_decisiones_historicas()
        elif opcion == "6":
            quiz_historia_ia()
        elif opcion == "7":
            print("\n🎉 ¡Has viajado a través de la historia de la IA!")
            print("📚 Próximo paso: ejemplo_03_tipos_ia.py")
            break
        else:
            print("❌ Opción no válida. Por favor, elige entre 1-7.")

# ============================================================================
# 🚀 EJECUCIÓN
# ============================================================================

if __name__ == "__main__":
    # Configurar matplotlib
    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 10
    
    # Ejecutar programa principal
    main()

"""
📚 CONCEPTOS HISTÓRICOS APRENDIDOS:

✅ Hitos importantes en la evolución de la IA
✅ Ciclos de primaveras e inviernos de la IA
✅ Pioneros y sus contribuciones fundamentales
✅ Impacto económico y de financiamiento
✅ Lecciones aprendidas de decisiones históricas

🔍 PATRONES IDENTIFICADOS:
• La IA progresa en ciclos de optimismo y realismo
• Las expectativas exageradas conducen a desilusiones
• La investigación básica es crucial para avances futuros
• La convergencia de factores (datos+algoritmos+computación) impulsa el progreso

🚀 PRÓXIMO PASO:
Ejecuta ejemplo_03_tipos_ia.py para clasificar diferentes tipos de sistemas de IA
"""