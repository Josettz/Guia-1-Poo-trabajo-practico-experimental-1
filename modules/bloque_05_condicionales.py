from utils.consola import limpiar, pausar, titulo, amarillo, error, SEPARADOR


def menu():
    while True:
        titulo("BLOQUE 05_condicionales  — lógica")
        print(f"  [{amarillo('1')}] Ejercicio 1 - Par o impar")
        print(f"  [{amarillo('2')}] Ejercicio 2 - Calificación letra por nota")
        print(f"  [{amarillo('3')}] Ejercicio 3 - Sistema de login")
        print(f"  [{amarillo('4')}] Ejercicio 4 - Ej extra sistema de descuento por edad")
        print(SEPARADOR)
        print(f"  [{amarillo('0')}]  Volver al menú principal")
        print(SEPARADOR)

        op = input("\n  Opción: ").strip()

        if op == "0":
            break
        elif op == "1": _ej1()
        elif op == "2": _ej2()
        elif op == "3": _ej3()
        elif op == "4": _ej4()
        else:
            error("opción incorrecta, por favor ingresar un num válido")
            pausar()

def _ej1():
    titulo("BLOQUE 05_condicionales - Ejercicio 1")
    num = int(input("Ingrese un número para verificar si es par o impar: "))
    if num % 2 == 0:
        print(f"El num {num} es par")
    else:
        print(f"El num {num} es impar")

    pausar()

def _ej2():
    titulo("BLOQUE 05_condicionales - Ejercicio 2")
    nota = int(input("Ingrese su nota: "))
    if nota < 0 or nota > 10:
       print("Nota inválida, ingrese entre 0 y 10")
    elif nota >= 9:
       print("Su calificación es A")
    elif nota >= 7:
       print("Su calificación es B")
    elif nota >= 5:
       print("Su calificación es C")
    else:
       print("Su calificación es D")


    pausar()

def _ej3():
    titulo("BLOQUE 05_condicionales - Ejercicio 3")
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")
    if usuario == "admin" and contraseña == "123":
        print("Bienvenido")
    else:
        print("Acceso denegado")

    pausar()

def _ej4():
    titulo("BLOQUE 05_condicionales - Ejercicio 4")
    precio = float(input("El precio del producto es: "))
    edad = int(input("¿Qué edad tiene?: "))
    if precio <= 0:
        print("Precio inválido")
        return
    if edad < 0:
        print("Edad inválida, ingrese entre 0 y 10")
        return
    elif edad <= 12:
        descuento = (precio * 20)/100
    elif edad > 12 and edad <= 17:
        descuento = (precio * 10)/100
    elif edad >= 18 and edad < 65:
        descuento = 0
    elif edad >= 65:
        descuento = (precio * 15)/100
    
    print(f"Precio original: {precio}")
    print(f"Descuento: {descuento}")
    print(f"Precio final: {precio - descuento}")

    pausar()