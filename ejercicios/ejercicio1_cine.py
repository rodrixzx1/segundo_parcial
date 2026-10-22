# PROBLEMA
# Determinar el importe total de una compra de boletos de cine aplicando un descuento por volumen.
# ENTRADAS
# cantidad: int, boletos, entero mayor a 0.
# SALIDAS
# cantidad, precio unitario, subtotal, descuento y total a pagar, mostrados en pesos mexicanos con dos decimales y en tabla usando tabulate con frase descriptiva.
# REGLAS Y SUPUESTOS
# Precio fijo por boleto: $75.00.
# Si se adquieren 4 boletos o más (cantidad >= 4), se aplica un 10% de descuento (0.10) sobre el subtotal.
# Para compras menores a 4 boletos, el descuento es de $0.00.
# ALGORITMO
# 1. Leer la cantidad de boletos.
# 2. Definir precio_unitario = 75.0
# 3. Calcular subtotal = cantidad * precio_unitario
# 4. Si cantidad >= 4:
#      descuento = subtotal * 0.10
#    En caso contrario:
#      descuento = 0.0
# 5. Calcular total = subtotal - descuento
# 6. Mostrar la información utilizando tabulate con una frase descriptiva.
# CASOS DE PRUEBA
# 1 -> Subtotal: $75.00, Descuento: $0.00, Total: $75.00
# 3 -> Subtotal: $225.00, Descuento: $0.00, Total: $225.00
# 4 -> Subtotal: $300.00, Descuento: $30.00, Total: $270.00
# 6 -> Subtotal: $450.00, Descuento: $45.00, Total: $405.00
# RESTRICCIONES PARA EL AGENTE
# Implementa exactamente este algoritmo, en el mismo orden.
# Usa únicamente las funciones del contrato, con esas firmas.
# La única biblioteca externa permitida es tabulate. No importes ningún otro módulo.
# No agregues clases ni validaciones adicionales fuera de lo especificado.
# No llames a las funciones en este archivo; se llaman desde menu/menu.py.

# CONTRATO DE FUNCIONES
# leerCantidad() -> int
# calcularSubtotal(cantidad: int) -> tuple
# mostrarCompra(cantidad: int, precio_unitario: float, subtotal: float, descuento: float, total: float) -> None

from tabulate import tabulate

def leerCantidad():
    return int(input("Ingrese la cantidad de boletos a comprar: "))

def calcularSubtotal(cantidad):
    precio_unitario = 75.0
    subtotal = cantidad * precio_unitario
    if cantidad >= 4:
        descuento = subtotal * 0.10
    else:
        descuento = 0.0
    total = subtotal - descuento
    return precio_unitario, subtotal, descuento, total

def mostrarCompra(cantidad, precio_unitario, subtotal, descuento, total):
    print("\n--- Resultado de la Compra de Boletos ---")
    filas = [
        ["Cantidad de boletos", cantidad],
        ["Precio unitario", f"${precio_unitario:.2f}"],
        ["Subtotal", f"${subtotal:.2f}"],
        ["Descuento aplicado", f"${descuento:.2f}"],
        ["Total a pagar", f"${total:.2f}"]
    ]
    print(tabulate(filas, headers=["Concepto", "Detalle"]))