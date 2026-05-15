from utils.consola import limpiar, pausar, titulo, amarillo, error, SEPARADOR


def menu():
    while True:
        titulo("BLOQUE 08_listas  — métodos y operaciones")
        print(f"  [{amarillo('1')}] Ejercicio 1 - Agregar elementos con append y ordenar")
        print(f"  [{amarillo('2')}] Ejercicio 2 - Suma, máximo y mínimo de una lista")
        print(f"  [{amarillo('3')}] Ejercicio 3 - Referencia vs copia de lista")
        print(f"  [{amarillo('4')}] Ejercicio 4 - Ej extra insert, pop, count e index")
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
    titulo("BLOQUE 08_listas - Ejercicio 1")
    lista = [1, 2, 3]
    lista.append(4)
    lista.append(5)
    lista.append(6)
    lista.sort()
    print(lista)

    pausar()

def _ej2():
    titulo("BLOQUE 08_listas - Ejercicio 2")
    lista = [5,3,8,1,9,3]
    lista_min = min(lista)
    lista_max = max(lista)
    lista_sum = sum(lista)
    print(f"El mínimo de la lista: {lista_min}")
    print(f"El máximo de la lista: {lista_max}")
    print(f"La suma de la lista: {lista_sum}")

    pausar()

def _ej3():
    titulo("BLOQUE 08_listas - Ejercicio 3")
    print("¿Qué pasa si haces copia=lista y luego copia.append(4)?")
    lista = [1, 2, 3]
    copia = lista
    copia.append(4)
    print(f"lista: {lista}")
    print(f"copia: {copia}")

    lista2 = [1, 2, 3]
    copia2 = lista2.copy()
    copia2.append(4)
    print(f"lista2: {lista2}")
    print(f"copia2: {copia2}")
    print("lista también cambia porque ambas variables apuntan al mismo objeto, si no quiero que pase esto puedo usar el .copy() para no modificar la lista ")


    pausar()

def _ej4():
    titulo("BLOQUE 08_listas - Ejercicio 4")
    lista = [1, 2, 3, 4, 5, 5]
    lista.insert(2, 7)
    print(f"Lista con inserción: {lista}")
    lista.pop()
    print(f"Lista sin último: {lista}")
    print(f"Veces que aparece el 5: {lista.count(5)}")
    print(f"Posición del 3: {lista.index(3)}")

    pausar()