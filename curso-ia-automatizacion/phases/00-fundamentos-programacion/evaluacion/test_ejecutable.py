#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🧪 Test Ejecutable - Fase 00: Fundamentos de Programación

Instrucciones:
1. Completa cada función con tu código
2. Ejecuta este archivo para verificar tus respuestas
3. El sistema te dará feedback inmediato
4. Alcanza 70 puntos o más para aprobar

Autor: Curso IA y Automatización
Fecha: Octubre 2025
"""

import sys
from typing import List, Dict, Any, Union

# =============================================================================
# SISTEMA DE EVALUACIÓN AUTOMÁTICA
# =============================================================================

class EvaluadorTest:
    def __init__(self):
        self.puntos_total = 0
        self.puntos_maximos = 100
        self.resultados = []
    
    def evaluar_funcion(self, nombre_funcion, funcion, casos_prueba, puntos_maximos):
        """Evalúa una función con casos de prueba"""
        puntos_obtenidos = 0
        casos_exitosos = 0
        
        print(f"\n🔍 Evaluando {nombre_funcion}...")
        
        for i, caso in enumerate(casos_prueba, 1):
            try:
                entrada = caso['entrada']
                esperado = caso['esperado']
                
                if isinstance(entrada, tuple):
                    resultado = funcion(*entrada)
                else:
                    resultado = funcion(entrada)
                
                if resultado == esperado:
                    casos_exitosos += 1
                    print(f"  ✅ Caso {i}: CORRECTO")
                else:
                    print(f"  ❌ Caso {i}: Esperado {esperado}, obtuvo {resultado}")
            
            except Exception as e:
                print(f"  💥 Caso {i}: Error - {e}")
        
        # Calcular puntos proporcionales
        if casos_prueba:
            puntos_obtenidos = (casos_exitosos / len(casos_prueba)) * puntos_maximos
        
        self.puntos_total += puntos_obtenidos
        self.resultados.append({
            'funcion': nombre_funcion,
            'puntos': puntos_obtenidos,
            'maximos': puntos_maximos,
            'casos_exitosos': casos_exitosos,
            'casos_totales': len(casos_prueba)
        })
        
        print(f"  📊 Puntos obtenidos: {puntos_obtenidos:.1f}/{puntos_maximos}")
        return puntos_obtenidos
    
    def mostrar_resumen(self):
        """Muestra el resumen final de la evaluación"""
        print("\n" + "="*60)
        print("📊 RESUMEN DE EVALUACIÓN")
        print("="*60)
        
        for resultado in self.resultados:
            porcentaje = (resultado['puntos'] / resultado['maximos']) * 100
            print(f"{resultado['funcion']:<25} {resultado['puntos']:>5.1f}/{resultado['maximos']:<3} ({porcentaje:>5.1f}%)")
        
        print("-" * 60)
        print(f"{'TOTAL':<25} {self.puntos_total:>5.1f}/{self.puntos_maximos:<3} ({self.puntos_total:>5.1f}%)")
        
        # Calificación final
        if self.puntos_total >= 90:
            calificacion = "A - ¡EXCELENTE! 🌟"
        elif self.puntos_total >= 80:
            calificacion = "B - ¡MUY BIEN! 👍"
        elif self.puntos_total >= 70:
            calificacion = "C - APROBADO ✅"
        elif self.puntos_total >= 60:
            calificacion = "D - NECESITAS MEJORAR ⚠️"
        else:
            calificacion = "F - REPROBADO ❌"
        
        print(f"\n🎯 CALIFICACIÓN FINAL: {calificacion}")
        
        if self.puntos_total >= 70:
            print("🎉 ¡Felicidades! Estás listo para la Fase 01: Fundamentos de IA")
        else:
            print("📚 Revisa los conceptos y vuelve a intentarlo. ¡Tú puedes!")

# =============================================================================
# SECCIÓN A: VARIABLES Y TIPOS DE DATOS
# =============================================================================

def convertir_temperatura(celsius):
    """
    A1: Convierte temperatura de Celsius a Fahrenheit
    Fórmula: F = C * 9/5 + 32
    """
    # TODO: Implementa tu código aquí
    pass

def calcular_imc(peso, altura):
    """
    A2: Calcula el Índice de Masa Corporal
    Fórmula: IMC = peso / (altura^2)
    Retorna el IMC redondeado a 2 decimales
    """
    # TODO: Implementa tu código aquí
    pass

def analizar_string(texto):
    """
    A3: Retorna un diccionario con análisis del texto:
    - 'longitud': número de caracteres
    - 'palabras': número de palabras
    - 'mayusculas': True si tiene mayúsculas, False si no
    """
    # TODO: Implementa tu código aquí
    pass

# =============================================================================
# SECCIÓN B: OPERADORES Y CÁLCULOS
# =============================================================================

def calcular_descuento(precio, descuento_porcentaje):
    """
    B1: Calcula el precio final después del descuento
    Retorna el precio con descuento redondeado a 2 decimales
    """
    # TODO: Implementa tu código aquí
    pass

def es_numero_primo(numero):
    """
    B2: Determina si un número es primo
    Un número primo solo es divisible por 1 y por sí mismo
    Considera que 1 no es primo
    """
    # TODO: Implementa tu código aquí
    pass

def operacion_matematica(a, b, operacion):
    """
    B3: Realiza operación matemática básica
    operacion puede ser: "suma", "resta", "multiplicacion", "division"
    Para división por cero, retorna "Error"
    """
    # TODO: Implementa tu código aquí
    pass

# =============================================================================
# SECCIÓN C: CONDICIONALES Y LÓGICA
# =============================================================================

def clasificar_edad(edad):
    """
    C1: Clasifica edad en categorías:
    0-12: "Niño", 13-17: "Adolescente", 18-64: "Adulto", 65+: "Adulto Mayor"
    Para edades inválidas (<0 o >120): "Edad inválida"
    """
    # TODO: Implementa tu código aquí
    pass

def evaluar_calificacion(puntos):
    """
    C2: Convierte puntos (0-100) a letra:
    90-100: "A", 80-89: "B", 70-79: "C", 60-69: "D", <60: "F"
    """
    # TODO: Implementa tu código aquí
    pass

def validar_password(password):
    """
    C3: Valida si un password es seguro:
    - Al menos 8 caracteres
    - Al menos una mayúscula
    - Al menos una minúscula
    - Al menos un número
    Retorna True si es seguro, False si no
    """
    # TODO: Implementa tu código aquí
    pass

# =============================================================================
# SECCIÓN D: BUCLES Y REPETICIÓN
# =============================================================================

def contar_vocales(texto):
    """
    D1: Cuenta las vocales (a,e,i,o,u) en un texto
    Considera mayúsculas y minúsculas
    """
    # TODO: Implementa tu código aquí
    pass

def fibonacci(n):
    """
    D2: Genera los primeros n números de la secuencia Fibonacci
    Retorna una lista con la secuencia
    """
    # TODO: Implementa tu código aquí
    pass

# =============================================================================
# SECCIÓN E: LISTAS Y MANIPULACIÓN
# =============================================================================

def procesar_numeros(numeros):
    """
    E1: Procesa una lista de números y retorna diccionario con:
    - 'suma': suma total
    - 'promedio': promedio (redondeado a 2 decimales)
    - 'maximo': número más grande
    - 'minimo': número más pequeño
    Si la lista está vacía, retorna None
    """
    # TODO: Implementa tu código aquí
    pass

def filtrar_pares(numeros):
    """
    E2: Retorna una nueva lista solo con los números pares
    """
    # TODO: Implementa tu código aquí
    pass

# =============================================================================
# SECCIÓN F: DICCIONARIOS
# =============================================================================

def contar_caracteres(texto):
    """
    F1: Cuenta la frecuencia de cada carácter en el texto
    Retorna un diccionario con caracter: frecuencia
    """
    # TODO: Implementa tu código aquí
    pass

def fusionar_diccionarios(dict1, dict2):
    """
    F2: Fusiona dos diccionarios
    Si hay claves repetidas, suma sus valores
    """
    # TODO: Implementa tu código aquí
    pass

# =============================================================================
# SECCIÓN G: FUNCIONES AVANZADAS
# =============================================================================

def calculadora_avanzada(operaciones):
    """
    G1: Procesa una lista de operaciones matemáticas
    Cada operación es un diccionario: {'operacion': str, 'a': num, 'b': num}
    Retorna lista con los resultados
    Operaciones válidas: "suma", "resta", "multiplicacion", "division"
    """
    # TODO: Implementa tu código aquí
    pass

# =============================================================================
# CASOS DE PRUEBA
# =============================================================================

def ejecutar_test():
    """Ejecuta todos los tests de evaluación"""
    evaluador = EvaluadorTest()
    
    print("🧪 INICIANDO TEST DE EVALUACIÓN - FASE 00")
    print("=" * 60)
    
    # Test Sección A
    evaluador.evaluar_funcion("convertir_temperatura", convertir_temperatura, [
        {'entrada': 0, 'esperado': 32.0},
        {'entrada': 100, 'esperado': 212.0},
        {'entrada': 25, 'esperado': 77.0}
    ], 5)
    
    evaluador.evaluar_funcion("calcular_imc", calcular_imc, [
        {'entrada': (70, 1.75), 'esperado': 22.86},
        {'entrada': (80, 1.80), 'esperado': 24.69},
        {'entrada': (60, 1.60), 'esperado': 23.44}
    ], 5)
    
    evaluador.evaluar_funcion("analizar_string", analizar_string, [
        {'entrada': "Hola Mundo", 'esperado': {'longitud': 10, 'palabras': 2, 'mayusculas': True}},
        {'entrada': "python", 'esperado': {'longitud': 6, 'palabras': 1, 'mayusculas': False}},
        {'entrada': "Test 123", 'esperado': {'longitud': 8, 'palabras': 2, 'mayusculas': True}}
    ], 5)
    
    # Test Sección B
    evaluador.evaluar_funcion("calcular_descuento", calcular_descuento, [
        {'entrada': (100, 20), 'esperado': 80.0},
        {'entrada': (250, 15), 'esperado': 212.5},
        {'entrada': (50, 10), 'esperado': 45.0}
    ], 5)
    
    evaluador.evaluar_funcion("es_numero_primo", es_numero_primo, [
        {'entrada': 2, 'esperado': True},
        {'entrada': 17, 'esperado': True},
        {'entrada': 4, 'esperado': False},
        {'entrada': 1, 'esperado': False}
    ], 5)
    
    evaluador.evaluar_funcion("operacion_matematica", operacion_matematica, [
        {'entrada': (10, 5, "suma"), 'esperado': 15},
        {'entrada': (10, 5, "division"), 'esperado': 2.0},
        {'entrada': (10, 0, "division"), 'esperado': "Error"}
    ], 5)
    
    # Test Sección C
    evaluador.evaluar_funcion("clasificar_edad", clasificar_edad, [
        {'entrada': 10, 'esperado': "Niño"},
        {'entrada': 15, 'esperado': "Adolescente"},
        {'entrada': 25, 'esperado': "Adulto"},
        {'entrada': 70, 'esperado': "Adulto Mayor"},
        {'entrada': -5, 'esperado': "Edad inválida"}
    ], 7)
    
    evaluador.evaluar_funcion("evaluar_calificacion", evaluar_calificacion, [
        {'entrada': 95, 'esperado': "A"},
        {'entrada': 85, 'esperado': "B"},
        {'entrada': 75, 'esperado': "C"},
        {'entrada': 65, 'esperado': "D"},
        {'entrada': 45, 'esperado': "F"}
    ], 6)
    
    evaluador.evaluar_funcion("validar_password", validar_password, [
        {'entrada': "MiPassword123", 'esperado': True},
        {'entrada': "password", 'esperado': False},
        {'entrada': "PASSWORD123", 'esperado': False},
        {'entrada': "Pass123", 'esperado': False}  # Muy corto
    ], 7)
    
    # Test Sección D
    evaluador.evaluar_funcion("contar_vocales", contar_vocales, [
        {'entrada': "Hola Mundo", 'esperado': 4},
        {'entrada': "Python", 'esperado': 1},
        {'entrada': "Programación", 'esperado': 5}
    ], 8)
    
    evaluador.evaluar_funcion("fibonacci", fibonacci, [
        {'entrada': 5, 'esperado': [0, 1, 1, 2, 3]},
        {'entrada': 7, 'esperado': [0, 1, 1, 2, 3, 5, 8]},
        {'entrada': 1, 'esperado': [0]}
    ], 7)
    
    # Test Sección E
    evaluador.evaluar_funcion("procesar_numeros", procesar_numeros, [
        {'entrada': [1, 2, 3, 4, 5], 'esperado': {'suma': 15, 'promedio': 3.0, 'maximo': 5, 'minimo': 1}},
        {'entrada': [10], 'esperado': {'suma': 10, 'promedio': 10.0, 'maximo': 10, 'minimo': 10}},
        {'entrada': [], 'esperado': None}
    ], 8)
    
    evaluador.evaluar_funcion("filtrar_pares", filtrar_pares, [
        {'entrada': [1, 2, 3, 4, 5, 6], 'esperado': [2, 4, 6]},
        {'entrada': [1, 3, 5], 'esperado': []},
        {'entrada': [2, 4, 8, 10], 'esperado': [2, 4, 8, 10]}
    ], 7)
    
    # Test Sección F
    evaluador.evaluar_funcion("contar_caracteres", contar_caracteres, [
        {'entrada': "hello", 'esperado': {'h': 1, 'e': 1, 'l': 2, 'o': 1}},
        {'entrada': "aaa", 'esperado': {'a': 3}},
        {'entrada': "ab ab", 'esperado': {'a': 2, 'b': 2, ' ': 1}}
    ], 5)
    
    evaluador.evaluar_funcion("fusionar_diccionarios", fusionar_diccionarios, [
        {'entrada': ({'a': 1, 'b': 2}, {'b': 3, 'c': 4}), 'esperado': {'a': 1, 'b': 5, 'c': 4}},
        {'entrada': ({}, {'x': 10}), 'esperado': {'x': 10}},
        {'entrada': ({'x': 5}, {}), 'esperado': {'x': 5}}
    ], 5)
    
    # Test Sección G
    evaluador.evaluar_funcion("calculadora_avanzada", calculadora_avanzada, [
        {'entrada': [
            {'operacion': 'suma', 'a': 5, 'b': 3},
            {'operacion': 'multiplicacion', 'a': 4, 'b': 2}
        ], 'esperado': [8, 8]},
        {'entrada': [
            {'operacion': 'division', 'a': 10, 'b': 2},
            {'operacion': 'resta', 'a': 7, 'b': 3}
        ], 'esperado': [5.0, 4]}
    ], 10)
    
    # Mostrar resumen final
    evaluador.mostrar_resumen()

# =============================================================================
# EJECUCIÓN PRINCIPAL
# =============================================================================

if __name__ == "__main__":
    print("🎓 CURSO DE IA Y AUTOMATIZACIÓN")
    print("📋 Test de Evaluación - Fase 00: Fundamentos de Programación")
    print("-" * 60)
    print("Instrucciones:")
    print("1. Completa cada función marcada con 'TODO'")
    print("2. Ejecuta este archivo para obtener tu calificación")
    print("3. Necesitas 70 puntos o más para aprobar")
    print("4. ¡Buena suerte! 🍀")
    
    input("\nPresiona Enter para comenzar el test...")
    
    try:
        ejecutar_test()
    except KeyboardInterrupt:
        print("\n\n⚠️ Test interrumpido por el usuario")
    except Exception as e:
        print(f"\n\n💥 Error inesperado: {e}")
        print("Contacta al instructor si el problema persiste")
    
    input("\nPresiona Enter para salir...")