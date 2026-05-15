from utils.consola import limpiar, pausar, titulo, amarillo, error, SEPARADOR


def menu():
    while True:
        titulo("BLOQUE 04_io  — personalización")
        print(f"  [{amarillo('1')}] Ejercicio 1 - input de nombre y edad con f-string")
        print(f"  [{amarillo('2')}] Ejercicio 2 - Suma y promedio de dos números")
        print(f"  [{amarillo('3')}] Ejercicio 3 - Concatenación sin casting")
        print(f"  [{amarillo('4')}] Ejercicio 4 - Ej extra validar nombre, edad y altura")
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
    titulo("BLOQUE 04_io - Ejercicio 1")

    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    print(f"Soy {nombre} y mi edad es {edad}")

    pausar()

def _ej2():
    titulo("BLOQUE 04_io - Ejercicio 2")
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    suma = num1 + num2
    promedio = suma/2
    print(f"La suma es: {suma}")
    print(f"El promedio es: {promedio}")

    pausar()

def _ej3():
    titulo("BLOQUE 04_io - Ejercicio 3")
    num1 = input("Ingrese el primer número: ")
    num2 = input("Ingrese el segundo número: ")
    suma = num1 + num2
    print(f"La concatenación es: {suma}")
  
    pausar()

def _ej4():
    titulo("BLOQUE 04_io - Ejercicio 4")
    nombre = input("Ingrese su nonbre: ")
    edad = int(input("Ingrese su edad: "))
    altura = float(input("Ingrese su altura: "))

    if edad <= 0 or altura <= 0:
      print("Datos inválidos")
      return
    
    eres_mayor_de_edad = edad >= 18

    print(f"Nombre: {nombre}")
    print(f"Edad: {edad}")
    print(f"Altura: {altura}")
    print(f"Eres mayor de edad: {eres_mayor_de_edad}")

    pausar()