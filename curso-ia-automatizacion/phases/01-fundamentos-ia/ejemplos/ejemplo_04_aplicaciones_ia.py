"""
🌟 EJEMPLO 04: Aplicaciones de Inteligencia Artificial
====================================================

📚 OBJETIVOS DE APRENDIZAJE:
• Identificar aplicaciones de IA en diferentes industrias
• Analizar casos de éxito y fracaso en implementaciones
• Evaluar el impacto económico y social de la IA
• Explorar tendencias emergentes y oportunidades futuras
• Desarrollar criterios para seleccionar soluciones de IA

🎯 NIVEL: Intermedio - Aplicaciones prácticas
⏱️ TIEMPO ESTIMADO: 75-90 minutos
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import random

# ============================================================================
# 🏥 PARTE 1: IA EN SALUD Y MEDICINA
# ============================================================================

def explorar_ia_salud():
    """
    Explora aplicaciones de IA en el sector sanitario
    """
    print("=" * 70)
    print("🏥 INTELIGENCIA ARTIFICIAL EN SALUD")
    print("=" * 70)
    
    aplicaciones_salud = {
        "🔬 Diagnóstico por Imagen": {
            "descripcion": "Análisis automático de radiografías, TAC, resonancias",
            "precisión": 95,  # Porcentaje
            "casos_uso": ["Detección de cáncer", "Fracturas óseas", "Patologías cardíacas"],
            "beneficios": ["Diagnóstico temprano", "Reducción de errores", "Mayor velocidad"],
            "ejemplos": ["IBM Watson for Oncology", "Google DeepMind Eye Disease"]
        },
        "💊 Descubrimiento de Fármacos": {
            "descripcion": "Aceleración del desarrollo de nuevos medicamentos",
            "precisión": 78,
            "casos_uso": ["Identificación de compuestos", "Predicción de efectos", "Optimización"],
            "beneficios": ["Reducción de costos", "Menor tiempo desarrollo", "Menos fallos"],
            "ejemplos": ["DeepMind AlphaFold", "Atomwise drug discovery"]
        },
        "🤖 Cirugía Robótica": {
            "descripcion": "Asistencia y automatización en procedimientos quirúrgicos",
            "precisión": 92,
            "casos_uso": ["Cirugía mínimamente invasiva", "Neurocirugía", "Oftalmología"],
            "beneficios": ["Mayor precisión", "Menos invasiva", "Recuperación rápida"],
            "ejemplos": ["Da Vinci Surgical System", "Mazor Robotics"]
        },
        "👩‍⚕️ Asistentes Virtuales": {
            "descripcion": "Soporte para profesionales sanitarios y pacientes",
            "precisión": 85,
            "casos_uso": ["Triaje virtual", "Seguimiento pacientes", "Recordatorios"],
            "beneficios": ["Acceso 24/7", "Reducción carga trabajo", "Personalización"],
            "ejemplos": ["Ada Health", "Babylon Health", "Your.MD"]
        },
        "🧬 Medicina Personalizada": {
            "descripcion": "Tratamientos adaptados al perfil genético individual",
            "precisión": 88,
            "casos_uso": ["Oncología personalizada", "Farmacogenómica", "Terapia génica"],
            "beneficios": ["Tratamientos efectivos", "Menos efectos secundarios", "Precisión"],
            "ejemplos": ["Foundation Medicine", "Tempus", "IBM Watson Genomics"]
        }
    }
    
    # Mostrar información detallada
    for aplicacion, info in aplicaciones_salud.items():
        print(f"\n{aplicacion}")
        print(f"   📖 {info['descripcion']}")
        print(f"   🎯 Precisión promedio: {info['precisión']}%")
        print(f"   💡 Casos de uso: {', '.join(info['casos_uso'])}")
        print(f"   ✅ Beneficios: {', '.join(info['beneficios'])}")
        print(f"   🏢 Ejemplos comerciales: {', '.join(info['ejemplos'])}")
    
    # Crear visualizaciones
    _, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 8))
    
    # Gráfico de precisión por aplicación
    nombres = [app.split(' ')[1] for app in aplicaciones_salud.keys()]
    precisiones = [info['precisión'] for info in aplicaciones_salud.values()]
    colores = ['lightcoral', 'lightblue', 'lightgreen', 'orange', 'plum']
    
    bars = ax1.bar(nombres, precisiones, color=colores, alpha=0.8)
    ax1.set_ylabel('Precisión (%)')
    ax1.set_title('🎯 Precisión de Aplicaciones IA en Salud')
    ax1.set_ylim(0, 100)
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Añadir valores en las barras
    for bar, precision in zip(bars, precisiones):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{precision}%', ha='center', va='bottom', fontweight='bold')
    
    # Gráfico de adopción por región (simulado)
    regiones = ['América\nNorte', 'Europa', 'Asia', 'América\nLatina', 'África']
    adopcion = [85, 75, 70, 45, 25]  # Porcentaje de adopción
    
    ax2.pie(adopcion, labels=regiones, autopct='%1.1f%%', 
           colors=colores, startangle=90, explode=(0.1, 0, 0, 0, 0))
    ax2.set_title('🌍 Adopción de IA en Salud por Región')
    
    plt.tight_layout()
    plt.show()
    
    # Proyección de crecimiento
    print("\n📈 PROYECCIONES DEL MERCADO:")
    años = list(range(2020, 2031))
    mercado_valor = [4.9, 6.7, 10.4, 15.1, 22.8, 31.3, 45.2, 62.8, 85.6, 116.2, 148.4]  # Billions USD
    
    plt.figure(figsize=(12, 6))
    plt.plot(años, mercado_valor, marker='o', linewidth=3, markersize=8, color='green')
    plt.title('💰 Proyección del Mercado Global de IA en Salud')
    plt.xlabel('Año')
    plt.ylabel('Valor del Mercado (Billones USD)')
    plt.grid(True, alpha=0.3)
    plt.xticks(años[::2])  # Mostrar cada dos años
    
    # Añadir anotaciones
    for i, valor in enumerate(mercado_valor[::3]):  # Cada 3 años
        plt.annotate(f'${valor}B', (años[i*3], valor), 
                    textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.tight_layout()
    plt.show()

def caso_estudio_watson_oncology():
    """
    Caso de estudio: IBM Watson for Oncology - éxito y fracaso
    """
    print("\n" + "=" * 70)
    print("📊 CASO DE ESTUDIO: IBM WATSON FOR ONCOLOGY")
    print("=" * 70)
    
    print("🎯 OBJETIVO:")
    print("   Asistir a oncólogos en recomendaciones de tratamiento de cáncer")
    
    print("\n✅ ÉXITOS INICIALES:")
    print("   • Procesamiento de literatura médica masiva")
    print("   • Recomendaciones basadas en evidencia")
    print("   • Adopción en hospitales prestigiosos")
    print("   • Marketing exitoso y expectativas altas")
    
    print("\n❌ PROBLEMAS ENCONTRADOS:")
    problemas = [
        "Entrenamiento con datos limitados (Memorial Sloan Kettering únicamente)",
        "Sesgos en recomendaciones hacia protocolos estadounidenses",
        "Dificultad con casos complejos y atípicos",
        "Interfaz poco intuitiva para médicos",
        "Altos costos de implementación y mantenimiento",
        "Resistencia del personal médico",
        "Evidencia limitada de mejora en resultados"
    ]
    
    for i, problema in enumerate(problemas, 1):
        print(f"   {i}. {problema}")
    
    print("\n📉 RESULTADO:")
    print("   • Múltiples hospitales cancelaron contratos")
    print("   • Críticas por overselling de capacidades")
    print("   • IBM reestructuró el programa en 2022")
    print("   • Lecciones aprendidas sobre implementación de IA médica")
    
    # Visualizar timeline del proyecto
    años = ['2012', '2013', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
    eventos = [
        'Inicio desarrollo',
        'Alianza Sloan Kettering', 
        'Primeros pilotos',
        'Lanzamiento comercial',
        'Expansión global',
        'Primeras críticas',
        'Estudios negativos',
        'Cancelaciones',
        'Más hospitales se retiran',
        'Reestructuración'
    ]
    
    sentiment = [5, 7, 8, 9, 8, 6, 4, 3, 2, 3]  # 1-10 scale
    
    plt.figure(figsize=(14, 8))
    colors = ['red' if s < 5 else 'orange' if s < 7 else 'green' for s in sentiment]
    
    plt.scatter(años, sentiment, s=200, c=colors, alpha=0.7)
    plt.plot(años, sentiment, '--', alpha=0.5, color='gray')
    
    # Añadir eventos
    for i, (año, evento, sent) in enumerate(zip(años, eventos, sentiment)):
        plt.annotate(evento, (año, sent), 
                    textcoords="offset points", xytext=(0, 15 if i % 2 == 0 else -25), 
                    ha='center', fontsize=9, rotation=45 if len(evento) > 15 else 0)
    
    plt.ylabel('Percepción del Proyecto (1-10)')
    plt.title('📈 Timeline: IBM Watson for Oncology')
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.ylim(0, 10)
    plt.tight_layout()
    plt.show()
    
    print("\n🎓 LECCIONES APRENDIDAS:")
    lecciones = [
        "Datos de entrenamiento diversos y representativos son críticos",
        "La adopción médica requiere evidencia clínica sólida",
        "La interfaz debe diseñarse con y para los usuarios finales",
        "El marketing no debe sobrepasar las capacidades reales",
        "Los pilotos deben incluir múltiples instituciones",
        "El cambio cultural en medicina es gradual y requiere paciencia"
    ]
    
    for i, leccion in enumerate(lecciones, 1):
        print(f"   💡 {i}. {leccion}")

# ============================================================================
# 🚗 PARTE 2: IA EN TRANSPORTE
# ============================================================================

def explorar_ia_transporte():
    """
    Explora aplicaciones de IA en transporte y movilidad
    """
    print("\n" + "=" * 70)
    print("🚗 INTELIGENCIA ARTIFICIAL EN TRANSPORTE")
    print("=" * 70)
    
    niveles_autonomia = {
        "Nivel 0": {
            "nombre": "Sin automatización",
            "descripcion": "Control humano completo",
            "ejemplos": ["Autos tradicionales", "Motocicletas básicas"],
            "adopcion": 60  # Porcentaje del parque vehicular
        },
        "Nivel 1": {
            "nombre": "Asistencia al conductor",
            "descripcion": "Sistema controla aceleración O dirección",
            "ejemplos": ["Control crucero adaptativo", "Asistencia de carril"],
            "adopcion": 25
        },
        "Nivel 2": {
            "nombre": "Automatización parcial",
            "descripcion": "Sistema controla aceleración Y dirección",
            "ejemplos": ["Tesla Autopilot", "Mercedes Drive Pilot"],
            "adopcion": 12
        },
        "Nivel 3": {
            "nombre": "Automatización condicional",
            "descripcion": "Sistema maneja todo, humano debe estar listo",
            "ejemplos": ["Audi Traffic Jam Pilot", "Honda Legend"],
            "adopcion": 2
        },
        "Nivel 4": {
            "nombre": "Alta automatización",
            "descripcion": "Sistema autónomo en condiciones específicas",
            "ejemplos": ["Waymo en Phoenix", "Robotaxis limitados"],
            "adopcion": 0.8
        },
        "Nivel 5": {
            "nombre": "Automatización completa",
            "descripcion": "Sin restricciones, sin conductor humano",
            "ejemplos": ["Aún no comercial", "Objetivo futuro"],
            "adopcion": 0.2
        }
    }
    
    # Mostrar información de niveles
    for nivel, info in niveles_autonomia.items():
        print(f"\n🚗 {nivel}: {info['nombre']}")
        print(f"   📖 {info['descripcion']}")
        print(f"   💡 Ejemplos: {', '.join(info['ejemplos'])}")
        print(f"   📊 Adopción actual: {info['adopcion']}%")
    
    # Crear visualizaciones
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Gráfico 1: Distribución actual de niveles
    niveles_nombres = list(niveles_autonomia.keys())
    adopciones = [info['adopcion'] for info in niveles_autonomia.values()]
    colores = plt.cm.viridis(np.linspace(0, 1, len(niveles_nombres)))
    
    wedges, texts, autotexts = ax1.pie(adopciones, labels=niveles_nombres, autopct='%1.1f%%',
                                      colors=colores, startangle=90)
    ax1.set_title('🚗 Distribución Actual de Niveles de Autonomía')
    
    # Gráfico 2: Proyección temporal
    años_proj = list(range(2024, 2035))
    # Proyecciones para Nivel 4 y 5
    nivel4_proj = [0.8, 1.2, 2.1, 3.8, 6.2, 9.8, 14.5, 20.2, 27.1, 34.8, 42.5]
    nivel5_proj = [0.2, 0.3, 0.5, 0.8, 1.4, 2.3, 4.1, 6.8, 10.2, 15.1, 21.3]
    
    ax2.plot(años_proj, nivel4_proj, marker='o', label='Nivel 4', linewidth=2)
    ax2.plot(años_proj, nivel5_proj, marker='s', label='Nivel 5', linewidth=2)
    ax2.set_xlabel('Año')
    ax2.set_ylabel('Adopción (%)')
    ax2.set_title('📈 Proyección: Vehículos Autónomos Avanzados')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    # Gráfico 3: Beneficios esperados
    beneficios = ['Reducción\nAccidentes', 'Eficiencia\nTráfico', 'Accesibilidad', 
                 'Productividad', 'Emisiones\nReducidas']
    impacto = [85, 70, 60, 75, 45]  # Porcentaje de mejora esperada
    
    bars = ax3.bar(beneficios, impacto, color=['red', 'orange', 'blue', 'green', 'brown'], alpha=0.7)
    ax3.set_ylabel('Mejora Esperada (%)')
    ax3.set_title('📊 Beneficios Esperados de la Conducción Autónoma')
    ax3.tick_params(axis='x', rotation=45)
    
    # Añadir valores
    for bar, valor in zip(bars, impacto):
        ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                f'{valor}%', ha='center', va='bottom', fontweight='bold')
    
    # Gráfico 4: Desafíos técnicos
    desafios = ['Percepción\nCompleja', 'Decisiones\nÉticas', 'Condiciones\nClimáticas', 
                'Interacción\nHumana', 'Infraestructura']
    dificultad = [9, 8, 7, 6, 8]  # Escala 1-10
    
    bars = ax4.barh(desafios, dificultad, color='salmon', alpha=0.7)
    ax4.set_xlabel('Nivel de Dificultad (1-10)')
    ax4.set_title('🚧 Principales Desafíos Técnicos')
    
    # Añadir valores
    for bar, valor in zip(bars, dificultad):
        ax4.text(bar.get_width() + 0.1, bar.get_y() + bar.get_height()/2,
                f'{valor}/10', va='center', fontweight='bold')
    
    plt.tight_layout()
    plt.show()

def simulador_decision_vehiculo_autonomo():
    """
    Simulador de dilemas éticos en vehículos autónomos
    """
    print("\n" + "=" * 70)
    print("🤖 SIMULADOR: DILEMAS ÉTICOS EN VEHÍCULOS AUTÓNOMOS")
    print("=" * 70)
    
    escenarios = [
        {
            "situacion": "Frenos fallan: continuar recto (5 peatones) o girar (1 pasajero del auto)",
            "opciones": [
                "A) Continuar recto - minimizar víctimas totales",
                "B) Girar - proteger pasajeros del vehículo",
                "C) Decisión aleatoria - no programar preferencia"
            ],
            "factores": ["Número de vidas", "Responsabilidad con pasajeros", "Imparcialidad"],
            "dilema": "¿Debe el auto priorizar el mayor bien o proteger a sus ocupantes?"
        },
        {
            "situacion": "Inevitable atropello: niño corriendo vs adulto mayor caminando",
            "opciones": [
                "A) Hacia el niño - más ágil, puede esquivar",
                "B) Hacia el adulto - vida más completa vivida",
                "C) No discriminar por edad"
            ],
            "factores": ["Años de vida restantes", "Probabilidad de supervivencia", "Igualdad"],
            "dilema": "¿Debe considerar la edad en decisiones de vida o muerte?"
        },
        {
            "situacion": "Cruce peligroso: atropellar a quien cruza ilegalmente vs chocar auto que respeta semáforo",  
            "opciones": [
                "A) Hacia el peatón - violó la norma",
                "B) Hacia el auto - conductor responsable no debe sufrir",
                "C) Minimizar daño total sin considerar culpabilidad"
            ],
            "factores": ["Responsabilidad personal", "Justicia", "Consecuencias"],
            "dilema": "¿Debe influir el comportamiento previo en la decisión?"
        }
    ]
    
    respuestas_usuario = []
    
    for i, escenario in enumerate(escenarios, 1):
        print(f"\n🚨 ESCENARIO {i}:")
        print(f"   {escenario['situacion']}")
        print("\n🤔 OPCIONES:")
        for opcion in escenario['opciones']:
            print(f"   {opcion}")
        
        print(f"\n⚖️ FACTORES EN JUEGO: {', '.join(escenario['factores'])}")
        print(f"🎯 DILEMA CENTRAL: {escenario['dilema']}")
        
        while True:
            try:
                respuesta = input("\nTu decisión (A/B/C): ").upper().strip()
                if respuesta in ['A', 'B', 'C']:
                    respuestas_usuario.append(respuesta)
                    break
                else:
                    print("❌ Por favor, elige A, B o C")
            except:
                print("❌ Entrada inválida")
    
    # Análisis de respuestas
    print("\n" + "=" * 50)
    print("📊 ANÁLISIS DE TUS DECISIONES")
    print("=" * 50)
    
    filosofias = {
        'utilitarista': 0,    # Maximizar bienestar general
        'deontologica': 0,    # Deberes y reglas
        'virtud': 0          # Carácter y virtudes
    }
    
    # Análisis simplificado de tendencias
    if respuestas_usuario[0] == 'A':  # Minimizar víctimas
        filosofias['utilitarista'] += 1
    elif respuestas_usuario[0] == 'B':  # Proteger pasajeros
        filosofias['deontologica'] += 1
    else:
        filosofias['virtud'] += 1
    
    if respuestas_usuario[1] == 'C':  # No discriminar
        filosofias['deontologica'] += 1
    elif respuestas_usuario[1] == 'A':
        filosofias['utilitarista'] += 1
    else:
        filosofias['virtud'] += 1
    
    if respuestas_usuario[2] == 'C':  # Minimizar daño
        filosofias['utilitarista'] += 1
    elif respuestas_usuario[2] == 'A':  # Considerar responsabilidad
        filosofias['deontologica'] += 1
    else:
        filosofias['virtud'] += 1
    
    # Mostrar resultado
    filosofia_dominante = max(filosofias, key=filosofias.get)
    
    print(f"🎭 TU PERFIL ÉTICO: {filosofia_dominante.upper()}")
    
    if filosofia_dominante == 'utilitarista':
        print("   📊 Tiendes a maximizar el bienestar general")
        print("   ✅ Pros: Eficiencia, resultados medibles")
        print("   ❌ Contras: Puede ignorar derechos individuales")
    elif filosofia_dominante == 'deontologica':
        print("   ⚖️ Te enfocas en deberes y reglas universales")  
        print("   ✅ Pros: Consistencia, respeto por derechos")
        print("   ❌ Contras: Rigidez, resultados subóptimos")
    else:
        print("   🌟 Valoras la imparcialidad y el carácter")
        print("   ✅ Pros: Equidad, consideración contextual")
        print("   ❌ Contras: Ambigüedad, difícil implementación")
    
    print("\n🚗 IMPLICACIONES PARA VEHÍCULOS AUTÓNOMOS:")
    print("   • No existe consenso universal sobre la ética correcta")
    print("   • Los algoritmos deben transparentar sus criterios")
    print("   • Se necesita debate público sobre estas decisiones")
    print("   • Diferentes culturas pueden preferir enfoques distintos")

# ============================================================================
# 💰 PARTE 3: IA EN FINANZAS
# ============================================================================

def explorar_ia_finanzas():
    """
    Explora aplicaciones de IA en servicios financieros
    """
    print("\n" + "=" * 70)
    print("💰 INTELIGENCIA ARTIFICIAL EN FINANZAS")
    print("=" * 70)
    
    aplicaciones_fintech = {
        "🔍 Detección de Fraude": {
            "descripcion": "Identificación en tiempo real de transacciones sospechosas",
            "precision": 99.5,
            "ahorro_anual": "Billions USD en pérdidas evitadas",
            "casos_uso": ["Tarjetas de crédito", "Transferencias", "Criptomonedas"],
            "tecnologias": ["Machine Learning", "Anomaly Detection", "Graph Analysis"]
        },
        "📊 Trading Algorítmico": {
            "descripcion": "Ejecución automática de operaciones basada en algoritmos",
            "precision": 85.2,
            "ahorro_anual": "Reducción 40% costos transacción",
            "casos_uso": ["High-frequency trading", "Arbitraje", "Market making"],
            "tecnologias": ["Deep Learning", "Reinforcement Learning", "NLP"]
        },
        "💳 Evaluación Crediticia": {
            "descripcion": "Análisis automático de riesgo crediticio",
            "precision": 92.3,
            "ahorro_anual": "Reducción 25% morosidad",
            "casos_uso": ["Préstamos personales", "Hipotecas", "Microcréditos"],
            "tecnologias": ["Random Forest", "Gradient Boosting", "Neural Networks"]
        },
        "🤖 Robo-Advisors": {
            "descripcion": "Asesoramiento automático de inversiones",
            "precision": 78.9,
            "ahorro_anual": "Comisiones 80% menores",
            "casos_uso": ["Gestión de carteras", "Planificación financiera", "Rebalanceo"],
            "tecnologias": ["Portfolio Optimization", "Risk Assessment", "Goal-based Investing"]
        },
        "📞 Atención al Cliente": {
            "descripcion": "Chatbots y asistentes virtuales financieros",
            "precision": 88.7,
            "ahorro_anual": "Reducción 60% costos soporte",
            "casos_uso": ["Consultas básicas", "Soporte 24/7", "Gestión de cuentas"],
            "tecnologias": ["NLP", "Conversational AI", "Intent Recognition"]
        }
    }
    
    # Mostrar información
    for aplicacion, info in aplicaciones_fintech.items():
        print(f"\n{aplicacion}")
        print(f"   📖 {info['descripcion']}")
        print(f"   🎯 Precisión: {info['precision']}%")
        print(f"   💰 Beneficio: {info['ahorro_anual']}")
        print(f"   🎪 Casos de uso: {', '.join(info['casos_uso'])}")
        print(f"   🔧 Tecnologías: {', '.join(info['tecnologias'])}")
    
    # Visualizaciones
    _, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Gráfico 1: Precisión por aplicación
    nombres = [app.split(' ')[1] for app in aplicaciones_fintech.keys()]
    precisiones = [info['precision'] for info in aplicaciones_fintech.values()]
    
    bars = ax1.bar(nombres, precisiones, color='gold', alpha=0.7)
    ax1.set_ylabel('Precisión (%)')
    ax1.set_title('🎯 Precisión de Aplicaciones IA en Finanzas')
    ax1.tick_params(axis='x', rotation=45)
    ax1.grid(True, alpha=0.3, axis='y')
    
    for bar, precision in zip(bars, precisiones):
        ax1.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
                f'{precision}%', ha='center', va='bottom', fontweight='bold')
    
    # Gráfico 2: Adopción por institución financiera
    tipos_institucion = ['Bancos\nGrandes', 'Bancos\nRegionales', 'Fintech\nStartups', 
                        'Aseguradoras', 'Gestoras\nFondos']
    adopcion_ia = [95, 78, 88, 65, 82]
    
    ax2.barh(tipos_institucion, adopcion_ia, color='lightgreen', alpha=0.7)
    ax2.set_xlabel('Adopción de IA (%)')
    ax2.set_title('🏦 Adopción de IA por Tipo de Institución')
    
    # Gráfico 3: ROI de implementaciones de IA
    aplicaciones_roi = ['Fraude', 'Trading', 'Crédito', 'Robo-Advisor', 'Soporte']
    roi_percentaje = [320, 180, 240, 150, 280]  # ROI en %
    
    ax3.bar(aplicaciones_roi, roi_percentaje, color='darkgreen', alpha=0.7)
    ax3.set_ylabel('ROI (%)')
    ax3.set_title('💹 ROI de Implementaciones de IA (primer año)')
    ax3.tick_params(axis='x', rotation=45)
    
    # Gráfico 4: Timeline de evolución
    años = list(range(2015, 2025))
    inversion_ia_fintech = [2.1, 3.4, 5.8, 8.9, 12.7, 18.2, 23.8, 31.4, 42.1, 56.3]  # Billions USD
    
    ax4.plot(años, inversion_ia_fintech, marker='o', linewidth=3, markersize=8, color='blue')
    ax4.set_xlabel('Año')
    ax4.set_ylabel('Inversión (Billones USD)')
    ax4.set_title('📈 Inversión Global en IA Financiera')
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

def simulador_evaluacion_riesgo_credito():
    """
    Simulador de sistema de evaluación de riesgo crediticio con IA
    """
    print("\n" + "=" * 70)
    print("🎮 SIMULADOR: EVALUACIÓN DE RIESGO CREDITICIO")
    print("=" * 70)
    
    # Generar perfiles de solicitantes ficticios
    perfiles = [
        {
            "nombre": "María García",
            "edad": 28,
            "ingresos": 45000,
            "historial_credito": 720,
            "empleo_años": 3,
            "deudas_actuales": 8000,
            "educacion": "Universitaria",
            "vivienda": "Alquiler"
        },
        {
            "nombre": "Carlos López",
            "edad": 45,
            "ingresos": 75000,
            "historial_credito": 680,
            "empleo_años": 15,
            "deudas_actuales": 25000,
            "educacion": "Secundaria",
            "vivienda": "Propia"
        },
        {
            "nombre": "Ana Martínez", 
            "edad": 22,
            "ingresos": 28000,
            "historial_credito": 0,  # Sin historial
            "empleo_años": 1,
            "deudas_actuales": 12000,
            "educacion": "Universitaria",
            "vivienda": "Familiar"
        }
    ]
    
    def calcular_score_credito(perfil):
        """Algoritmo simplificado de scoring crediticio"""
        score = 500  # Base
        
        # Factor edad (curva óptima 30-50 años)
        if 25 <= perfil["edad"] <= 55:
            score += 50
        elif perfil["edad"] < 25 or perfil["edad"] > 65:
            score -= 30
        
        # Factor ingresos
        if perfil["ingresos"] > 60000:
            score += 100
        elif perfil["ingresos"] > 40000:
            score += 50
        elif perfil["ingresos"] < 25000:
            score -= 50
        
        # Historial crediticio (factor más importante)
        if perfil["historial_credito"] > 750:
            score += 150
        elif perfil["historial_credito"] > 700:
            score += 100
        elif perfil["historial_credito"] > 650:
            score += 50
        elif perfil["historial_credito"] == 0:
            score -= 100  # Sin historial
        else:
            score -= 150  # Mal historial
        
        # Estabilidad laboral
        if perfil["empleo_años"] > 5:
            score += 50
        elif perfil["empleo_años"] < 2:
            score -= 30
        
        # Ratio deuda/ingresos
        ratio_deuda = perfil["deudas_actuales"] / perfil["ingresos"]
        if ratio_deuda < 0.3:
            score += 30
        elif ratio_deuda > 0.6:
            score -= 80
        
        # Educación
        if perfil["educacion"] == "Universitaria":
            score += 20
        
        # Vivienda
        if perfil["vivienda"] == "Propia":
            score += 30
        
        return max(300, min(850, score))  # Limitar entre 300-850
    
    print("🎯 EVALUANDO PERFILES DE SOLICITANTES...")
    
    resultados = []
    for perfil in perfiles:
        score = calcular_score_credito(perfil)
        
        # Determinar decisión
        if score >= 700:
            decision = "APROBADO"
            tasa_interes = 4.5 + (800 - score) * 0.02  # Tasa mejor para score alto
            color = "🟢"
        elif score >= 600:
            decision = "APROBADO CONDICIONAL"  
            tasa_interes = 8.5 + (700 - score) * 0.05
            color = "🟡"
        else:
            decision = "RECHAZADO"
            tasa_interes = None
            color = "🔴"
        
        resultado = {
            "perfil": perfil,
            "score": score,
            "decision": decision,
            "tasa": tasa_interes,
            "color": color
        }
        resultados.append(resultado)
        
        # Mostrar resultado
        print(f"\n{color} {perfil['nombre']} (Edad: {perfil['edad']})")
        print(f"   💰 Ingresos: ${perfil['ingresos']:,}")
        print(f"   📊 Score crediticio histórico: {perfil['historial_credito'] or 'Sin historial'}")
        print(f"   👔 Años de empleo: {perfil['empleo_años']}")
        print(f"   💳 Deudas actuales: ${perfil['deudas_actuales']:,}")
        print(f"   🎓 Educación: {perfil['educacion']}")
        print(f"   🏠 Vivienda: {perfil['vivienda']}")
        print(f"   📈 Score IA calculado: {score}")
        print(f"   ⚖️ Decisión: {decision}")
        if tasa_interes:
            print(f"   💸 Tasa de interés: {tasa_interes:.1f}%")
    
    # Visualizar resultados
    plt.figure(figsize=(14, 10))
    
    # Subplot 1: Scores por solicitante
    plt.subplot(2, 2, 1)
    nombres = [r["perfil"]["nombre"] for r in resultados]
    scores = [r["score"] for r in resultados]
    colores_bars = ['green' if s >= 700 else 'orange' if s >= 600 else 'red' for s in scores]
    
    bars = plt.bar(nombres, scores, color=colores_bars, alpha=0.7)
    plt.ylabel('Score Crediticio')
    plt.title('📊 Scores de Evaluación por IA')
    plt.xticks(rotation=45)
    
    # Añadir líneas de referencia
    plt.axhline(y=700, color='green', linestyle='--', alpha=0.7, label='Aprobación')
    plt.axhline(y=600, color='orange', linestyle='--', alpha=0.7, label='Condicional')
    plt.legend()
    
    # Subplot 2: Factores por solicitante
    plt.subplot(2, 2, 2)
    factores = ['Ingresos', 'Hist. Crédito', 'Estab. Laboral', 'Ratio Deuda']
    
    # Normalizar factores para comparación
    ingresos_norm = [p["perfil"]["ingresos"]/1000 for p in resultados]
    credito_norm = [p["perfil"]["historial_credito"]/10 if p["perfil"]["historial_credito"] > 0 else 0 for p in resultados]
    empleo_norm = [p["perfil"]["empleo_años"]*10 for p in resultados]
    deuda_norm = [100 - (p["perfil"]["deudas_actuales"]/p["perfil"]["ingresos"]*100) for p in resultados]
    
    x = np.arange(len(nombres))
    width = 0.2
    
    plt.bar(x - 1.5*width, ingresos_norm, width, label='Ingresos/1k', alpha=0.8)
    plt.bar(x - 0.5*width, credito_norm, width, label='Crédito/10', alpha=0.8)
    plt.bar(x + 0.5*width, empleo_norm, width, label='Empleoⅹ10', alpha=0.8)
    plt.bar(x + 1.5*width, deuda_norm, width, label='100-RatioDeuda', alpha=0.8)
    
    plt.ylabel('Valor Normalizado')
    plt.title('📈 Comparación de Factores')
    plt.xticks(x, nombres, rotation=45)
    plt.legend()
    
    # Subplot 3: Distribución de decisiones
    plt.subplot(2, 2, 3)
    decisiones = [r["decision"] for r in resultados]
    decision_counts = {}
    for decision in decisiones:
        decision_counts[decision] = decision_counts.get(decision, 0) + 1
    
    plt.pie(decision_counts.values(), labels=decision_counts.keys(), autopct='%1.0f%%',
            colors=['green', 'orange', 'red'])
    plt.title('🎯 Distribución de Decisiones')
    
    # Subplot 4: Tasas de interés
    plt.subplot(2, 2, 4)
    nombres_aprobados = [r["perfil"]["nombre"] for r in resultados if r["tasa"]]
    tasas = [r["tasa"] for r in resultados if r["tasa"]]
    
    if tasas:
        plt.bar(nombres_aprobados, tasas, color='lightblue', alpha=0.7)
        plt.ylabel('Tasa de Interés (%)')
        plt.title('💸 Tasas Asignadas')
        plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()
    
    print("\n🎓 INSIGHTS DEL ALGORITMO:")
    print("   • El historial crediticio es el factor más determinante")
    print("   • Los ingresos altos no garantizan aprobación sin historial")
    print("   • La estabilidad laboral mejora significativamente el score")
    print("   • El ratio deuda/ingresos es crítico para la decisión final")

# ============================================================================
# 🎯 FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Función principal que ejecuta todo el ejemplo sobre aplicaciones de IA
    """
    print("🌟 EJEMPLO 04: APLICACIONES DE INTELIGENCIA ARTIFICIAL")
    print("=" * 80)
    
    while True:
        print("\n📋 MENÚ DE APLICACIONES:")
        print("1. 🏥 IA en Salud - Medicina y diagnóstico")
        print("2. 📊 Caso de estudio: IBM Watson Oncology")
        print("3. 🚗 IA en Transporte - Vehículos autónomos")
        print("4. 🤖 Simulador de dilemas éticos")
        print("5. 💰 IA en Finanzas - Servicios financieros")
        print("6. 🎮 Simulador de evaluación crediticia")
        print("7. 🚪 Salir")
        
        opcion = input("\n¿Qué aplicación quieres explorar? (1-7): ").strip()
        
        if opcion == "1":
            explorar_ia_salud()
        elif opcion == "2":
            caso_estudio_watson_oncology()
        elif opcion == "3":
            explorar_ia_transporte()
        elif opcion == "4":
            simulador_decision_vehiculo_autonomo()
        elif opcion == "5":
            explorar_ia_finanzas()
        elif opcion == "6":
            simulador_evaluacion_riesgo_credito()
        elif opcion == "7":
            print("\n🎉 ¡Has explorado el mundo real de aplicaciones de IA!")
            print("📚 Próximo paso: ejemplo_05_machine_learning.py")
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
    
    # Ejecutar programa principal
    main()

"""
🌟 APLICACIONES DE IA EXPLORADAS:

✅ 🏥 Salud y Medicina - Diagnóstico, fármacos, cirugía
✅ 🚗 Transporte - Vehículos autónomos y dilemas éticos  
✅ 💰 Finanzas - Fraude, trading, evaluación crediticia
✅ 📊 Casos de estudio reales - Éxitos y fracasos
✅ 🎮 Simuladores interactivos - Decisiones prácticas

🔍 SECTORES ANALIZADOS:
• Impacto económico y social de implementaciones
• Desafíos técnicos y éticos específicos
• Tendencias de adopción y proyecciones futuras
• Factores críticos de éxito y fracaso
• Métricas de evaluación de desempeño

🚀 PRÓXIMO PASO:
Ejecuta ejemplo_05_machine_learning.py para profundizar en los algoritmos
"""