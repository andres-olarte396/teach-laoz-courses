# 📏 Guía de Estilo - Curso IA y Automatización

## 🎯 Principios de Diseño del Curso

### 📚 **Convenciones de Contenido**

#### 🎨 **Formato Markdown**

- **Encabezados**: Usar jerarquía clara (H1 para títulos principales, H2 para secciones, etc.)
- **Emojis**: Uso consistente para navegación y categorización
- **Código**: Usar bloques de código con sintaxis highlighting
- **Enlaces**: Siempre con texto descriptivo, evitar "clic aquí"

#### 🎯 **Estructura de Módulos**

```markdown
# 📘 [Número] [Título del Módulo]

> **⏱️ Duración:** X horas | **📊 Peso:** Y% | **✅ Estado:** [Estado]

## 🎯 Objetivos del Módulo
- Objetivo 1
- Objetivo 2

## 📚 Contenido
### 🗂️ Unidad X.Y: [Título]
**⏱️ Duración:** X minutos

#### 📖 Contenido Teórico
[Desarrollo del tema]

#### 🧪 Práctica
[Ejercicios y laboratorios]

## 📋 Evaluación
[Criterios y métodos]
```

#### 🔤 **Convenciones de Nomenclatura**

- **Archivos**: kebab-case (ej: `fundamentos-ia.md`)
- **Directorios**: kebab-case (ej: `machine-learning/`)
- **IDs**: MAYÚSCULAS con guiones (ej: `AI-AUTO-001`)
- **Variables**: snake_case en código Python

### 🎨 **Sistema de Iconos**

#### 📚 **Contenido Educativo**

- 📘 Módulos principales
- 📗 Módulos secundarios  
- 📙 Módulos avanzados
- 📖 Contenido teórico
- 🧪 Laboratorios prácticos
- 📊 Evaluaciones

#### 🎯 **Navegación y Estado**

- ✅ Completado
- ⏳ En progreso
- 📋 Planificado
- ❌ Pendiente/Error
- 🔄 En revisión
- 🎯 Objetivo/Meta

#### 🔧 **Herramientas y Recursos**

- 🛠️ Herramientas
- 💻 Código/Scripts
- 📈 Métricas/Datos
- 🔗 Enlaces externos
- 📄 Documentos/PDFs
- 🎥 Videos

#### ⚠️ **Alertas y Notas**

- 💡 Tips/Consejos
- ⚠️ Advertencias
- 🚨 Errores críticos
- 📝 Notas importantes
- 🔍 Para investigar

### 📝 **Estilo de Escritura**

#### 🎯 **Tono y Voz**

- **Profesional pero accesible**: Evitar jerga innecesaria
- **Directo y claro**: Frases concisas, párrafos cortos
- **Inclusivo**: Usar lenguaje neutro e inclusivo
- **Motivacional**: Enfocado en el crecimiento del estudiante

#### 📖 **Estructura de Párrafos**

- **Párrafo introductorio**: Establece el contexto
- **Desarrollo**: Máximo 3-4 oraciones por párrafo
- **Párrafo de cierre**: Resume o conecta con el siguiente tema

#### 🔍 **Precisión Técnica**

- **Definiciones claras**: Definir términos técnicos al introducirlos
- **Ejemplos concretos**: Ilustrar conceptos abstractos
- **Referencias**: Citar fuentes cuando sea apropiado

### 💻 **Convenciones de Código**

#### 🐍 **Python**

```python
# Estilo PEP 8
# Comentarios descriptivos
# Nombres de variables descriptivos

def procesar_datos_ia(dataset, modelo="random_forest"):
    """
    Procesa datos para entrenamiento de IA.
    
    Args:
        dataset (pd.DataFrame): Datos de entrada
        modelo (str): Tipo de modelo a usar
    
    Returns:
        dict: Resultados del procesamiento
    """
    resultados = {}
    # Implementación aquí
    return resultados
```

#### 📊 **Jupyter Notebooks**

