from ejercicios import ejercicio1_cine as ej1
from ejercicios import ejercicio2_combustible as ej2

def ejecutarEjercicio1():
    cantidad = ej1.leerCantidad()
    precio_unitario, subtotal, descuento, total = ej1.calcularSubtotal(cantidad)
    ej1.mostrarCompra(cantidad, precio_unitario, subtotal, descuento, total)

def ejecutarEjercicio2():
    distancia, litros = ej2.leerDatos()
    rendimiento, costo = ej2.calcularRendimientoYCosto(distancia, litros)
    ej2.mostrarResultados(distancia, litros, rendimiento, costo)

def mostrarMenu():
    print()
    print("SEGUNDO EXAMEN PARCIAL")
    print("1. Venta de boletos de cine")
    print("2. Consumo de combustible")
    print("0. Salir")

def menus():
    opcion = ""
    while opcion != "0":
        mostrarMenu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            ejecutarEjercicio1()
        elif opcion == "2":
            ejecutarEjercicio2()
        elif opcion != "0":
            print("Opción no válida.")