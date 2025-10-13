"""
🎯 EJEMPLO 03: Tipos de Inteligencia Artificial
=============================================

📚 OBJETIVOS DE APRENDIZAJE:
• Distinguir entre IA débil (narrow) y IA fuerte (general)
• Clasificar sistemas según niveles de capacidad
• Identificar enfoques técnicos (simbólico, conexionista, etc.)
• Evaluar aplicaciones reales según su tipo de IA
• Comprender las tendencias hacia sistemas híbridos

🎯 NIVEL: Básico-Intermedio - Clasificación de sistemas
⏱️ TIEMPO ESTIMADO: 60-75 minutos
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from collections import Counter
import seaborn as sns

# ============================================================================
# 🧠 PARTE 1: IA DÉBIL VS IA FUERTE
# ============================================================================

def comparar_ia_debil_fuerte():
    """
    Compara y contrasta IA débil (narrow) con IA fuerte (general)
    """
    print("=" * 70)
    print("🧠 IA DÉBIL (NARROW) vs IA FUERTE (GENERAL)")
    print("=" * 70)
    
    comparacion = {
        "Característica": [
            "Especialización",
            "Transferencia de conocimiento",
            "Consciencia",
            "Creatividad genuina",
            "Comprensión contextual",
            "Adaptabilidad",
            "Estado actual",
            "Ejemplos típicos"
        ],
        "IA Débil (Narrow)": [
            "Excelente en UNA tarea específica",
            "Limitada o nula",
            "No tiene consciencia",
            "Imitación de patrones",
            "Contexto muy específico",
            "Baja, requiere reentrenamiento",
            "Dominante en 2024",
            "ChatGPT, AlphaGo, Siri"
        ],
        "IA Fuerte (General)": [
            "Competente en MÚLTIPLES dominios",
            "Excelente entre dominios",
            "Posible autoconciencia",
            "Creatividad original",
            "Comprensión amplia y flexible",
            "Alta, aprendizaje continuo",
            "En investigación",
            "Hipotético: AGI, ASI"
        ]
    }
    
    # Mostrar tabla comparativa
    df = pd.DataFrame(comparacion)
    print(df.to_string(index=False))
    
    # Crear visualización
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Gráfico de capacidades
    capacidades = ['Especialización', 'Generalización', 'Transferencia', 
                  'Creatividad', 'Consciencia', 'Adaptabilidad']
    
    ia_debil_scores = [9, 2, 1, 3, 0, 2]    # Puntuaciones de 0-10
    ia_fuerte_scores = [7, 9, 9, 8, 7, 9]   # Puntuaciones hipotéticas
    
    x = np.arange(len(capacidades))
    width = 0.35
    
    ax1.bar(x - width/2, ia_debil_scores, width, label='IA Débil', color='lightblue', alpha=0.8)
    ax1.bar(x + width/2, ia_fuerte_scores, width, label='IA Fuerte', color='orange', alpha=0.8)
    
    ax1.set_ylabel('Nivel de Capacidad (0-10)')
    ax1.set_title('🎯 Comparación de Capacidades: IA Débil vs IA Fuerte')
    ax1.set_xticks(x)
    ax1.set_xticklabels(capacidades, rotation=45, ha='right')
    ax1.legend()
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Gráfico circular de distribución actual
    tipos_actuales = ['IA Débil\n(Sistemas Actuales)', 'IA Fuerte\n(Investigación)', 'Sistemas Híbridos\n(Emergentes)']
    distribucion = [85, 5, 10]  # Porcentajes aproximados
    colores = ['lightblue', 'orange', 'lightgreen']
    
    ax2.pie(distribucion, labels=tipos_actuales, autopct='%1.1f%%', 
            colors=colores, startangle=90, explode=(0.1, 0.1, 0.1))
    ax2.set_title('📊 Distribución de Tipos de IA en 2024')
    
    plt.tight_layout()
    plt.show()

def evaluar_sistemas_existentes():
    """
    Evalúa sistemas de IA existentes según criterios de débil/fuerte
    """
    print("\n" + "=" * 70)
    print("🔍 EVALUACIÓN DE SISTEMAS DE IA EXISTENTES")
    print("=" * 70)
    
    sistemas = {
        "ChatGPT": {
            "tipo": "IA Débil Avanzada",
            "especialización": 9,  # Excelente en texto
            "generalización": 6,   # Múltiples tareas de texto
            "transferencia": 4,    # Limitada fuera de texto
            "creatividad": 6,      # Genera contenido original
            "consciencia": 0,      # Sin autoconciencia
            "ejemplos_uso": ["Escritura", "Programación", "Análisis", "Conversación"]
        },
        "AlphaGo": {
            "tipo": "IA Débil Especializada",
            "especialización": 10, # Perfecto en Go
            "generalización": 1,   # Solo juega Go
            "transferencia": 0,    # No transfiere a otros juegos
            "creatividad": 8,      # Movimientos creativos
            "consciencia": 0,      # Sin autoconciencia
            "ejemplos_uso": ["Juego de Go únicamente"]
        },
        "Tesla Autopilot": {
            "tipo": "IA Débil Contextual",
            "especialización": 8,  # Muy bueno conduciendo
            "generalización": 3,   # Solo conducción
            "transferencia": 2,    # No se aplica a otros vehículos fácilmente
            "creatividad": 5,      # Soluciones de navegación
            "consciencia": 0,      # Sin autoconciencia
            "ejemplos_uso": ["Conducción autónoma", "Estacionamiento", "Navegación"]
        },
        "Siri/Alexa": {
            "tipo": "IA Débil Multimodal",
            "especialización": 6,  # Bueno en tareas específicas
            "generalización": 5,   # Varias tareas domésticas
            "transferencia": 3,    # Limitada fuera del hogar
            "creatividad": 3,      # Respuestas programadas
            "consciencia": 0,      # Sin autoconciencia
            "ejemplos_uso": ["Control domótico", "Música", "Información", "Recordatorios"]
        },
        "GPT-4V": {
            "tipo": "IA Débil Multimodal Avanzada",
            "especialización": 8,  # Excelente en texto+imagen
            "generalización": 7,   # Múltiples modalidades
            "transferencia": 5,    # Mejor transferencia
            "creatividad": 7,      # Muy creativo
            "consciencia": 0,      # Sin autoconciencia
            "ejemplos_uso": ["Análisis de imágenes", "Escritura", "Código", "Educación"]
        }
    }
    
    # Crear DataFrame para análisis
    data = []
    for sistema, props in sistemas.items():
        fila = [sistema, props["tipo"]] + [props[key] for key in 
               ["especialización", "generalización", "transferencia", "creatividad", "consciencia"]]
        data.append(fila)
    
    columnas = ["Sistema", "Tipo", "Especialización", "Generalización", 
               "Transferencia", "Creatividad", "Consciencia"]
    df_sistemas = pd.DataFrame(data, columns=columnas)
    
    print("📊 PUNTUACIÓN DE SISTEMAS (0-10):")
    print(df_sistemas.to_string(index=False))
    
    # Visualización con heatmap
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
    
    # Heatmap de capacidades
    heatmap_data = df_sistemas.iloc[:, 2:].set_index(df_sistemas['Sistema'])
    sns.heatmap(heatmap_data, annot=True, cmap='RdYlGn', ax=ax1, 
                cbar_kws={'label': 'Nivel de Capacidad'})
    ax1.set_title('🌡️ Mapa de Calor: Capacidades por Sistema de IA')
    ax1.set_ylabel('Sistemas de IA')
    
    # Gráfico de barras apiladas
    sistemas_nombres = df_sistemas['Sistema']
    capacidades_tipos = ['Especialización', 'Generalización', 'Transferencia', 'Creatividad']
    
    bottom = np.zeros(len(sistemas_nombres))
    colores = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    
    for i, capacidad in enumerate(capacidades_tipos):
        valores = df_sistemas[capacidad]
        ax2.bar(sistemas_nombres, valores, bottom=bottom, 
               label=capacidad, color=colores[i], alpha=0.8)
        bottom += valores
    
    ax2.set_title('📊 Perfil de Capacidades por Sistema')
    ax2.set_ylabel('Puntuación Acumulada')
    ax2.legend(loc='upper right')
    ax2.tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.show()
    
    # Análisis de tendencias
    print("\n🔍 ANÁLISIS DE TENDENCIAS:")
    print("   • Los sistemas más recientes (GPT-4V) muestran mayor generalización")
    print("   • Ningún sistema actual tiene consciencia")
    print("   • La especialización sigue siendo la fortaleza principal")
    print("   • La transferencia de conocimiento es el mayor desafío")

# ============================================================================
# 📊 PARTE 2: NIVELES DE CAPACIDAD DE IA
# ============================================================================

def clasificar_niveles_capacidad():
    """
    Clasifica sistemas de IA según su nivel de capacidad
    """
    print("\n" + "=" * 70)
    print("📊 NIVELES DE CAPACIDAD DE IA")
    print("=" * 70)
    
    niveles = {
        "Nivel 0: Sin IA": {
            "descripcion": "Sistemas determinísticos tradicionales",
            "caracteristicas": ["Reglas fijas", "Sin aprendizaje", "Comportamiento predecible"],
            "ejemplos": ["Calculadoras", "Semáforos tradicionales", "Software convencional"],
            "color": "gray"
        },
        "Nivel 1: IA Asistiva": {
            "descripcion": "Ayuda a humanos en tareas específicas",
            "caracteristicas": ["Sugiere opciones", "Mejora eficiencia", "Humano toma decisiones"],
            "ejemplos": ["Autocorrección", "Sugerencias de búsqueda", "Recomendaciones básicas"],
            "color": "lightblue"
        },
        "Nivel 2: IA Automática": {
            "descripcion": "Realiza tareas completas sin supervisión constante",
            "caracteristicas": ["Automatización completa", "Decisiones independientes", "Supervisión ocasional"],
            "ejemplos": ["Filtros de spam", "Sistemas de recomendación", "Trading algorítmico"],
            "color": "orange"
        },
        "Nivel 3: IA Aumentativa": {
            "descripcion": "Potencia significativamente las capacidades humanas",
            "caracteristicas": ["Colaboración activa", "Insights profundos", "Capacidades sobrehumanas"],
            "ejemplos": ["GitHub Copilot", "Asistentes médicos IA", "Análisis de datos avanzado"],
            "color": "green"
        },
        "Nivel 4: IA Autónoma": {
            "descripcion": "Toma decisiones complejas independientemente",
            "caracteristicas": ["Autonomía completa", "Responsabilidad delegada", "Mínima supervisión"],
            "ejemplos": ["Vehículos autónomos L5", "Robots de servicio", "Gestión automatizada"],
            "color": "red"
        },
        "Nivel 5: IA Superinteligente": {
            "descripcion": "Supera inteligencia humana en todos los dominios",
            "caracteristicas": ["Capacidades sobrehumanas", "Auto-mejora", "Impacto civilizacional"],
            "ejemplos": ["Hipotético", "En investigación", "Futuro incierto"],
            "color": "purple"
        }
    }
    
    # Mostrar información detallada
    for nivel, info in niveles.items():
        print(f"\n🎯 {nivel}")
        print(f"   📖 {info['descripcion']}")
        print("   🔍 Características:")
        for caracteristica in info['caracteristicas']:
            print(f"      • {caracteristica}")
        print("   💡 Ejemplos:")
        for ejemplo in info['ejemplos']:
            print(f"      • {ejemplo}")
    
    # Crear visualización de pirámide de niveles
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Pirámide de adopción actual
    niveles_nombres = list(niveles.keys())
    # Estimación de distribución actual (porcentajes)
    adopcion_actual = [15, 35, 30, 15, 4, 1]  # Nivel 0 a 5
    colores = [info['color'] for info in niveles.values()]
    
    # Crear pirámide invertida
    y_positions = range(len(niveles_nombres))
    bars1 = ax1.barh(y_positions, adopcion_actual, color=colores, alpha=0.7)
    
    # Añadir valores en las barras
    for i, (bar, valor) in enumerate(zip(bars1, adopcion_actual)):
        ax1.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                f'{valor}%', va='center', fontweight='bold')
    
    ax1.set_yticks(y_positions)
    ax1.set_yticklabels([nivel.split(':')[0] for nivel in niveles_nombres])
    ax1.set_xlabel('Porcentaje de Adopción Actual (%)')
    ax1.set_title('📊 Distribución Actual de Niveles de IA')
    ax1.grid(True, alpha=0.3, axis='x')
    
    # Proyección futura (2030)
    adopcion_futura = [5, 20, 35, 25, 12, 3]  # Proyección optimista
    bars2 = ax2.barh(y_positions, adopcion_futura, color=colores, alpha=0.7)
    
    # Añadir valores en las barras
    for i, (bar, valor) in enumerate(zip(bars2, adopcion_futura)):
        ax2.text(bar.get_width() + 1, bar.get_y() + bar.get_height()/2,
                f'{valor}%', va='center', fontweight='bold')
    
    ax2.set_yticks(y_positions)
    ax2.set_yticklabels([nivel.split(':')[0] for nivel in niveles_nombres])
    ax2.set_xlabel('Proyección de Adopción 2030 (%)')
    ax2.set_title('🔮 Proyección de Niveles de IA para 2030')
    ax2.grid(True, alpha=0.3, axis='x')
    
    plt.tight_layout()
    plt.show()

def simulador_clasificador_niveles():
    """
    Simulador interactivo para clasificar sistemas según su nivel de IA
    """
    print("\n" + "=" * 70)
    print("🎮 SIMULADOR: CLASIFICADOR DE NIVELES DE IA")
    print("=" * 70)
    
    sistemas_prueba = [
        {
            "nombre": "Sistema de recomendación de Netflix",
            "descripcion": "Analiza tu historial y recomienda películas automáticamente",
            "nivel_correcto": 2,
            "explicacion": "Automatiza completamente la tarea de recomendación sin supervisión constante"
        },
        {
            "nombre": "GitHub Copilot",
            "descripcion": "Asiste a programadores sugiriendo código en tiempo real",
            "nivel_correcto": 3,
            "explicacion": "Aumenta significativamente las capacidades del programador, colaboración activa"
        },
        {
            "nombre": "Calculadora científica",
            "descripcion": "Realiza cálculos complejos siguiendo reglas matemáticas fijas",
            "nivel_correcto": 0,
            "explicacion": "Sistema determinístico sin aprendizaje ni adaptación"
        },
        {
            "nombre": "Waymo (vehículo autónomo L4)",
            "descripcion": "Conduce autónomamente en ciudades específicas sin conductor",
            "nivel_correcto": 4,
            "explicacion": "Toma decisiones complejas independientemente con mínima supervisión"
        },
        {
            "nombre": "Autocorrector de teléfono",
            "descripcion": "Sugiere correcciones mientras escribes",
            "nivel_correcto": 1,
            "explicacion": "Asiste al usuario sugiriendo opciones, pero el humano decide"
        }
    ]
    
    puntuacion = 0
    for i, sistema in enumerate(sistemas_prueba, 1):
        print(f"\n🎯 SISTEMA {i}: {sistema['nombre']}")
        print(f"📖 Descripción: {sistema['descripcion']}")
        print("\n¿A qué nivel de IA corresponde?")
        print("0) Sin IA")
        print("1) IA Asistiva") 
        print("2) IA Automática")
        print("3) IA Aumentativa")
        print("4) IA Autónoma")
        print("5) IA Superinteligente")
        
        try:
            respuesta = int(input("\nTu clasificación (0-5): "))
            
            if respuesta == sistema['nivel_correcto']:
                print("✅ ¡Correcto!")
                puntuacion += 1
            else:
                print(f"❌ Incorrecto. El nivel correcto es {sistema['nivel_correcto']}")
            
            print(f"💡 Explicación: {sistema['explicacion']}")
            
        except ValueError:
            print("❌ Por favor, introduce un número del 0 al 5")
    
    print(f"\n🏆 PUNTUACIÓN FINAL: {puntuacion}/{len(sistemas_prueba)}")
    
    if puntuacion == len(sistemas_prueba):
        print("🎉 ¡Experto en clasificación! Dominas perfectamente los niveles de IA")
    elif puntuacion >= len(sistemas_prueba) * 0.8:
        print("👍 ¡Muy bien! Tienes buen conocimiento de los niveles")
    else:
        print("📚 Necesitas practicar más la clasificación de niveles")

# ============================================================================
# 🔧 PARTE 3: ENFOQUES TÉCNICOS DE IA
# ============================================================================

def explorar_enfoques_tecnicos():
    """
    Explora diferentes enfoques técnicos para implementar IA
    """
    print("\n" + "=" * 70)
    print("🔧 ENFOQUES TÉCNICOS DE INTELIGENCIA ARTIFICIAL")
    print("=" * 70)
    
    enfoques = {
        "🧮 IA Simbólica": {
            "principio": "Representación explícita del conocimiento con símbolos y reglas",
            "fortalezas": ["Explicabilidad", "Precisión lógica", "Razonamiento claro"],
            "debilidades": ["Rigidez", "Dificultad con incertidumbre", "Escalabilidad limitada"],
            "ejemplos": ["Sistemas expertos", "Prolog", "Planificadores"],
            "mejor_para": "Dominios bien definidos con reglas claras"
        },
        "🧠 IA Conexionista": {
            "principio": "Redes de neuronas artificiales que aprenden patrones",
            "fortalezas": ["Flexibilidad", "Aprendizaje automático", "Generalización"],
            "debilidades": ["Caja negra", "Necesita muchos datos", "Recursos computacionales"],
            "ejemplos": ["Redes neuronales", "Deep learning", "CNN/RNN"],
            "mejor_para": "Reconocimiento de patrones complejos"
        },
        "🔄 IA Evolutiva": {
            "principio": "Algoritmos inspirados en evolución biológica",
            "fortalezas": ["Optimización global", "No requiere gradientes", "Robustez"],
            "debilidades": ["Lentitud", "Sin garantía de óptimo", "Muchos parámetros"],
            "ejemplos": ["Algoritmos genéticos", "Programación genética", "PSO"],
            "mejor_para": "Optimización y diseño de soluciones"
        },
        "🎲 IA Probabilística": {
            "principio": "Manejo explícito de incertidumbre con probabilidades",
            "fortalezas": ["Manejo de incertidumbre", "Fundamento teórico", "Interpretabilidad"],
            "debilidades": ["Complejidad computacional", "Modelado difícil", "Escalabilidad"],
            "ejemplos": ["Redes Bayesianas", "HMM", "Filtros de Kalman"],
            "mejor_para": "Sistemas con incertidumbre y riesgo"
        },
        "🤖 IA por Refuerzo": {
            "principio": "Aprendizaje a través de interacción y recompensas",
            "fortalezas": ["Aprendizaje autónomo", "Optimización secuencial", "Adaptabilidad"],
            "debilidades": ["Exploración/explotación", "Recompensas difíciles", "Inestabilidad"],
            "ejemplos": ["Q-learning", "Policy gradients", "Actor-Critic"],
            "mejor_para": "Toma de decisiones secuenciales"
        }
    }
    
    # Mostrar información detallada
    for enfoque, info in enfoques.items():
        print(f"\n{enfoque}")
        print(f"   🎯 Principio: {info['principio']}")
        print(f"   ✅ Fortalezas: {', '.join(info['fortalezas'])}")
        print(f"   ❌ Debilidades: {', '.join(info['debilidades'])}")
        print(f"   💡 Ejemplos: {', '.join(info['ejemplos'])}")
        print(f"   🎪 Mejor para: {info['mejor_para']}")
    
    # Crear visualización comparativa
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Gráfico 1: Popularidad actual (simulada)
    enfoques_nombres = [enfoque.split(' ')[1] for enfoque in enfoques.keys()]
    popularidad = [15, 65, 5, 10, 5]  # Porcentajes aproximados
    colores = ['lightblue', 'green', 'orange', 'purple', 'red']
    
    ax1.pie(popularidad, labels=enfoques_nombres, autopct='%1.1f%%', 
           colors=colores, startangle=90)
    ax1.set_title('📊 Popularidad de Enfoques Técnicos (2024)')
    
    # Gráfico 2: Complejidad vs Interpretabilidad
    complejidad = [3, 8, 6, 7, 7]      # 1-10 scale
    interpretabilidad = [9, 2, 5, 6, 4]  # 1-10 scale
    
    scatter = ax2.scatter(complejidad, interpretabilidad, s=200, 
                         c=colores, alpha=0.7)
    ax2.set_xlabel('Complejidad de Implementación')
    ax2.set_ylabel('Interpretabilidad')
    ax2.set_title('🎯 Complejidad vs Interpretabilidad')
    ax2.grid(True, alpha=0.3)
    
    # Añadir etiquetas
    for i, nombre in enumerate(enfoques_nombres):
        ax2.annotate(nombre, (complejidad[i], interpretabilidad[i]),
                    xytext=(5, 5), textcoords='offset points', fontsize=8)
    
    # Gráfico 3: Eficiencia de datos vs Precisión
    eficiencia_datos = [8, 3, 7, 6, 5]  # Qué tan bien funciona con pocos datos
    precision = [8, 9, 6, 7, 7]         # Precisión típica
    
    ax3.scatter(eficiencia_datos, precision, s=200, c=colores, alpha=0.7)
    ax3.set_xlabel('Eficiencia con Pocos Datos')
    ax3.set_ylabel('Precisión Típica')
    ax3.set_title('📈 Eficiencia de Datos vs Precisión')
    ax3.grid(True, alpha=0.3)
    
    for i, nombre in enumerate(enfoques_nombres):
        ax3.annotate(nombre, (eficiencia_datos[i], precision[i]),
                    xytext=(5, 5), textcoords='offset points', fontsize=8)
    
    # Gráfico 4: Línea de tiempo de desarrollo
    años_desarrollo = [1960, 1943, 1960, 1980, 1989]  # Años aproximados de origen
    ax4.scatter(años_desarrollo, range(len(enfoques_nombres)), 
               s=200, c=colores, alpha=0.7)
    ax4.set_xlabel('Año de Desarrollo')
    ax4.set_yticks(range(len(enfoques_nombres)))
    ax4.set_yticklabels(enfoques_nombres)
    ax4.set_title('📅 Línea de Tiempo de Enfoques')
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# ============================================================================
# 🔄 PARTE 4: SISTEMAS HÍBRIDOS
# ============================================================================

def explorar_sistemas_hibridos():
    """
    Explora la tendencia hacia sistemas híbridos que combinan múltiples enfoques
    """
    print("\n" + "=" * 70)
    print("🔄 SISTEMAS HÍBRIDOS: EL FUTURO DE LA IA")
    print("=" * 70)
    
    print("🎯 ¿POR QUÉ SISTEMAS HÍBRIDOS?")
    print("   • Combinar fortalezas de diferentes enfoques")
    print("   • Compensar debilidades individuales")
    print("   • Obtener mejor rendimiento general")
    print("   • Mayor robustez y adaptabilidad")
    
    sistemas_hibridos = {
        "Neuro-Simbólico": {
            "componentes": ["Redes Neuronales", "Lógica Simbólica"],
            "ventajas": ["Aprendizaje + Razonamiento", "Explicabilidad mejorada"],
            "ejemplo": "IBM Watson: Deep learning + base de conocimiento",
            "aplicaciones": ["Medicina", "Finanzas", "Investigación científica"]
        },
        "Evolutivo-Neural": {
            "componentes": ["Algoritmos Evolutivos", "Redes Neuronales"],
            "ventajas": ["Optimización de arquitecturas", "Búsqueda de hiperparámetros"],
            "ejemplo": "NEAT: Evolución de topologías de red",
            "aplicaciones": ["Robótica", "Juegos", "Control automático"]
        },
        "Probabilístico-Conexionista": {
            "componentes": ["Modelos Probabilísticos", "Deep Learning"],
            "ventajas": ["Incertidumbre cuantificada", "Aprendizaje robusto"],
            "ejemplo": "Variational Autoencoders, Bayesian Neural Networks",
            "aplicaciones": ["Modelado generativo", "Análisis de riesgo"]
        },
        "Reinforcement + Supervised": {
            "componentes": ["Aprendizaje por Refuerzo", "Aprendizaje Supervisado"],
            "ventajas": ["Arranque rápido", "Mejora continua"],
            "ejemplo": "AlphaGo: Imitación + Auto-juego",
            "aplicaciones": ["Juegos", "Robótica", "Conducción autónoma"]
        }
    }
    
    # Mostrar información de sistemas híbridos
    for sistema, info in sistemas_hibridos.items():
        print(f"\n🔄 {sistema}")
        print(f"   🧩 Componentes: {' + '.join(info['componentes'])}")
        print(f"   ✅ Ventajas: {', '.join(info['ventajas'])}")
        print(f"   💡 Ejemplo: {info['ejemplo']}")
        print(f"   🎯 Aplicaciones: {', '.join(info['aplicaciones'])}")
    
    # Crear visualización de arquitectura híbrida
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Diagrama conceptual de sistema híbrido
    # (Simulación de arquitectura)
    componentes = ['Entrada\nDatos', 'Procesamiento\nNeural', 'Razonamiento\nSimbólico', 
                  'Integración', 'Salida\nExplicable']
    x_pos = [1, 2, 2, 3, 4]
    y_pos = [2, 3, 1, 2, 2]
    
    # Dibujar nodos
    for i, (x, y, comp) in enumerate(zip(x_pos, y_pos, componentes)):
        color = ['lightblue', 'green', 'orange', 'purple', 'red'][i]
        ax1.scatter(x, y, s=2000, c=color, alpha=0.7)
        ax1.text(x, y, comp, ha='center', va='center', fontsize=9, fontweight='bold')
    
    # Dibujar conexiones
    conexiones = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4)]
    for inicio, fin in conexiones:
        ax1.arrow(x_pos[inicio], y_pos[inicio], 
                 x_pos[fin] - x_pos[inicio], y_pos[fin] - y_pos[inicio],
                 head_width=0.1, head_length=0.1, fc='gray', ec='gray', alpha=0.6)
    
    ax1.set_xlim(0.5, 4.5)
    ax1.set_ylim(0.5, 3.5)
    ax1.set_title('🏗️ Arquitectura de Sistema Híbrido Neuro-Simbólico')
    ax1.axis('off')
    
    # Comparación de rendimiento
    sistemas_comp = ['Puramente\nNeural', 'Puramente\nSimbólico', 'Sistema\nHíbrido']
    precision = [8.5, 7.0, 9.2]
    explicabilidad = [3.0, 9.5, 8.0]
    robustez = [7.0, 6.0, 8.5]
    
    x = np.arange(len(sistemas_comp))
    width = 0.25
    
    ax2.bar(x - width, precision, width, label='Precisión', alpha=0.8)
    ax2.bar(x, explicabilidad, width, label='Explicabilidad', alpha=0.8)
    ax2.bar(x + width, robustez, width, label='Robustez', alpha=0.8)
    
    ax2.set_ylabel('Puntuación (1-10)')
    ax2.set_title('📊 Comparación de Rendimiento')
    ax2.set_xticks(x)
    ax2.set_xticklabels(sistemas_comp)
    ax2.legend()
    ax2.grid(True, alpha=0.3, axis='y')
    
    plt.tight_layout()
    plt.show()
    
    print("\n🚀 TENDENCIAS FUTURAS:")
    print("   • Integración más profunda de enfoques")
    print("   • Sistemas auto-configurables")
    print("   • Arquitecturas modulares y composables")
    print("   • IA explicable por diseño")

# ============================================================================
# 🎓 PARTE 5: EVALUACIÓN FINAL
# ============================================================================

def evaluacion_tipos_ia():
    """
    Evaluación comprensiva sobre tipos de IA
    """
    print("\n" + "=" * 70)
    print("🎓 EVALUACIÓN: TIPOS DE INTELIGENCIA ARTIFICIAL")
    print("=" * 70)
    
    preguntas = [
        {
            "pregunta": "¿Cuál es la principal limitación de la IA débil?",
            "opciones": [
                "A) Es menos precisa que la IA fuerte",
                "B) No puede transferir conocimiento entre dominios",
                "C) Requiere más recursos computacionales",
                "D) Es más difícil de programar"
            ],
            "respuesta": "B",
            "explicacion": "La IA débil está especializada en una tarea y no puede aplicar su conocimiento a otros dominios."
        },
        {
            "pregunta": "¿Qué nivel de IA representa GitHub Copilot?",
            "opciones": [
                "A) IA Asistiva (Nivel 1)",
                "B) IA Automática (Nivel 2)", 
                "C) IA Aumentativa (Nivel 3)",
                "D) IA Autónoma (Nivel 4)"
            ],
            "respuesta": "C",
            "explicacion": "GitHub Copilot aumenta significativamente las capacidades del programador mediante colaboración activa."
        },
        {
            "pregunta": "¿Cuál es la principal ventaja de los sistemas híbridos?",
            "opciones": [
                "A) Son más rápidos de entrenar",
                "B) Combinan fortalezas de diferentes enfoques",
                "C) Requieren menos datos",
                "D) Son más fáciles de implementar"
            ],
            "respuesta": "B",
            "explicacion": "Los sistemas híbridos combinan las fortalezas de diferentes enfoques para obtener mejor rendimiento."
        },
        {
            "pregunta": "¿Qué enfoque técnico es mejor para dominios con reglas claras y bien definidas?",
            "opciones": [
                "A) IA Conexionista",
                "B) IA Simbólica",
                "C) IA Evolutiva",
                "D) IA por Refuerzo"
            ],
            "respuesta": "B",
            "explicacion": "La IA simbólica es ideal para dominios bien definidos con reglas claras y lógica formal."
        },
        {
            "pregunta": "¿Cuál de estos sistemas NO es un ejemplo de IA débil?",
            "opciones": [
                "A) ChatGPT",
                "B) AlphaGo",
                "C) Tesla Autopilot",
                "D) Ninguno (todos son IA débil)"
            ],
            "respuesta": "D",
            "explicacion": "Todos los sistemas mencionados son ejemplos de IA débil, especializados en tareas específicas."
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
        print("🎉 ¡Experto en Tipos de IA! Dominas perfectamente la clasificación")
    elif puntuacion >= len(preguntas) * 0.8:
        print("👍 ¡Excelente! Tienes muy buen conocimiento de los tipos de IA")
    elif puntuacion >= len(preguntas) * 0.6:
        print("📖 Bien, pero puedes profundizar más en algunos conceptos")
    else:
        print("📚 Necesitas repasar los diferentes tipos y clasificaciones de IA")

# ============================================================================
# 🎯 FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Función principal que ejecuta todo el ejemplo sobre tipos de IA
    """
    print("🎯 EJEMPLO 03: TIPOS DE INTELIGENCIA ARTIFICIAL")
    print("=" * 80)
    
    while True:
        print("\n📋 MENÚ DE CLASIFICACIÓN:")
        print("1. 🧠 IA Débil vs IA Fuerte - Comparación fundamental")
        print("2. 📊 Niveles de Capacidad - Clasificación por habilidades")
        print("3. 🔧 Enfoques Técnicos - Métodos de implementación")
        print("4. 🔄 Sistemas Híbridos - El futuro de la IA")
        print("5. 🎮 Simulador clasificador de niveles")
        print("6. 🎓 Evaluación final")
        print("7. 🚪 Salir")
        
        opcion = input("\n¿Qué tipo de clasificación quieres explorar? (1-7): ").strip()
        
        if opcion == "1":
            comparar_ia_debil_fuerte()
            evaluar_sistemas_existentes()
        elif opcion == "2":
            clasificar_niveles_capacidad()
        elif opcion == "3":
            explorar_enfoques_tecnicos()
        elif opcion == "4":
            explorar_sistemas_hibridos()
        elif opcion == "5":
            simulador_clasificador_niveles()
        elif opcion == "6":
            evaluacion_tipos_ia()
        elif opcion == "7":
            print("\n🎉 ¡Has dominado la clasificación de tipos de IA!")
            print("📚 Próximo paso: ejemplo_04_aplicaciones_ia.py")
            break
        else:
            print("❌ Opción no válida. Por favor, elige entre 1-7.")

# ============================================================================
# 🚀 EJECUCIÓN
# ============================================================================

if __name__ == "__main__":
    # Configurar visualizaciones
    plt.style.use('default')
    plt.rcParams['figure.figsize'] = (12, 8)
    plt.rcParams['font.size'] = 10
    sns.set_palette("husl")
    
    # Ejecutar programa principal
    main()

"""
📚 CLASIFICACIONES DE IA DOMINADAS:

✅ IA Débil vs IA Fuerte - Diferencias fundamentales
✅ Niveles de capacidad (0-5) - Escala de habilidades
✅ Enfoques técnicos - Métodos de implementación
✅ Sistemas híbridos - Combinación de enfoques
✅ Evaluación práctica de sistemas reales

🔍 CRITERIOS DE CLASIFICACIÓN APRENDIDOS:
• Especialización vs Generalización
• Nivel de autonomía y capacidad
• Enfoque técnico subyacente  
• Grado de hibridación
• Aplicabilidad y dominio de uso

🚀 PRÓXIMO PASO:
Ejecuta ejemplo_04_aplicaciones_ia.py para ver cómo estos tipos se aplican en el mundo real
"""