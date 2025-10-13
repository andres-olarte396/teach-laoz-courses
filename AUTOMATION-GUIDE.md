# 🤖 Sistema de Automatización para Generación de Cursos

Este proyecto incluye un sistema completo de automatización para la generación, validación y exportación de cursos usando GitHub Actions.

## 📋 Resumen del Sistema

El sistema automatiza los siguientes procesos:

1. **🔍 Validación automática** de archivos YAML de cursos
2. **📚 Generación de contenido** completo a partir de la configuración YAML
3. **📄 Exportación a PDF** de todos los materiales
4. **🏷️ Creación de releases** con los archivos generados

## 🚀 Workflows Disponibles

### 1. Generación Automática de Cursos (`generate-course.yml`)

**Triggers:**
- Push a archivos `**/curso.yaml` o `**/scripts/**`
- Pull requests que modifiquen estos archivos
- Ejecución manual (workflow_dispatch)

**Funcionalidades:**
- ✅ Validación de estructura YAML
- 📚 Generación automática de README, roadmap y módulos
- 🧪 Ejecución de tests de validación
- 💾 Commit automático de cambios generados
- 📊 Estadísticas y métricas del curso

**Uso manual:**
```bash
# Ir a Actions > Generación Automática de Cursos > Run workflow
# Especificar: curso-IA-AUTOMATIZACION/curso.yaml
```

### 2. Validación Continua (`validate-simple.yml`)

**Triggers:**
- Push a ramas main/develop
- Pull requests
- Ejecución manual

**Funcionalidades:**
- 🔍 Búsqueda automática de todos los cursos
- ✅ Validación de sintaxis YAML
- 📊 Generación de reportes de validación

### 3. Exportación a PDF (`export-pdf.yml`)

**Triggers:**
- Ejecución manual (workflow_dispatch)
- Push de tags de versión (`v*`)

**Funcionalidades:**
- 📄 Conversión de Markdown a PDF usando Pandoc
- 📚 Creación de PDF combinado del curso completo
- 📦 Generación de archivos ZIP para descarga
- 🏷️ Creación de releases automáticas

**Uso manual:**
```bash
# Ir a Actions > Exportar Cursos a PDF > Run workflow
# Especificar directorio: curso-IA-AUTOMATIZACION
# Marcar "crear release" si se desea
```

## 📁 Estructura de Archivos Generados

Cuando se ejecuta la generación automática, se crean los siguientes archivos:

```
curso-IA-AUTOMATIZACION/
├── README.md                 # 📖 Documentación principal
├── roadmap.md               # 🗺️ Hoja de ruta detallada
├── test.md                  # 🧪 Validaciones y métricas
├── stats.md                 # 📊 Estadísticas generadas
├── modulos/                 # 📚 Estructura de módulos
│   ├── modulo-01-mod1/
│   │   ├── README.md
│   │   ├── laboratorios/
│   │   ├── recursos/
│   │   └── evaluacion/
│   └── modulo-02-mod2/
│       └── ...
└── exports/                 # 📄 Exportaciones (cuando se ejecuta PDF)
    └── pdf/
        ├── README.pdf
        ├── roadmap.pdf
        ├── modulo-01-README.pdf
        └── curso-completo.pdf
```

## 🛠️ Scripts Disponibles

### 1. `generate_course.py`
Genera todo el contenido del curso a partir del archivo YAML.

```bash
python scripts/generate_course.py curso.yaml
```

### 2. `validate_yaml.py`
Valida la estructura y contenido del archivo YAML del curso.

```bash
python scripts/validate_yaml.py curso.yaml
```

### 3. `export_pdf.sh`
Exporta todos los archivos Markdown a PDF.

```bash
chmod +x scripts/export_pdf.sh
./scripts/export_pdf.sh
```

## 📋 Guía de Uso Paso a Paso

### Para crear un nuevo curso:

1. **📝 Crear archivo YAML:**
   ```bash
   cp template-curso.yaml nuevo-curso/curso.yaml
   # Editar nuevo-curso/curso.yaml con la información del curso
   ```

