from utils.consola import limpiar, pausar, titulo, amarillo, error, SEPARADOR


def menu():
    while True:
        titulo("BLOQUE 06_bucles  — while, for")
        print(f"  [{amarillo('1')}] Ejercicio 1 - Números del 1 al 10 con while")
        print(f"  [{amarillo('2')}] Ejercicio 2 - Recorrer lista con enumerate")
        print(f"  [{amarillo('3')}] Ejercicio 3 - Cuadrados de pares con compresión de listas")
        print(f"  [{amarillo('4')}] Ejercicio 4 - Ej extra aprobados y reprobados")
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
    titulo("BLOQUE 06_bucles - Ejercicio 1")
    i = 1
    while i <= 10:
        print(i)
        i = i + 1

    pausar()

def _ej2():
    titulo("BLOQUE 06_bucles - Ejercicio 2")
    lista = ["Manzana", "Pera", "Uvas"]
    for indice, fruta in enumerate(lista):
        print(f"{indice}: {fruta}")
    
    pausar()
    
def _ej3():
    titulo("BLOQUE 06_bucles - Ejercicio 3")
    cuadrado_pares = [n**2 for n in range(1,11) if n % 2 == 0]
    print(cuadrado_pares)
    
    pausar()
    
def _ej4():
    titulo("BLOQUE 06_bucles - Ejercicio 4")

    Estudiantes = [{"Nombre": "Jose", "Nota": 20},
                   {"Nombre": "Elian", "Nota": 22},
                   {"Nombre": "Belfor", "Nota":21}]
    
    aprobados = 0
    reprobados = 0
    for i in Estudiantes:
        if i["Nota"] >= 5:
            aprobados = aprobados + 1
            print(f"- {i['Nombre']}: {i['Nota']} APROBO")
        else:
            reprobados = reprobados + 1
            print(f"- {i['Nombre']}: {i['Nota']} REPROBO")

    print(f"Aprobados: {aprobados} | Reprobados: {reprobados} ")

    pausar()
    