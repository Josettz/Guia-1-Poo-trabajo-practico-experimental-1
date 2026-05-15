from utils.consola import limpiar, pausar, titulo, amarillo, error, SEPARADOR


def menu():
    while True:
        titulo("BLOQUE 09_tuplas  — Inmutabilidad y unpacking  ")
        print(f"  [{amarillo('1')}] Ejercicio 1 - Intentar modificar una tupla")
        print(f"  [{amarillo('2')}] Ejercicio 2 - Unpacking con *resto")
        print(f"  [{amarillo('3')}] Ejercicio 3 - Recorrer coordenadas")
        print(f"  [{amarillo('4')}] Ejercicio 4 - Ej extra convertir tupla a lista y viceversa ")
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
    titulo("BLOQUE 09_tuplas - Ejercicio 1")
    tupla = (1,2,3,4,5)
    try:
      tupla[0] = 10
    except TypeError as e:
      print(f"Error: {e}")

    pausar()

def _ej2():
    titulo("BLOQUE 09_tuplas - Ejercicio 2")
    a, b, *resto = (100, 200, 300, 400)
    print(f"a: {a}")
    print(f"b: {b}")
    print(f"resto: {resto}")

    pausar()

def _ej3():
    titulo("BLOQUE 09_tuplas - Ejercicio 3")
    coordenadas = [(1, 2), (3, 4), (5, 6)]
    for x, y in coordenadas:
        print(f"x={x}, y={y}")
    
    pausar()

def _ej4():
    titulo("BLOQUE 09_tuplas - Ejercicio 4")
    tupla = ("Jhoan", "Elian", "Belfor", "Isaac", "Jose")
    tupla = list(tupla)
    tupla.append("Jean")
    tupla.pop(0)
    tupla = tuple(tupla)
    print(tupla)

    pausar()
