# ============================================================================
# EJEMPLO 03: OPERACIONES BÁSICAS
# ============================================================================
# Tema: Operadores aritméticos y de comparación
# Objetivo: Realizar cálculos y comparaciones básicas
# Nivel: Principiante
# Prerrequisito: ejemplo_02_variables_tipos.py

# Datos de ejemplo
precio_original = 100
descuento_porcentaje = 15
cantidad = 3

print("=== CALCULADORA DE COMPRAS ===")
print(f"Precio original: ${precio_original}")
print(f"Descuento: {descuento_porcentaje}%")
print(f"Cantidad: {cantidad} unidades")

# Operaciones aritméticas básicas
descuento_dinero = precio_original * (descuento_porcentaje / 100)
precio_con_descuento = precio_original - descuento_dinero
total_compra = precio_con_descuento * cantidad

print("\nCálculos:")
print(f"Descuento en dinero: ${descuento_dinero}")
print(f"Precio con descuento: ${precio_con_descuento}")
print(f"Total de la compra: ${total_compra}")

# Operaciones adicionales
promedio_por_unidad = total_compra / cantidad
resto_division = precio_original % 7  # Módulo
precio_al_cubo = precio_original ** 3  # Potencia

print("\nOperaciones adicionales:")
print(f"Promedio por unidad: ${promedio_por_unidad}")
print(f"Resto de dividir {precio_original} entre 7: {resto_division}")
print(f"{precio_original} elevado al cubo: {precio_al_cubo}")

# Comparaciones
print("\nComparaciones:")
print(f"¿El total es mayor a $200? {total_compra > 200}")
print(f"¿El descuento es exactamente 15%? {descuento_porcentaje == 15}")
print(f"¿La cantidad es diferente de 2? {cantidad != 2}")
print(f"¿El precio original está entre 50 y 150? {50 <= precio_original <= 150}")

# Ejercicio: Calcula el impuesto (16%) sobre el total_compra