from utils.consola import limpiar, pausar, titulo, amarillo, error, SEPARADOR


def menu():
    while True:
        titulo("BLOQUE 07_funciones  — function")
        print(f"  [{amarillo('1')}] Ejercicio 1 - Doble de un número")
        print(f"  [{amarillo('2')}] Ejercicio 2 - Suma con *args")
        print(f"  [{amarillo('3')}] Ejercicio 3 - Factorial recursivo")
        print(f"  [{amarillo('4')}] Ejercicio 4 - Ej extra perfil con **kwargs")
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
    titulo("BLOQUE 07_funciones - Ejercicio 1")
    def doble_num(x):
        return x * 2
    
    print(doble_num(2))

    
    pausar()

def _ej2():
    titulo("BLOQUE 07_funciones - Ejercicio 2")
    def suma(*args):
        return sum(args)
    
    print(suma(1,2,3,4,5))

    pausar()

def _ej3():
    titulo("BLOQUE 07_funciones - Ejercicio 3")
    def factorial(n):
      if n == 0: return 1           
      return n * factorial(n - 1)
    
    print(factorial(5))

    pausar()


def _ej4():
    titulo("BLOQUE 07_funciones - Ejercicio 4")
    def crear_perfil(**kwargs):
        for clave, valor in kwargs.items():
          print(f"{clave}: {valor}")

    crear_perfil(nombre ="Jose", edad = 25, ciudad = "Guayaquil", profesion = "Desarrollador" )

    pausar()
    