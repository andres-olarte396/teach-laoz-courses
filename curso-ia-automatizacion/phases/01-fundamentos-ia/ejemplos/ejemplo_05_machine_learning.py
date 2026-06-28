"""
🤖 EJEMPLO 05: Introducción al Machine Learning
===============================================

📚 OBJETIVOS DE APRENDIZAJE:
• Comprender el proceso completo de Machine Learning
• Implementar algoritmos básicos de clasificación y regresión
• Evaluar modelos usando métricas apropiadas
• Identificar y solucionar problemas comunes
• Desarrollar un proyecto completo de ML desde cero

🎯 NIVEL: Intermedio-Avanzado - Implementación práctica
⏱️ TIEMPO ESTIMADO: 90-120 minutos
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import confusion_matrix, classification_report, mean_squared_error, r2_score
from sklearn.datasets import make_classification, make_regression
import warnings
warnings.filterwarnings('ignore')

# ============================================================================
# 📊 PARTE 1: FUNDAMENTOS DEL PROCESO DE MACHINE LEARNING
# ============================================================================

def introducir_proceso_ml():
    """
    Introduce el proceso completo de Machine Learning
    """
    print("=" * 70)
    print("📊 EL PROCESO DE MACHINE LEARNING")
    print("=" * 70)
    
    fases = {
        "1. 🎯 Definición del Problema": {
            "descripcion": "Identificar qué queremos predecir y por qué",
            "preguntas": [
                "¿Es un problema de clasificación o regresión?",
                "¿Qué datos necesitamos?", 
                "¿Cuál es el criterio de éxito?"
            ],
            "ejemplo": "Predecir si un email es spam (clasificación binaria)"
        },
        "2. 📥 Recolección de Datos": {
            "descripcion": "Obtener y reunir datos relevantes",
            "preguntas": [
                "¿Tenemos suficientes datos?",
                "¿Los datos son representativos?",
                "¿Hay problemas de calidad?"
            ],
            "ejemplo": "1000 emails etiquetados como spam/no-spam"
        },
        "3. 🔍 Exploración de Datos": {
            "descripcion": "Analizar y entender los datos",
            "preguntas": [
                "¿Qué patrones vemos?",
                "¿Hay valores faltantes?",
                "¿Existen outliers?"
            ],
            "ejemplo": "Analizar frecuencia de palabras, longitud de emails"
        },
        "4. 🧹 Preparación de Datos": {
            "descripcion": "Limpiar y transformar los datos",
            "preguntas": [
                "¿Cómo manejar valores faltantes?",
                "¿Necesitamos normalizar?",
                "¿Qué features crear?"
            ],
            "ejemplo": "Convertir texto a vectores, normalizar longitudes"
        },
        "5. 🤖 Selección de Modelo": {
            "descripcion": "Elegir algoritmo apropiado",
            "preguntas": [
                "¿Qué algoritmos son adecuados?",
                "¿Necesitamos interpretabilidad?",
                "¿Cuántos datos tenemos?"
            ],
            "ejemplo": "Probar Naive Bayes, SVM, Random Forest"
        },
        "6. 🏋️ Entrenamiento": {
            "descripcion": "Ajustar el modelo a los datos",
            "preguntas": [
                "¿Cómo dividir train/validation/test?",
                "¿Qué hiperparámetros usar?",
                "¿Hay overfitting?"
            ],
            "ejemplo": "Entrenar con 70% datos, validar con 15%"
        },
        "7. ⚖️ Evaluación": {
            "descripcion": "Medir rendimiento del modelo",
            "preguntas": [
                "¿Qué métricas usar?",
                "¿El modelo generaliza bien?",
                "¿Es suficientemente bueno?"
            ],
            "ejemplo": "Accuracy 95%, Precision 94%, Recall 96%"
        },
        "8. 🚀 Despliegue": {
            "descripcion": "Poner el modelo en producción",
            "preguntas": [
                "¿Cómo integrarlo al sistema?",
                "¿Cómo monitorear rendimiento?",
                "¿Cuándo reentrenar?"
            ],
            "ejemplo": "API que clasifica emails en tiempo real"
        }
    }
    
    # Mostrar proceso detallado
    for fase, info in fases.items():
        print(f"\n{fase}")
        print(f"   📖 {info['descripcion']}")
        print("   🤔 Preguntas clave:")
        for pregunta in info['preguntas']:
            print(f"      • {pregunta}")
        print(f"   💡 Ejemplo: {info['ejemplo']}")
    
    # Crear diagrama de flujo visual
    plt.figure(figsize=(14, 10))
    
    # Coordenadas para el diagrama de flujo
    fases_nombres = [fase.split('. ')[1] for fase in fases.keys()]
    posiciones = [
        (2, 8), (2, 6), (2, 4), (2, 2),  # Columna izquierda
        (6, 2), (6, 4), (6, 6), (6, 8)   # Columna derecha
    ]
    
    # Dibujar nodos
    for i, (nombre, pos) in enumerate(zip(fases_nombres, posiciones)):
        color = plt.cm.Set3(i / len(fases_nombres))
        plt.scatter(pos[0], pos[1], s=2000, c=[color], alpha=0.7)
        plt.text(pos[0], pos[1], nombre, ha='center', va='center', 
                fontsize=8, fontweight='bold', wrap=True)
    
    # Dibujar conexiones (flujo del proceso)
    conexiones = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7)]
    for i, (inicio, fin) in enumerate(conexiones):
        pos_inicio = posiciones[inicio]
        pos_fin = posiciones[fin]
        
        # Crear flecha curvada
        if inicio < 4 and fin < 4:  # Misma columna
            plt.arrow(pos_inicio[0], pos_inicio[1] - 0.3,
                     0, pos_fin[1] - pos_inicio[1] + 0.6,
                     head_width=0.2, head_length=0.2, fc='gray', ec='gray')
        elif inicio == 3 and fin == 4:  # Cambio de columna
            plt.arrow(pos_inicio[0] + 0.3, pos_inicio[1],
                     pos_fin[0] - pos_inicio[0] - 0.6, 0,
                     head_width=0.2, head_length=0.2, fc='gray', ec='gray')
        elif inicio >= 4 and fin >= 4:  # Segunda columna
            plt.arrow(pos_inicio[0], pos_inicio[1] + 0.3,
                     0, pos_fin[1] - pos_inicio[1] - 0.6,
                     head_width=0.2, head_length=0.2, fc='gray', ec='gray')
    
    plt.xlim(0, 8)
    plt.ylim(0, 10)
    plt.title('🔄 Proceso Completo de Machine Learning', fontsize=16, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    
    print("\n🎓 PUNTOS CLAVE DEL PROCESO:")
    print("   • Es iterativo: puedes volver a fases anteriores")
    print("   • La calidad de los datos es más importante que el algoritmo")
    print("   • La evaluación debe ser rigurosa y realista")
    print("   • El despliegue es tan importante como el desarrollo")

# ============================================================================
# 🧠 PARTE 2: TIPOS DE APRENDIZAJE AUTOMÁTICO
# ============================================================================

def explorar_tipos_aprendizaje():
    """
    Explora los diferentes tipos de aprendizaje automático con ejemplos
    """
    print("\n" + "=" * 70)
    print("🧠 TIPOS DE APRENDIZAJE AUTOMÁTICO")
    print("=" * 70)
    
    tipos = {
        "🎯 Aprendizaje Supervisado": {
            "definicion": "Aprende de ejemplos con respuestas conocidas",
            "caracteristicas": [
                "Datos etiquetados (X, y)",
                "Objetivo: predecir etiquetas",
                "Evaluación con datos de prueba"
            ],
            "subtipos": {
                "Clasificación": "Predice categorías discretas",
                "Regresión": "Predice valores continuos"
            },
            "algoritmos": ["Regresión Lineal", "SVM", "Random Forest", "Redes Neuronales"],
            "ejemplos": ["Detección de spam", "Reconocimiento de imágenes", "Predicción de precios"]
        },
        "🔍 Aprendizaje No Supervisado": {
            "definicion": "Encuentra patrones en datos sin etiquetas",
            "caracteristicas": [
                "Solo datos de entrada (X)",
                "Objetivo: descubrir estructura",
                "Evaluación más subjetiva"
            ],
            "subtipos": {
                "Clustering": "Agrupa datos similares",
                "Reducción de dimensionalidad": "Simplifica datos",
                "Detección de anomalías": "Encuentra outliers"
            },
            "algoritmos": ["K-Means", "PCA", "DBSCAN", "Autoencoders"],
            "ejemplos": ["Segmentación de clientes", "Compresión de datos", "Detección de fraude"]
        },
        "🎮 Aprendizaje por Refuerzo": {
            "definicion": "Aprende mediante prueba y error con recompensas",
            "caracteristicas": [
                "Interacción con ambiente",
                "Objetivo: maximizar recompensa",
                "Equilibrio exploración/explotación"
            ],
            "subtipos": {
                "Model-free": "Sin modelo del ambiente",
                "Model-based": "Con modelo del ambiente",
                "Policy-based": "Aprende política directamente"
            },
            "algoritmos": ["Q-Learning", "Policy Gradient", "Actor-Critic", "PPO"],
            "ejemplos": ["Juegos", "Robótica", "Trading automático", "Vehículos autónomos"]
        }
    }
    
    # Mostrar información detallada
    for tipo, info in tipos.items():
        print(f"\n{tipo}")
        print(f"   📖 Definición: {info['definicion']}")
        print("   🔍 Características:")
        for caracteristica in info['caracteristicas']:
            print(f"      • {caracteristica}")
        print("   📊 Subtipos:")
        for subtipo, desc in info['subtipos'].items():
            print(f"      • {subtipo}: {desc}")
        print(f"   🤖 Algoritmos: {', '.join(info['algoritmos'])}")
        print(f"   💡 Ejemplos: {', '.join(info['ejemplos'])}")
    
    # Crear visualización comparativa
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Gráfico 1: Popularidad de tipos (simulado)
    tipos_nombres = ['Supervisado', 'No Supervisado', 'Por Refuerzo']
    popularidad = [70, 25, 5]  # Porcentajes aproximados de uso
    colores = ['lightblue', 'lightgreen', 'orange']
    
    ax1.pie(popularidad, labels=tipos_nombres, autopct='%1.1f%%', 
           colors=colores, startangle=90)
    ax1.set_title('📊 Popularidad de Tipos de ML')
    
    # Gráfico 2: Dificultad de implementación vs Interpretabilidad
    dificultad = [6, 7, 9]      # 1-10 scale
    interpretabilidad = [7, 4, 3]  # 1-10 scale
    
    ax2.scatter(dificultad, interpretabilidad, s=300, c=colores, alpha=0.7)
    ax2.set_xlabel('Dificultad de Implementación')
    ax2.set_ylabel('Interpretabilidad')
    ax2.set_title('🎯 Dificultad vs Interpretabilidad')
    ax2.grid(True, alpha=0.3)
    
    for i, nombre in enumerate(tipos_nombres):
        ax2.annotate(nombre, (dificultad[i], interpretabilidad[i]),
                    xytext=(5, 5), textcoords='offset points', fontsize=9)
    
    # Gráfico 3: Cantidad de datos requeridos
    datos_requeridos = [1000, 10000, 100000]  # Ejemplos típicos
    ax3.bar(tipos_nombres, datos_requeridos, color=colores, alpha=0.7)
    ax3.set_ylabel('Ejemplos de Entrenamiento')
    ax3.set_title('📈 Datos Típicamente Requeridos')
    ax3.set_yscale('log')
    
    # Gráfico 4: Timeline de desarrollo
    años_desarrollo = [1950, 1960, 1980]  # Aproximados
    ax4.scatter(años_desarrollo, range(len(tipos_nombres)), 
               s=300, c=colores, alpha=0.7)
    ax4.set_xlabel('Año de Desarrollo')
    ax4.set_yticks(range(len(tipos_nombres)))
    ax4.set_yticklabels(tipos_nombres)
    ax4.set_title('📅 Evolución Histórica')
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()

# ============================================================================
# 🔧 PARTE 3: IMPLEMENTACIÓN PRÁCTICA DE ALGORITMOS
# ============================================================================

def implementar_clasificacion():
    """
    Implementa y compara algoritmos de clasificación
    """
    print("\n" + "=" * 70)
    print("🔧 IMPLEMENTACIÓN: ALGORITMOS DE CLASIFICACIÓN")
    print("=" * 70)
    
    # Generar dataset sintético
    print("📊 Generando dataset sintético...")
    X, y = make_classification(
        n_samples=1000,
        n_features=10,
        n_informative=5,
        n_redundant=2,
        n_clusters_per_class=1,
        random_state=42
    )
    
    # Dividir datos
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    # Normalizar datos
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    print(f"   • Dataset: {X.shape[0]} muestras, {X.shape[1]} características")
    print(f"   • Entrenamiento: {X_train.shape[0]} muestras")
    print(f"   • Prueba: {X_test.shape[0]} muestras")
    print(f"   • Clases: {len(np.unique(y))} (distribución: {np.bincount(y)})")
    
    # Definir algoritmos a probar
    algoritmos = {
        "Regresión Logística": LogisticRegression(random_state=42),
        "Árbol de Decisión": DecisionTreeClassifier(random_state=42),
        "Random Forest": RandomForestClassifier(n_estimators=100, random_state=42),
        "SVM": SVC(random_state=42),
        "K-Nearest Neighbors": KNeighborsClassifier(n_neighbors=5)
    }
    
    resultados = {}
    
    print("\n🤖 Entrenando y evaluando algoritmos...")
    for nombre, modelo in algoritmos.items():
        print(f"\n   Procesando {nombre}...")
        
        # Entrenar modelo
        if nombre == "SVM" or nombre == "K-Nearest Neighbors":
            modelo.fit(X_train_scaled, y_train)
            y_pred = modelo.predict(X_test_scaled)
        else:
            modelo.fit(X_train, y_train)
            y_pred = modelo.predict(X_test)
        
        # Calcular métricas
        accuracy = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted')
        recall = recall_score(y_test, y_pred, average='weighted')
        f1 = f1_score(y_test, y_pred, average='weighted')
        
        # Validación cruzada
        if nombre == "SVM" or nombre == "K-Nearest Neighbors":
            cv_scores = cross_val_score(modelo, X_train_scaled, y_train, cv=5)
        else:
            cv_scores = cross_val_score(modelo, X_train, y_train, cv=5)
        
        resultados[nombre] = {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1': f1,
            'cv_mean': cv_scores.mean(),
            'cv_std': cv_scores.std(),
            'predictions': y_pred
        }
        
        print(f"      Accuracy: {accuracy:.3f}")
        print(f"      Precision: {precision:.3f}")
        print(f"      Recall: {recall:.3f}")
        print(f"      F1-Score: {f1:.3f}")
        print(f"      CV Score: {cv_scores.mean():.3f} (±{cv_scores.std():.3f})")
    
    # Crear tabla comparativa
    print("\n📊 RESUMEN COMPARATIVO:")
    df_resultados = pd.DataFrame({
        nombre: {
            'Accuracy': res['accuracy'],
            'Precision': res['precision'],
            'Recall': res['recall'],
            'F1-Score': res['f1'],
            'CV Score': res['cv_mean']
        }
        for nombre, res in resultados.items()
    }).T
    
    print(df_resultados.round(3).to_string())
    
    # Visualizar resultados
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Gráfico 1: Comparación de métricas
    metricas = ['Accuracy', 'Precision', 'Recall', 'F1-Score']
    x = np.arange(len(algoritmos))
    width = 0.2
    
    for i, metrica in enumerate(metricas):
        valores = [resultados[alg][metrica.lower().replace('-', '_')] for alg in algoritmos.keys()]
        ax1.bar(x + i*width, valores, width, label=metrica, alpha=0.8)
    
    ax1.set_xlabel('Algoritmos')
    ax1.set_ylabel('Puntuación')
    ax1.set_title('📊 Comparación de Métricas')
    ax1.set_xticks(x + width * 1.5)
    ax1.set_xticklabels(list(algoritmos.keys()), rotation=45, ha='right')
    ax1.legend()
    ax1.grid(True, alpha=0.3, axis='y')
    
    # Gráfico 2: Validación cruzada
    nombres_alg = list(algoritmos.keys())
    cv_means = [resultados[alg]['cv_mean'] for alg in nombres_alg]
    cv_stds = [resultados[alg]['cv_std'] for alg in nombres_alg]
    
    ax2.bar(nombres_alg, cv_means, yerr=cv_stds, capsize=5, alpha=0.7, color='lightblue')
    ax2.set_ylabel('CV Score')
    ax2.set_title('🎯 Validación Cruzada (5-fold)')
    ax2.tick_params(axis='x', rotation=45)
    ax2.grid(True, alpha=0.3, axis='y')
    
    # Gráfico 3: Matriz de confusión del mejor modelo
    mejor_modelo = max(resultados.keys(), key=lambda k: resultados[k]['accuracy'])
    cm = confusion_matrix(y_test, resultados[mejor_modelo]['predictions'])
    
    im = ax3.imshow(cm, interpolation='nearest', cmap=plt.cm.Blues)
    ax3.figure.colorbar(im, ax=ax3)
    ax3.set_title(f'🎯 Matriz de Confusión - {mejor_modelo}')
    
    # Añadir valores a la matriz
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax3.text(j, i, format(cm[i, j], 'd'),
                    ha="center", va="center",
                    color="white" if cm[i, j] > thresh else "black")
    
    ax3.set_ylabel('Etiqueta Real')
    ax3.set_xlabel('Etiqueta Predicha')
    
    # Gráfico 4: Ranking de modelos
    ranking = sorted(algoritmos.keys(), key=lambda k: resultados[k]['accuracy'], reverse=True)
    accuracies = [resultados[alg]['accuracy'] for alg in ranking]
    
    bars = ax4.barh(ranking, accuracies, color='lightgreen', alpha=0.7)
    ax4.set_xlabel('Accuracy')
    ax4.set_title('🏆 Ranking de Modelos')
    
    # Añadir valores
    for bar, acc in zip(bars, accuracies):
        ax4.text(bar.get_width() + 0.001, bar.get_y() + bar.get_height()/2,
                f'{acc:.3f}', va='center', fontweight='bold')
    
    plt.tight_layout()
    plt.show()
    
    print(f"\n🏆 MEJOR MODELO: {mejor_modelo}")
    print(f"   📊 Accuracy: {resultados[mejor_modelo]['accuracy']:.3f}")
    print(f"   🎯 CV Score: {resultados[mejor_modelo]['cv_mean']:.3f}")

def implementar_regresion():
    """
    Implementa y evalúa un modelo de regresión
    """
    print("\n" + "=" * 70)
    print("📈 IMPLEMENTACIÓN: REGRESIÓN LINEAL")
    print("=" * 70)
    
    # Generar dataset sintético
    print("📊 Generando dataset de regresión...")
    X, y = make_regression(
        n_samples=500,
        n_features=3,
        n_informative=3,
        noise=10,
        random_state=42
    )
    
    # Crear nombres de características más descriptivos
    feature_names = ['Experiencia (años)', 'Educación (nivel)', 'Ubicación (índice)']
    
    # Dividir datos
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print(f"   • Prediciendo: Salario (variable continua)")
    print(f"   • Características: {', '.join(feature_names)}")
    print(f"   • Datos entrenamiento: {X_train.shape[0]}")
    print(f"   • Datos prueba: {X_test.shape[0]}")
    
    # Entrenar modelo
    modelo = LinearRegression()
    modelo.fit(X_train, y_train)
    
    # Hacer predicciones
    y_pred_train = modelo.predict(X_train)
    y_pred_test = modelo.predict(X_test)
    
    # Calcular métricas
    mse_train = mean_squared_error(y_train, y_pred_train)
    mse_test = mean_squared_error(y_test, y_pred_test)
    r2_train = r2_score(y_train, y_pred_train)
    r2_test = r2_score(y_test, y_pred_test)
    
    print(f"\n📊 MÉTRICAS DEL MODELO:")
    print(f"   🎯 Entrenamiento:")
    print(f"      MSE: {mse_train:.2f}")
    print(f"      R²: {r2_train:.3f}")
    print(f"   🎯 Prueba:")
    print(f"      MSE: {mse_test:.2f}")
    print(f"      R²: {r2_test:.3f}")
    
    # Mostrar coeficientes
    print(f"\n🔍 COEFICIENTES DEL MODELO:")
    print(f"   📊 Intercepto: {modelo.intercept_:.2f}")
    for i, (nombre, coef) in enumerate(zip(feature_names, modelo.coef_)):
        print(f"   📊 {nombre}: {coef:.2f}")
    
    # Visualizar resultados
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 12))
    
    # Gráfico 1: Predicciones vs Valores Reales
    ax1.scatter(y_test, y_pred_test, alpha=0.7, color='blue', label='Predicciones')
    ax1.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], 
             'r--', lw=2, label='Predicción Perfecta')
    ax1.set_xlabel('Valores Reales')
    ax1.set_ylabel('Predicciones')
    ax1.set_title('🎯 Predicciones vs Valores Reales')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Gráfico 2: Residuos
    residuos = y_test - y_pred_test
    ax2.scatter(y_pred_test, residuos, alpha=0.7, color='green')
    ax2.axhline(y=0, color='red', linestyle='--')
    ax2.set_xlabel('Predicciones')
    ax2.set_ylabel('Residuos')
    ax2.set_title('📊 Análisis de Residuos')
    ax2.grid(True, alpha=0.3)
    
    # Gráfico 3: Importancia de características
    importancias = np.abs(modelo.coef_)
    nombres_cortos = ['Experiencia', 'Educación', 'Ubicación']
    
    bars = ax3.bar(nombres_cortos, importancias, color='orange', alpha=0.7)
    ax3.set_ylabel('Importancia (|coeficiente|)')
    ax3.set_title('📊 Importancia de Características')
    
    # Añadir valores
    for bar, imp in zip(bars, importancias):
        ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{imp:.1f}', ha='center', va='bottom', fontweight='bold')
    
    # Gráfico 4: Distribución de residuos
    ax4.hist(residuos, bins=20, alpha=0.7, color='purple', edgecolor='black')
    ax4.axvline(x=0, color='red', linestyle='--', linewidth=2)
    ax4.set_xlabel('Residuos')
    ax4.set_ylabel('Frecuencia')
    ax4.set_title('📈 Distribución de Residuos')
    ax4.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Hacer predicciones de ejemplo
    print(f"\n🔮 PREDICCIONES DE EJEMPLO:")
    ejemplos = [
        [5, 3, 2],   # 5 años exp, nivel 3 educación, ubicación 2
        [10, 4, 4],  # 10 años exp, nivel 4 educación, ubicación 4
        [2, 2, 1]    # 2 años exp, nivel 2 educación, ubicación 1
    ]
    
    predicciones = modelo.predict(ejemplos)
    
    for i, (ejemplo, pred) in enumerate(zip(ejemplos, predicciones)):
        print(f"   Candidato {i+1}:")
        print(f"      Experiencia: {ejemplo[0]} años")
        print(f"      Educación: Nivel {ejemplo[1]}")
        print(f"      Ubicación: Índice {ejemplo[2]}")
        print(f"      💰 Salario predicho: ${pred:,.0f}")
        print()

# ============================================================================
# 🚨 PARTE 4: PROBLEMAS COMUNES Y SOLUCIONES
# ============================================================================

def demostrar_overfitting():
    """
    Demuestra el problema de overfitting y cómo detectarlo
    """
    print("\n" + "=" * 70)
    print("🚨 PROBLEMA: OVERFITTING (SOBREAJUSTE)")
    print("=" * 70)
    
    print("📖 DEFINICIÓN:")
    print("   El overfitting ocurre cuando un modelo aprende demasiado bien")
    print("   los datos de entrenamiento, incluyendo ruido y patrones específicos")
    print("   que no se generalizan a datos nuevos.")
    
    # Generar datos con poco ruido
    np.random.seed(42)
    X = np.linspace(0, 1, 50).reshape(-1, 1)
    y_true = 1.5 * X.ravel() + 0.3 * np.sin(15 * X.ravel())
    y = y_true + 0.1 * np.random.normal(size=X.shape[0])
    
    # Dividir datos
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    
    # Crear polinomios de diferentes grados (complejidad)
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.pipeline import Pipeline
    
    grados = [1, 3, 7, 15]
    resultados_overfit = {}
    
    # Datos para visualización
    X_plot = np.linspace(0, 1, 100).reshape(-1, 1)
    
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    axes = axes.ravel()
    
    for i, grado in enumerate(grados):
        # Crear pipeline con características polinómicas
        modelo = Pipeline([
            ('poly', PolynomialFeatures(grado)),
            ('linear', LinearRegression())
        ])
        
        # Entrenar
        modelo.fit(X_train, y_train)
        
        # Predicciones
        y_pred_train = modelo.predict(X_train)
        y_pred_test = modelo.predict(X_test)
        y_pred_plot = modelo.predict(X_plot)
        
        # Métricas
        mse_train = mean_squared_error(y_train, y_pred_train)
        mse_test = mean_squared_error(y_test, y_pred_test)
        r2_train = r2_score(y_train, y_pred_train)
        r2_test = r2_score(y_test, y_pred_test)
        
        resultados_overfit[f'Grado {grado}'] = {
            'mse_train': mse_train,
            'mse_test': mse_test,
            'r2_train': r2_train,
            'r2_test': r2_test,
            'gap': r2_train - r2_test  # Brecha indica overfitting
        }
        
        # Visualizar
        ax = axes[i]
        ax.scatter(X_train, y_train, alpha=0.7, color='blue', label='Entrenamiento')
        ax.scatter(X_test, y_test, alpha=0.7, color='red', label='Prueba')
        ax.plot(X_plot, y_pred_plot, color='green', linewidth=2, label='Modelo')
        ax.set_title(f'Polinomio Grado {grado}\nR² Train: {r2_train:.3f}, Test: {r2_test:.3f}')
        ax.legend()
        ax.grid(True, alpha=0.3)
        
        # Diagnóstico
        if r2_train - r2_test > 0.1:
            ax.text(0.05, 0.95, '🚨 OVERFITTING', transform=ax.transAxes, 
                   bbox=dict(boxstyle="round,pad=0.3", facecolor="red", alpha=0.7),
                   fontweight='bold', color='white', va='top')
        elif r2_test < 0.7:
            ax.text(0.05, 0.95, '⚠️ UNDERFITTING', transform=ax.transAxes,
                   bbox=dict(boxstyle="round,pad=0.3", facecolor="orange", alpha=0.7),
                   fontweight='bold', color='white', va='top')
        else:
            ax.text(0.05, 0.95, '✅ GOOD FIT', transform=ax.transAxes,
                   bbox=dict(boxstyle="round,pad=0.3", facecolor="green", alpha=0.7),
                   fontweight='bold', color='white', va='top')
    
    plt.tight_layout()
    plt.show()
    
    # Mostrar tabla de resultados
    print("\n📊 ANÁLISIS DE COMPLEJIDAD DEL MODELO:")
    df_overfit = pd.DataFrame(resultados_overfit).T
    print(df_overfit.round(3).to_string())
    
    # Visualizar curvas de aprendizaje
    plt.figure(figsize=(12, 6))
    
    grados_plot = list(range(1, 16))
    train_scores = []
    test_scores = []
    
    for grado in grados_plot:
        modelo = Pipeline([
            ('poly', PolynomialFeatures(grado)),
            ('linear', LinearRegression())
        ])
        modelo.fit(X_train, y_train)
        
        train_score = r2_score(y_train, modelo.predict(X_train))
        test_score = r2_score(y_test, modelo.predict(X_test))
        
        train_scores.append(train_score)
        test_scores.append(test_score)
    
    plt.plot(grados_plot, train_scores, 'o-', label='Entrenamiento', linewidth=2)
    plt.plot(grados_plot, test_scores, 'o-', label='Validación', linewidth=2)
    plt.xlabel('Complejidad del Modelo (Grado Polinómico)')
    plt.ylabel('R² Score')
    plt.title('📈 Curvas de Validación: Detección de Overfitting')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Marcar zona óptima
    mejor_grado = grados_plot[np.argmax(test_scores)]
    plt.axvline(x=mejor_grado, color='red', linestyle='--', alpha=0.7, 
               label=f'Óptimo (Grado {mejor_grado})')
    plt.legend()
    
    plt.tight_layout()
    plt.show()
    
    print(f"\n🎯 CONCLUSIONES:")
    print(f"   • Grado óptimo: {mejor_grado}")
    print(f"   • Modelos simples (grado 1): Underfitting")
    print(f"   • Modelos complejos (grado >10): Overfitting")
    print(f"   • La brecha train-test indica sobreajuste")
    print(f"   • Usar validación cruzada para seleccionar complejidad")

# ============================================================================
# 🎯 FUNCIÓN PRINCIPAL
# ============================================================================

def main():
    """
    Función principal que ejecuta todo el ejemplo de Machine Learning
    """
    print("🤖 EJEMPLO 05: INTRODUCCIÓN AL MACHINE LEARNING")
    print("=" * 80)
    
    while True:
        print("\n📋 MENÚ DE MACHINE LEARNING:")
        print("1. 📊 Proceso de Machine Learning - Flujo completo")
        print("2. 🧠 Tipos de aprendizaje - Supervisado, no supervisado, refuerzo")
        print("3. 🔧 Clasificación práctica - Implementar algoritmos")
        print("4. 📈 Regresión práctica - Modelo predictivo")
        print("5. 🚨 Overfitting - Problema y soluciones")
        print("6. 🚪 Salir")
        
        opcion = input("\n¿Qué aspecto de ML quieres explorar? (1-6): ").strip()
        
        if opcion == "1":
            introducir_proceso_ml()
        elif opcion == "2":
            explorar_tipos_aprendizaje()
        elif opcion == "3":
            implementar_clasificacion()
        elif opcion == "4":
            implementar_regresion()
        elif opcion == "5":
            demostrar_overfitting()
        elif opcion == "6":
            print("\n🎉 ¡Has completado la introducción a Machine Learning!")
            print("📚 Continúa con los ejemplos avanzados o proyectos integradores")
            break
        else:
            print("❌ Opción no válida. Por favor, elige entre 1-6.")

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
🤖 MACHINE LEARNING DOMINADO:

✅ 📊 Proceso completo de ML - 8 fases del desarrollo
✅ 🧠 Tipos de aprendizaje - Supervisado, no supervisado, refuerzo
✅ 🔧 Implementación práctica - Clasificación con 5 algoritmos
✅ 📈 Regresión lineal - Predicción de valores continuos
✅ 🚨 Overfitting - Detección y prevención

🔍 ALGORITMOS IMPLEMENTADOS:
• Regresión Logística
• Árboles de Decisión  
• Random Forest
• Support Vector Machines
• K-Nearest Neighbors
• Regresión Lineal

📊 MÉTRICAS DOMINADAS:
• Accuracy, Precision, Recall, F1-Score
• Mean Squared Error, R² Score
• Validación cruzada
• Análisis de residuos
• Matrices de confusión

🚀 PRÓXIMOS PASOS:
Explora proyectos integradores que combinen todo lo aprendido
en Phase 1: Fundamentos de IA
"""