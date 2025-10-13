# 🛠️ Herramientas - Curso IA y Automatización

## 🎯 Stack Tecnológico Requerido

### 🐍 **Python Ecosystem**

#### 📦 **Distribución Base**

- **Python 3.9+**: Lenguaje principal del curso
- **Anaconda/Miniconda**: Gestor de entornos y paquetes
- **pip**: Instalador de paquetes Python alternativo

#### 📊 **Data Science Libraries**

```bash
# Instalación de dependencias principales
conda install numpy pandas matplotlib seaborn plotly
pip install scikit-learn tensorflow keras torch torchvision
```

| Librería | Versión | Propósito |
|----------|---------|-----------|
| `numpy` | 1.24+ | Computación numérica |
| `pandas` | 2.0+ | Manipulación de datos |
| `matplotlib` | 3.7+ | Visualización básica |
| `seaborn` | 0.12+ | Visualización estadística |
| `plotly` | 5.15+ | Visualización interactiva |
| `scikit-learn` | 1.3+ | Machine Learning clásico |
| `tensorflow` | 2.13+ | Deep Learning |
| `pytorch` | 2.0+ | Deep Learning alternativo |

#### 🤖 **IA y NLP Libraries**

```bash
# Instalación de librerías especializadas
pip install transformers openai langchain chromadb
pip install spacy nltk textstat
python -m spacy download es_core_news_sm
```

| Librería | Versión | Propósito |
|----------|---------|-----------|
| `transformers` | 4.30+ | Modelos pre-entrenados |
| `openai` | 0.27+ | API de OpenAI (GPT, DALL-E) |
| `langchain` | 0.0.200+ | Framework para LLM apps |
| `spacy` | 3.6+ | Procesamiento de lenguaje natural |
| `nltk` | 3.8+ | Toolkit de NLP |

#### 🔄 **Automatización Libraries**

```bash
# Instalación de herramientas de automatización
pip install selenium beautifulsoup4 requests
pip install openpyxl xlsxwriter python-docx
pip install schedule APScheduler
```

| Librería | Versión | Propósito |
|----------|---------|-----------|
| `selenium` | 4.10+ | Automatización web |
| `beautifulsoup4` | 4.12+ | Web scraping |
| `requests` | 2.31+ | HTTP client |
| `openpyxl` | 3.1+ | Manipulación Excel |
| `schedule` | 1.2+ | Programación de tareas |

### 💻 **Entornos de Desarrollo**

#### 📓 **Jupyter Ecosystem**

- **JupyterLab**: Entorno principal para experimentación
- **Jupyter Notebook**: Notebooks clásicos
- **Google Colab**: Entorno cloud con GPU gratuita
- **Kaggle Kernels**: Kernels para competencias

#### 🎨 **IDEs y Editores**

- **VS Code**: Editor principal con extensiones Python
- **PyCharm Community**: IDE dedicado para Python
- **Sublime Text**: Editor ligero para scripts rápidos

#### ⚙️ **Extensiones VS Code Recomendadas**

```json
{
  "recommendations": [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-toolsai.jupyter",
    "ms-vscode.vscode-json",
    "streetsidesoftware.code-spell-checker",
    "ms-python.black-formatter"
  ]
}
```

### ☁️ **Plataformas Cloud**

#### 🌐 **Servicios de IA**

- **OpenAI API**: GPT-4, DALL-E, Whisper
- **Google Cloud AI**: Vertex AI, AutoML
- **AWS SageMaker**: ML platform completa
- **Azure Cognitive Services**: APIs de IA pre-construidas

#### 💾 **Almacenamiento y Bases de Datos**

- **Google Drive**: Almacenamiento de datasets
- **SQLite**: Base de datos local para desarrollo
- **PostgreSQL**: Base de datos para producción
- **MongoDB**: Base de datos NoSQL para documentos

### 🤖 **Herramientas RPA**

#### 🏢 **Plataformas Enterprise**

- **UiPath Community**: Plataforma RPA completa
- **Microsoft Power Automate**: Automatización low-code
- **Automation Anywhere Community**: Bot marketplace

#### 🔧 **Herramientas Open Source**

- **Robot Framework**: Framework de automatización
- **Sikuli**: Automatización visual
- **AutoHotkey**: Automatización de Windows

### 🌐 **Herramientas Web**

#### 🔍 **APIs y Servicios**

- **Postman**: Testing de APIs
- **Insomnia**: Cliente REST alternativo
- **curl**: Cliente HTTP de línea de comandos

#### 🌍 **Navegadores y Testing**

- **Chrome/Chromium**: Navegador principal con DevTools
- **Firefox**: Navegador alternativo
- **ChromeDriver**: Driver para Selenium
- **GeckoDriver**: Driver para Firefox

### 📊 **Visualización y Dashboards**

#### 📈 **Librerías Python**

- **Streamlit**: Apps web rápidas
- **Dash**: Dashboards interactivos
- **Gradio**: Interfaces para modelos ML

#### 🎨 **Herramientas Externas**

- **Tableau Public**: Visualización avanzada
- **Power BI**: Business intelligence
- **D3.js**: Visualización web custom

### 🔧 **DevOps y Deployment**

#### 📦 **Containerización**

- **Docker**: Containerización de aplicaciones
- **Docker Compose**: Orquestación multi-container

#### ☁️ **Deployment Platforms**

