from utils.consola import limpiar, pausar, titulo, amarillo, error, SEPARADOR


def menu():
    while True:
        titulo("BLOQUE 02_variables  — Colecciones")
        print(f"  [{amarillo('1')}] Ejercicio 1 - Declarar variables de cada tipo simple y complejas")
        print(f"  [{amarillo('2')}] Ejercicio 2 - Crea una lista con 5 elementos. Imprime el primero, el último y lista[1:4]")
        print(f"  [{amarillo('3')}] Ejercicio 3 - Crea una clase con un método que declare un str, una list y un dict")
        print(f"  [{amarillo('4')}] Ejercicio 4 - Ej extra crear una clase Inventario y usar: slicing de string, mostrar últimos 2 datos de una lista y mostrar un valor de un dict") 
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
    titulo("BLOQUE 02_variables - Ejercicio 1")
    variable1 = "variable 1"
    variable2 = 1
    variable3 = True
    variable4 = 3.14
    variable5 = None
    print(f"{variable1}, {variable2}, {variable3}, {variable4}, {variable5} ")

    vardict = { "variable1": "variable 1",
               "variable2": True,
               "variable3": 10

    }

    varlist = [1,2,3,4,5]
    vartuple = (1,2,3,4,5)
    varset = {1, 1, 2, 3, 4, 5}

    print(vardict)
    print(varlist)
    print(vartuple)
    print(varset)
    pausar()



def _ej2():
    titulo("BLOQUE 02_variables - Ejercicio 2")
    lista = [1,2,3,4,5]
    print(lista[0])
    print(lista[-1])
    print(lista[1:4])
    pausar()

        
def _ej3():
    titulo("BLOQUE 02_variables - Ejercicio 3")
    class ej3:
      def mostrar(self):
        texto = "hola mundo"
        lista = [1, 2, 3, 4, 5]
        diccionario = {"nombre": "Juan", "edad": 20}
        print(texto[0])
        print(lista[-1])
        print(diccionario["nombre"])
    

    obj = ej3()
    obj.mostrar()
    pausar()

def _ej4():
    titulo("BLOQUE 02_variables - Ejercicio 4")
    class inventario:
        def resumen(self):
            nombre_tienda = "tuti"
            lista_productos = ["coca cola", "mortadela", "kiwis"]
            stock_productos = {"coca cola": 162, "mortadela": 84, "kiwis": 120}

            print(nombre_tienda[:3])
            print(lista_productos[-2:])
            print(stock_productos["coca cola"])


    mostrar = inventario()
    mostrar.resumen()
    pausar()
 

        