2. **🔧 Configurar scripts:**
   ```bash
   mkdir -p nuevo-curso/scripts
   cp curso-IA-AUTOMATIZACION/scripts/* nuevo-curso/scripts/
   ```

3. **💾 Hacer commit:**
   ```bash
   git add nuevo-curso/
   git commit -m "feat: add new course configuration"
   git push
   ```

4. **🤖 La automatización se encarga del resto:**
   - Se valida el YAML automáticamente
   - Se genera todo el contenido
   - Se hace commit de los archivos generados

### Para exportar a PDF:

1. **🚀 Ejecutar workflow manualmente:**
   - Ir a Actions > "Exportar Cursos a PDF"
   - Seleccionar "Run workflow"
   - Especificar el directorio del curso
   - Marcar "create release" si se desea crear un release

2. **📦 Descargar archivos:**
   - Los PDFs se guardan como artifacts
   - Si se creó release, también están disponibles ahí

### Para hacer cambios a un curso existente:

1. **✏️ Editar archivo YAML:**
   ```bash
   # Modificar curso-IA-AUTOMATIZACION/curso.yaml
   git add curso-IA-AUTOMATIZACION/curso.yaml
   git commit -m "update: modify course structure"
   git push
   ```

2. **🔄 La regeneración es automática:**
   - Se detectan cambios en el YAML
   - Se regenera el contenido automáticamente
   - Se actualizan todos los archivos derivados

## 🔧 Configuración Avanzada

### Variables de entorno disponibles:

En los workflows se pueden configurar:

- `COURSE_PATH`: Ruta al directorio del curso
- `VALIDATION_LEVEL`: Nivel de validación (basic, strict)
- `PDF_ENGINE`: Motor para generación PDF (xelatex, pdflatex)

### Personalización de templates:

Los templates de generación se pueden personalizar editando:
- `generate_course.py`: Lógica de generación
- `template-curso.yaml`: Estructura base de cursos

### Hooks personalizados:

Se pueden añadir hooks pre/post generación creando:
- `scripts/pre_generate.py`: Ejecutado antes de generar
- `scripts/post_generate.py`: Ejecutado después de generar

## 🐛 Troubleshooting

### Problemas comunes:

1. **❌ Error de validación YAML:**
   ```bash
   # Verificar sintaxis manualmente
   python -c "import yaml; yaml.safe_load(open('curso.yaml'))"
   ```

2. **❌ Error en generación PDF:**
   ```bash
   # Verificar que pandoc esté instalado
   pandoc --version
   
   # Instalar dependencias faltantes
   sudo apt-get install pandoc texlive-xetex
   ```

3. **❌ Workflow no se ejecuta:**
   - Verificar que los paths en el trigger coincidan
   - Revisar permisos del repositorio
   - Verificar que no hay errores de sintaxis en el YAML del workflow

### Logs y debugging:

- Revisar la pestaña "Actions" en GitHub para logs detallados
- Los artifacts contienen archivos de log adicionales
- El job summary muestra un resumen de cada ejecución

## 📊 Métricas y Monitoreo

El sistema genera automáticamente:

- **📈 Estadísticas de curso:** Número de módulos, laboratorios, etc.
- **⏱️ Tiempos de ejecución:** Duración de cada workflow
- **📋 Reportes de validación:** Estado de todos los cursos
- **📄 Logs de exportación:** Detalles de archivos generados

## 🔒 Seguridad y Permisos

- Los workflows usan `GITHUB_TOKEN` para operaciones básicas
- No se requieren secretos adicionales para funcionalidad básica
- Los PDFs se almacenan como artifacts con retención configurable
- Los releases se crean con permisos estándar del repositorio

## 🆕 Futuras Mejoras

- [ ] 🌐 Exportación a HTML interactivo
- [ ] 📱 Generación de versión móvil
- [ ] 🎨 Templates de diseño personalizables  
- [ ] 🔗 Integración con plataformas LMS
- [ ] 📧 Notificaciones automáticas
- [ ] 🌍 Soporte multi-idioma
- [ ] 📊 Dashboard de métricas avanzadas

---

**🎯 ¡El sistema está listo para usar!** Simplemente edita los archivos YAML y la automatización se encarga del resto.