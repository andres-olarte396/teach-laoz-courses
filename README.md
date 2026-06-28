# 🤖 Sistema de Automatización de Cursos - Teach LaOz

[![Estado](https://img.shields.io/badge/Estado-Activo-success)](https://github.com/andres-olarte396/teach-laoz-courses)
[![Licencia](https://img.shields.io/badge/Licencia-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.8%2B-blue)](course-automation.py)
[![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-CI%2FCD-brightgreen)](.github/workflows/)

## 📋 Descripción

Repositorio de **plantillas y herramientas de automatización** para la creación, validación y exportación de cursos del ecosistema **Teach LaOz**. Contiene pipelines de GitHub Actions, scripts de generación y plantillas YAML para estandarizar la producción de cursos.

## 🎯 Funcionalidades

1. **Generación automática de cursos** desde plantillas YAML
2. **Validación de estructura** y calidad del contenido
3. **Exportación a PDF** de todos los materiales del curso
4. **Creación de releases** automáticos con los archivos generados
5. **Métricas y estadísticas** de progreso de cada curso

## 🔧 Workflows de GitHub Actions

| Workflow | Trigger | Función |
|---------|---------|---------|
| `generate-course.yml` | Push a `**/curso.yaml` | Genera contenido completo del curso |
| `validate-courses.yml` | PR con cambios | Valida estructura y consistencia |
| `export-pdf.yml` | Manual / Merge | Exporta materiales a PDF |
| `validate-simple.yml` | Push | Validación rápida de sintaxis YAML |

## 📁 Estructura del Proyecto

```
teach-laoz-courses/
│
├── README.md                          # Este archivo
├── AUTOMATION-GUIDE.md                # Guía completa del sistema
├── CHECKLIST.md                       # Checklist de calidad para cursos
├── course-automation.py               # Script principal de automatización
├── template-curso.yaml                # Plantilla base para nuevos cursos
│
├── .github/
│   └── workflows/
│       ├── generate-course.yml        # Generación automática
│       ├── validate-courses.yml       # Validación completa
│       ├── export-pdf.yml             # Exportación a PDF
│       └── validate-simple.yml        # Validación rápida
│
└── curso-ia-automatizacion/           # Curso de ejemplo: IA y Automatización
    ├── curso.yaml                     # Configuración del curso
    ├── roadmap.md                     # Hoja de ruta
    └── docs/                          # Documentación del curso
```

## 🚀 Cómo Crear un Nuevo Curso

### 1. Desde la plantilla YAML

```bash
# Copia la plantilla base
cp template-curso.yaml mi-nuevo-curso/curso.yaml

# Edita la configuración
nano mi-nuevo-curso/curso.yaml
```

### 2. Estructura del archivo `curso.yaml`

```yaml
nombre: "nombre-del-curso"
titulo: "Título del Curso"
descripcion: "Descripción breve del curso"
nivel: "Básico | Intermedio | Avanzado"
duracion: "X horas"
modulos:
  - id: 0
    titulo: "Módulo 0: Nivelación"
    temas:
      - "Tema 0.1"
      - "Tema 0.2"
```

### 3. Ejecutar la automatización

El pipeline se activa automáticamente al hacer push del archivo `curso.yaml`, o manualmente desde la pestaña **Actions** en GitHub.

## 📋 Checklist de Calidad

Antes de publicar un curso, verifica el [CHECKLIST.md](CHECKLIST.md):

- [ ] Plan curricular completo
- [ ] Objetivos claros y medibles
- [ ] Cronograma realista
- [ ] Ejercicios prácticos en cada módulo
- [ ] Evaluaciones con criterios definidos
- [ ] README detallado

## 🤝 Contribuciones

Para mejorar las plantillas o agregar nuevos workflows:

1. Abre un **Issue** describiendo la mejora
2. Haz un **Fork** del repositorio
3. Envía un **Pull Request**

## 📄 Licencia

Disponible bajo la Licencia MIT.

## 👥 Créditos

**Proyecto**: Teach LaOz Learning Management System
**Autor**: Andrés Olarte
**Repositorio**: [github.com/andres-olarte396/teach-laoz-courses](https://github.com/andres-olarte396/teach-laoz-courses)

---

**¡Automatiza la creación de conocimiento! 🤖📚**