- **Heroku**: Platform-as-a-Service simple
- **Vercel**: Deployment para apps web
- **AWS EC2**: Máquinas virtuales cloud
- **Google Cloud Run**: Containers serverless

### 🔒 **Seguridad y Gestión de Secretos**

#### 🔐 **Manejo de Credenciales**

- **python-dotenv**: Variables de entorno
- **keyring**: Almacenamiento seguro de credenciales
- **cryptography**: Encriptación en Python

#### 🛡️ **Best Practices**

```python
# Ejemplo de configuración segura
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")
```

---

## 🚀 Setup Instructions

### 📋 **Prerequisitos del Sistema**

- **OS**: Windows 10/11, macOS 10.15+, o Ubuntu 18.04+
- **RAM**: Mínimo 8GB, recomendado 16GB+
- **Storage**: 20GB libres para instalaciones y datasets
- **Internet**: Conexión estable para descargas y APIs

### 🔧 **Instalación Paso a Paso**

#### 1️⃣ **Python y Anaconda**

```bash
# Descargar e instalar Anaconda
# https://www.anaconda.com/products/distribution

# Verificar instalación
python --version
conda --version
```

#### 2️⃣ **Crear Entorno Virtual**

```bash
# Crear entorno específico para el curso
conda create -n ia-automatizacion python=3.9
conda activate ia-automatizacion

# Verificar entorno activo
conda info --envs
```

#### 3️⃣ **Instalar Dependencias Core**

```bash
# Instalar paquetes básicos
conda install numpy pandas matplotlib seaborn jupyter
pip install scikit-learn tensorflow openai langchain

# Verificar instalaciones
python -c "import numpy, pandas, sklearn; print('✅ Instalación exitosa')"
```

#### 4️⃣ **Configurar Jupyter**

```bash
# Instalar kernel del entorno
python -m ipykernel install --user --name ia-automatizacion --display-name "IA y Automatización"

# Iniciar JupyterLab
jupyter lab
```

#### 5️⃣ **Instalar Herramientas RPA**

```bash
# Selenium y drivers
pip install selenium
# Descargar ChromeDriver manualmente o usar webdriver-manager
pip install webdriver-manager

# UiPath Community Edition
# Descargar desde: https://www.uipath.com/community
```

#### 6️⃣ **Configurar APIs**

```bash
# Crear archivo .env
echo "OPENAI_API_KEY=tu_api_key_aquí" > .env
echo "GOOGLE_API_KEY=tu_google_key_aquí" >> .env
```

### 🧪 **Verificación de Setup**

```python
# Script de verificación completa
import sys
import importlib

def check_package(package_name):
    try:
        importlib.import_module(package_name)
        print(f"✅ {package_name}")
        return True
    except ImportError:
        print(f"❌ {package_name}")
        return False

# Lista de paquetes críticos
packages = [
    'numpy', 'pandas', 'matplotlib', 'seaborn',
    'sklearn', 'tensorflow', 'openai', 'selenium'
]

print("🔍 Verificando instalaciones...")
all_good = all(check_package(pkg) for pkg in packages)

if all_good:
    print("🎉 ¡Setup completo y exitoso!")
else:
    print("⚠️  Algunas dependencias faltan. Revisa la instalación.")
```

### 🆘 **Troubleshooting Común**

#### 🐍 **Problemas con Python**

```bash
# Python no encontrado
export PATH="/opt/anaconda3/bin:$PATH"  # macOS/Linux
# En Windows: agregar a PATH en Variables de Entorno

# Conflictos de versiones
conda clean --all
conda update --all
```

#### 📦 **Problemas con Paquetes**

```bash
# Dependencias conflictivas
pip install --upgrade pip
conda update conda
conda clean --packages

# Instalación desde conda-forge
conda install -c conda-forge package_name
```

#### 🌐 **Problemas con APIs**

```python
# Test de conexión OpenAI
import openai
import os

try:
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.Model.list()
    print("✅ OpenAI API conectada")
except Exception as e:
    print(f"❌ Error OpenAI: {e}")
```

#### 🔧 **Problemas específicos de Windows**

```powershell
# Habilitar ejecución de scripts
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Visual Studio C++ Build Tools (para algunos paquetes)
# Descargar desde: https://visualstudio.microsoft.com/visual-cpp-build-tools/
```

---

## 📚 **Recursos Adicionales**

### 📖 **Documentación Oficial**

- [Python.org](https://docs.python.org/3/)
- [Anaconda Documentation](https://docs.anaconda.com/)
- [Jupyter Documentation](https://jupyter.readthedocs.io/)
- [Scikit-learn User Guide](https://scikit-learn.org/stable/user_guide.html)

### 🎥 **Videos de Configuración**

- [Installing Anaconda](https://www.youtube.com/anaconda-install)
- [Jupyter Lab Tutorial](https://www.youtube.com/jupyter-tutorial)
- [VS Code Python Setup](https://www.youtube.com/vscode-python)

### 🔧 **Tools Alternativos**

- **Google Colab**: Para quienes no puedan instalar localmente
- **Repl.it**: Entorno de desarrollo online
- **Kaggle Notebooks**: Para datasets y competencias

---

*Herramientas v1.0 | Stack actualizado para 2025*  
*Última actualización: 13 de octubre de 2025 | Autor: Andres Olarte*