- **Título descriptivo** en la primera celda
- **Imports** en celdas separadas al inicio
- **Comentarios** en celdas markdown entre código
- **Outputs** visibles para demostración

### 🎨 **Diseño Visual**

#### 📐 **Espaciado y Layout**

- **Espacios en blanco**: Usar liberalmente para legibilidad
- **Listas**: Máximo 7 elementos por lista principal
- **Tablas**: Usar para comparaciones y datos estructurados
- **Diagramas**: Incluir cuando clarifique conceptos complejos

#### 🎨 **Colores y Énfasis**

- **Negrita**: Para términos clave y conceptos importantes
- **Cursiva**: Para énfasis sutil y definiciones
- **Código inline**: `Para comandos y variables`
- **Blockquotes**: > Para definiciones y conceptos clave

### 📚 **Estructura de Aprendizaje**

#### 🎯 **Progresión Pedagógica**

1. **Introducción**: Contexto y motivación
2. **Conceptos**: Definiciones y teoría
3. **Ejemplos**: Casos prácticos
4. **Práctica**: Ejercicios hands-on
5. **Evaluación**: Verificación de aprendizaje
6. **Síntesis**: Conexión con temas futuros

#### 🔄 **Metodología 70-20-10**

- **70% Práctica**: Laboratorios, ejercicios, proyectos
- **20% Colaboración**: Discusiones, peer review
- **10% Teoría**: Conceptos y fundamentos

### 📋 **Checklist de Calidad**

#### ✅ **Antes de Publicar**

- [ ] Ortografía y gramática revisadas
- [ ] Enlaces funcionando correctamente
- [ ] Código ejecutable y probado
- [ ] Imágenes con texto alternativo
- [ ] Estructura de navegación clara
- [ ] Objetivos de aprendizaje definidos
- [ ] Evaluación alineada con objetivos

#### 🔍 **Revisión de Contenido**

- [ ] Precisión técnica verificada
- [ ] Ejemplos relevantes y actuales
- [ ] Progresión lógica de conceptos
- [ ] Balance teoría-práctica apropiado
- [ ] Recursos adicionales incluidos

### 🔄 **Control de Versiones**

#### 📝 **Commits**

- **Formato**: `[tipo]: descripción breve`
- **Tipos**: feat, fix, docs, style, refactor, test
- **Ejemplos**:
  - `feat: agregar laboratorio de NLP`
  - `docs: actualizar guía de estilo`
  - `fix: corregir enlace roto en MOD2`

#### 🏷️ **Versionado**

- **Formato**: Semantic Versioning (X.Y.Z)
- **X**: Cambios mayores (estructura, contenido principal)
- **Y**: Nuevas características (módulos, laboratorios)
- **Z**: Correcciones menores (typos, enlaces)

---

## 🎯 Aplicación Práctica

### 📖 **Ejemplo de Sección Bien Formateada**

```markdown
## 🧠 Machine Learning Supervisado

> **💡 Concepto Clave:** El aprendizaje supervisado utiliza datos etiquetados para entrenar modelos que puedan hacer predicciones sobre nuevos datos.

### 🎯 Objetivos de Aprendizaje
- Distinguir entre clasificación y regresión
- Implementar algoritmos básicos de ML supervisado
- Evaluar la performance de modelos predictivos

### 📚 Algoritmos Principales

#### 🔍 **Regresión Lineal**
La regresión lineal busca la mejor línea recta que se ajuste a los datos.

```python
from sklearn.linear_model import LinearRegression

# Ejemplo práctico
modelo = LinearRegression()
modelo.fit(X_train, y_train)
predicciones = modelo.predict(X_test)
```

#### 🌳 **Árboles de Decisión**

Los árboles de decisión crean reglas de decisión en forma de árbol.

**Ventajas:**

- Fácil interpretación
- No requiere normalización de datos
- Maneja variables categóricas y numéricas

**Desventajas:**

- Propenso al overfitting
- Inestable con pequeños cambios en datos

```

---

*Guía de Estilo v1.0 | Actualizada: 13 de octubre de 2025 | Autor: Andres Olarte*
