from utils.consola import titulo, pausar, amarillo, error, SEPARADOR
from modules.bloque_17_mixins import ej1_promedio, ej2_validacion, ej3_exportar


def menu():
    while True:
        titulo("BLOQUE 17  —  Mixins")
        print(f"  [{amarillo('1')}]  Ejercicio 1 — PromedioMixin")
        print(f"  [{amarillo('2')}]  Ejercicio 2 — ValidacionMixin")
        print(f"  [{amarillo('3')}]  Ejercicio 3 — ExportarMixin")
        print()
        print(SEPARADOR)
        print(f"  [{amarillo('0')}]  Volver al menú principal")
        print(SEPARADOR)

        op = input("\n  Opción: ").strip()

        if   op == "0": break
        elif op == "1": ej1_promedio.ejecutar()
        elif op == "2": ej2_validacion.ejecutar()
        elif op == "3": ej3_exportar.ejecutar()
        else:
            error("Opción no válida.")
            pausar()