# PROBLEMA
# Calcular el rendimiento de combustible de un vehículo y el costo total de un recorrido.
# ENTRADAS
# distancia: float, kilómetros, mayor a 0.
# litros: float, litros consumidos, mayor a 0.
# SALIDAS
# Distancia, litros, precio por litro, rendimiento en km/l y costo total, presentados en formato con dos decimales y mediante tabulate con frase descriptiva.
# REGLAS Y SUPUESTOS
# Precio fijo por litro de combustible: $24.00.
# Rendimiento se calcula como: distancia / litros.
# Costo total se calcula como: litros * 24.0.
# ALGORITMO
# 1. Leer distancia y litros.
# 2. Definir precio_litro = 24.0
# 3. Calcular rendimiento = distancia / litros
# 4. Calcular costo = litros * precio_litro
# 5. Mostrar la información utilizando tabulate con una frase descriptiva.
# CASOS DE PRUEBA
# 120 km, 10 litros -> Rendimiento: 12.00 km/l, Costo: $240.00
# 250 km, 20 litros -> Rendimiento: 12.50 km/l, Costo: $480.00
# 180 km, 15 litros -> Rendimiento: 12.00 km/l, Costo: $360.00
# 300 km, 25 litros -> Rendimiento: 12.00 km/l, Costo: $600.00
# RESTRICCIONES PARA EL AGENTE
# Implementa exactamente este algoritmo, en el mismo orden.
# Usa únicamente las funciones del contrato, con esas firmas.
# La única biblioteca externa permitida es tabulate. No importes ningún otro módulo.
# No agregues clases ni validaciones adicionales fuera de lo especificado.
# No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerDatos() = tuple
# calcularRendimientoYCosto(distancia: float, litros: float) = tuple
# mostrarResultados(distancia: float, litros: float, rendimiento: float, costo: float) -> None

from tabulate import tabulate

def leerDatos():
    distancia = float(input("Ingrese la distancia recorrida en kilómetros: "))
    litros = float(input("Ingrese la cantidad de litros consumidos: "))
    return distancia, litros

def calcularRendimientoYCosto(distancia, litros):
    rendimiento = distancia / litros
    costo = litros * 24.0
    return rendimiento, costo

def mostrarResultados(distancia, litros, rendimiento, costo):
    print("\n--- Análisis de Consumo de Combustible ---")
    filas = [
        ["Distancia recorrida", f"{distancia:.2f} km"],
        ["Litros consumidos", f"{litros:.2f} L"],
        ["Precio por litro", "$24.00"],
        ["Rendimiento del vehículo", f"{rendimiento:.2f} km/l"],
        ["Costo total del combustible", f"${costo:.2f}"]
    ]
    print(tabulate(filas, headers=["Concepto", "Detalle"]))