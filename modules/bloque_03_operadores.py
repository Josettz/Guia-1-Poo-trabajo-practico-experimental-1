from utils.consola import limpiar, pausar, titulo, amarillo, error, SEPARADOR


def menu():
    while True:
        titulo("BLOQUE 03_operadores  — Aritméticos")
        print(f"  [{amarillo('1')}] Ejercicio 1 - Operadores aritméticos con a=20, b=4")
        print(f"  [{amarillo('2')}] Ejercicio 2 - == vs is en listas idénticas")
        print(f"  [{amarillo('3')}] Ejercicio 3 - Precedencia de operadores")
        print(f"  [{amarillo('4')}] Ejercicio 4 - Verificar acceso con operadores lógicos")
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
    titulo("BLOQUE 03_operadores - Ejercicio 1")
    def operaciones(a=20,b=4):
        suma = a + b
        resta = a - b
        multi = a * b
        div = a / b
        res = a % b
        dive = a // b
        potencia = a ** b

        print(f"suma = {suma}")
        print(f"resta = {resta}")
        print(f"multiplicación = {multi}")
        print(f"división = {div}")
        print(f"residuo = {res}")
        print(f"división entera = {dive}")
        print(f"potencia = {potencia}")

    operaciones()


    pausar()

def _ej2():
    titulo("BLOQUE 03_operadores - Ejercicio 2")
    def verificar_lista():
        a = [1,2]
        b = [1,2]

        print(f"a == b: {a == b}")  
        print(f"a is b: {a is b}") 
        
    verificar_lista()
    pausar()

def _ej3():
    titulo("BLOQUE 03_operadores - Ejercicio 3")
    def prioridad_op():
         x = 2 + 1 * 2 % 2 + (2**1)//2
         print(f"x = {x}")
         print("Orden: ** → % → // → +")

    prioridad_op()

    pausar()

def _ej4():
    titulo("BLOQUE 03_operadores - Ejercicio 4")
    def verificar_acceso(edad, tiene_cuenta):

        if edad >= 18 and tiene_cuenta:
            puede_acceder = True
            motivo = "Acceso permitido"
        else:
            puede_acceder = False
            motivo = "No tiene cuenta" if edad >= 18 else "Menor de edad"

        print(f"Mayor de edad: {edad >= 18}")
        print(f"Puede acceder: {puede_acceder}")
        print(f"Motivo: {motivo}")

    verificar_acceso(20,True)
    
    pausar()

