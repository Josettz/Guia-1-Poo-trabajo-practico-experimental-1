from utils.consola import limpiar, pausar, titulo, amarillo, error, SEPARADOR

def menu():
    while True:
        titulo("BLOQUE 00_intro  —  Introducción a la POO")
        print(f"  [{amarillo('1')}]  Ejercicio 1 - Identificación de 5 clases de una biblioteca ")
        print(f"  [{amarillo('2')}]  Ejercicio 2 - Creación de la clase Persona con nombre y edad, con su instanciación")
        print(f"  [{amarillo('3')}]  Ejercicio 3 - Explicación con mis propias palabras de que es clase y objeto")
        print(f"  [{amarillo('4')}]  Ejercicio 4 - Ej extra una clase auto y sus atributos")
        print()
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
            error("Opción no válida.")
            pausar()


def _ej1():
    titulo("Bloque 00_intro — Ejercicio 1") 
    print("Clases: libro, usuario, prestamo, ejemplar, multa, autor, categoria")
    pausar()


def _ej2():
    titulo("Bloque 00_intro — Ejercicio 2")
    class Persona:
        def __init__(self, nombre, edad, genero):
            self.nombre = nombre
            self.edad = edad
            self.genero = genero
    p1 = Persona("Elian", 54, "masculino")
    p2 = Persona("Belfor", 22, "masculino")
    p3 = Persona("Carlos", 20, "masculino")

    print(f"{p1.nombre}, {p1.edad}, {p1.genero}")
    print(f"{p2.nombre}, {p2.edad}, {p2.genero}")
    print(f"{p3.nombre}, {p3.edad}, {p3.genero}")
    pausar()


def _ej3():
    titulo("Bloque 00_intro — Ejercicio 3")
    print("Una clase es el molde o plantilla que define qué atributos y comportamientos tendrá algo. Un objeto es una instancia concreta creada a partir de ese molde, con sus propios valores. (le da vida al molde)")
    pausar()

def _ej4():
    titulo("Bloque 00_intro - Ejercicio 4")
    class Auto:
        def __init__(self, modelo, color):
            self.modelo = modelo
            self.color = color
    
    c1 = Auto("Nissan", "Negro")
    c2 = Auto("Chevrolet", "Rojo")

    print(f"{c1.modelo}, {c1.color}")
    print(f"{c2.modelo}, {c2.color}")
    pausar()