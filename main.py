from utils.consola import (
    limpiar, pausar, titulo, subtitulo,
    SEPARADOR, amarillo, cyan, negrita, error
)

from modules import (
    bloque_00_intro,
    bloque_01_constructor,
    bloque_02_variables,
    bloque_03_operadores,
    bloque_04_io,
    bloque_05_condicionales,
    bloque_06_bucles,
    bloque_07_funciones,
    bloque_08_listas,
    bloque_09_tuplas,
    bloque_10_diccionarios,
    bloque_11_conjuntos,
    bloque_12_excepciones,
    bloque_13_decoradores,
    bloque_14_unpacking,
    bloque_15_orden_superior,
    bloque_16_archivos_json,
)
from modules.bloque_17_mixins import menu as menu_17

BLOQUES = [
    (" 0", "Introducción a la POO",       bloque_00_intro.menu),
    (" 1", "Constructor __init__",         bloque_01_constructor.menu),
    (" 2", "Variables y Tipos de Datos",   bloque_02_variables.menu),
    (" 3", "Operadores",                   bloque_03_operadores.menu),
    (" 4", "Entrada y Salida",             bloque_04_io.menu),
    (" 5", "Condicionales",                bloque_05_condicionales.menu),
    (" 6", "Bucles",                       bloque_06_bucles.menu),
    (" 7", "Funciones",                    bloque_07_funciones.menu),
    (" 8", "Listas",                       bloque_08_listas.menu),
    (" 9", "Tuplas",                       bloque_09_tuplas.menu),
    ("10", "Diccionarios",                 bloque_10_diccionarios.menu),
    ("11", "Conjuntos (set)",              bloque_11_conjuntos.menu),
    ("12", "Excepciones",                  bloque_12_excepciones.menu),
    ("13", "Decoradores",                  bloque_13_decoradores.menu),
    ("14", "Unpacking",                    bloque_14_unpacking.menu),
    ("15", "Funciones de Orden Superior",  bloque_15_orden_superior.menu),
    ("16", "Archivos y JSON",              bloque_16_archivos_json.menu),
    ("17", "Mixins",                       menu_17),
]


def mostrar_menu():
    titulo("GUÍA PRÁCTICA 1  —  POO en Python")
    print(f"  {cyan('Selecciona un bloque:')}\n")
    for num, nombre, _ in BLOQUES:
        print(f"  [{amarillo(num)}]  {nombre}")
    print()
    print(SEPARADOR)
    print(f"  [{amarillo(' S')}]  Salir")
    print(SEPARADOR)

def main():
    while True:
        mostrar_menu()
        op = input("\n  Opción: ").strip().upper()

        if op == "S":
            limpiar()
            print("\n  ¡Hasta luego!\n")
            break

        encontrado = False
        for num, _, fn_menu in BLOQUES:
            if op == num.strip():
                fn_menu()
                encontrado = True
                break

        if not encontrado:
            error("Opción no válida.")
            pausar()


if __name__ == "__main__":
    main()