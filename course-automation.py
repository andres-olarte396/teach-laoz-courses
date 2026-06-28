#!/usr/bin/env python3
"""
🤖 Utilidad de Automatización para Cursos
==========================================

Script unificado para gestionar todo el ciclo de vida de los cursos:
- Validación de archivos YAML
- Generación de contenido
- Exportación a PDF
- Gestión de releases
"""

import os
import sys
import argparse
import subprocess
import yaml
from pathlib import Path
from datetime import datetime

class CourseAutomation:
    def __init__(self, course_dir=None):
        self.course_dir = Path(course_dir) if course_dir else Path.cwd()
        self.yaml_file = self.course_dir / "curso.yaml"
        self.scripts_dir = self.course_dir / "scripts"
    
    def print_status(self, message, status="info"):
        """Imprime mensajes con formato"""
        colors = {
            "info": "\033[0;34m",     # Azul
            "success": "\033[0;32m",   # Verde
            "warning": "\033[1;33m",   # Amarillo
            "error": "\033[0;31m",     # Rojo
            "reset": "\033[0m"         # Reset
        }
        
        icons = {
            "info": "ℹ️",
            "success": "✅",
            "warning": "⚠️",
            "error": "❌"
        }
        
        color = colors.get(status, colors["info"])
        icon = icons.get(status, "")
        reset = colors["reset"]
        
        print(f"{color}{icon} {message}{reset}")
    
    def validate_course(self):
        """Valida la estructura del curso"""
        self.print_status("Validando curso...", "info")
        
        # Verificar que existe el archivo YAML
        if not self.yaml_file.exists():
            self.print_status(f"No se encontró {self.yaml_file}", "error")
            return False
        
        # Verificar scripts
        validate_script = self.scripts_dir / "validate_yaml.py"
        if validate_script.exists():
            try:
                result = subprocess.run([
                    sys.executable, str(validate_script), str(self.yaml_file)
                ], capture_output=True, text=True)
                
                if result.returncode == 0:
                    self.print_status("Validación exitosa", "success")
                    return True
                else:
                    self.print_status(f"Error en validación: {result.stderr}", "error")
                    return False
            except Exception as e:
                self.print_status(f"Error ejecutando validación: {e}", "error")
                return False
        else:
            # Validación básica
            try:
                with open(self.yaml_file, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                
                if 'curso' not in data:
                    self.print_status("Falta la clave 'curso' en el YAML", "error")
                    return False
                
                curso = data['curso']
                required_fields = ['id', 'titulo', 'descripcion', 'modulos']
                
                for field in required_fields:
                    if field not in curso:
                        self.print_status(f"Falta el campo '{field}'", "error")
                        return False
                
                self.print_status("Validación básica exitosa", "success")
                return True
                
            except Exception as e:
                self.print_status(f"Error en YAML: {e}", "error")
                return False
    
    def generate_content(self):
        """Genera el contenido del curso"""
        self.print_status("Generando contenido del curso...", "info")
        
        generate_script = self.scripts_dir / "generate_course.py"
        if not generate_script.exists():
            self.print_status("Script de generación no encontrado", "error")
            return False
        
        try:
            result = subprocess.run([
                sys.executable, str(generate_script), str(self.yaml_file)
            ], capture_output=True, text=True)
            
            if result.returncode == 0:
                self.print_status("Contenido generado exitosamente", "success")
                print(result.stdout)
                return True
            else:
                self.print_status(f"Error generando contenido: {result.stderr}", "error")
                return False
                
        except Exception as e:
            self.print_status(f"Error ejecutando generación: {e}", "error")
            return False
    
    def export_pdf(self):
        """Exporta el curso a PDF"""
        self.print_status("Exportando a PDF...", "info")
        
        export_script = self.scripts_dir / "export_pdf.sh"
        if not export_script.exists():
            self.print_status("Script de exportación no encontrado", "error")
            return False
        
        # Hacer ejecutable el script
        os.chmod(export_script, 0o755)
        
        try:
            result = subprocess.run([
                str(export_script), str(self.course_dir)
            ], capture_output=True, text=True, cwd=self.course_dir)
            
            if result.returncode == 0:
                self.print_status("Exportación a PDF exitosa", "success")
                print(result.stdout)
                return True
            else:
                self.print_status(f"Error en exportación: {result.stderr}", "error")
                return False
                
        except Exception as e:
            self.print_status(f"Error ejecutando exportación: {e}", "error")
            return False
    
    def show_status(self):
        """Muestra el estado actual del curso"""
        self.print_status("Estado del curso:", "info")
        
        # Información básica
        print(f"📁 Directorio: {self.course_dir}")
        print(f"📄 YAML: {'✅' if self.yaml_file.exists() else '❌'}")
        
        if self.yaml_file.exists():
            try:
                with open(self.yaml_file, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                
                curso = data.get('curso', {})
                print(f"🎓 Título: {curso.get('titulo', 'Sin título')}")
                print(f"🆔 ID: {curso.get('id', 'Sin ID')}")
                print(f"📚 Módulos: {len(curso.get('modulos', []))}")
                print(f"⏱️ Duración: {curso.get('duracion_aproximada', 'No especificada')}")
                
            except Exception as e:
                self.print_status(f"Error leyendo YAML: {e}", "error")
        
        # Archivos generados
        generated_files = ['README.md', 'roadmap.md', 'test.md']
        print("\n📋 Archivos generados:")
        for file in generated_files:
            file_path = self.course_dir / file
            status = "✅" if file_path.exists() else "❌"
            print(f"  {status} {file}")
        
        # Módulos
        modulos_dir = self.course_dir / "modulos"
        if modulos_dir.exists():
            module_count = len([d for d in modulos_dir.iterdir() if d.is_dir()])
            print(f"\n📖 Módulos generados: {module_count}")
        
        # PDFs
        pdf_dir = self.course_dir / "exports" / "pdf"
        if pdf_dir.exists():
            pdf_count = len(list(pdf_dir.glob("*.pdf")))
            print(f"📄 PDFs generados: {pdf_count}")
    
    def full_build(self):
        """Ejecuta el proceso completo: validar -> generar -> exportar"""
        self.print_status("🚀 Iniciando proceso completo de construcción...", "info")
        
        # Paso 1: Validar
        if not self.validate_course():
            self.print_status("Validación falló, abortando", "error")
            return False
        
        # Paso 2: Generar contenido
        if not self.generate_content():
            self.print_status("Generación falló, abortando", "error")
            return False
        
        # Paso 3: Exportar PDF (opcional, puede fallar sin afectar el resto)
        if not self.export_pdf():
            self.print_status("Exportación PDF falló, pero continuando", "warning")
        
        self.print_status("🎉 Proceso completo finalizado", "success")
        return True

def main():
    parser = argparse.ArgumentParser(
        description="🤖 Utilidad de Automatización para Cursos",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:
  %(prog)s status                          # Mostrar estado del curso actual
  %(prog)s validate                        # Validar curso actual
  %(prog)s generate                        # Generar contenido
  %(prog)s export                          # Exportar a PDF
  %(prog)s build                           # Proceso completo
  %(prog)s --dir ../otro-curso validate    # Validar otro curso
        """
    )
    
    parser.add_argument(
        '--dir', '--directory',
        dest='course_dir',
        help='Directorio del curso (por defecto: directorio actual)'
    )
    
    parser.add_argument(
        'action',
        choices=['status', 'validate', 'generate', 'export', 'build'],
        help='Acción a ejecutar'
    )
    
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Mostrar salida detallada'
    )
    
    args = parser.parse_args()
    
    # Crear instancia de automatización
    automation = CourseAutomation(args.course_dir)
    
    # Ejecutar acción
    success = True
    
    if args.action == 'status':
        automation.show_status()
    elif args.action == 'validate':
        success = automation.validate_course()
    elif args.action == 'generate':
        success = automation.generate_content()
    elif args.action == 'export':
        success = automation.export_pdf()
    elif args.action == 'build':
        success = automation.full_build()
    
    # Código de salida
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()