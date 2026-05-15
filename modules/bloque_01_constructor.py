from utils.consola import limpiar, pausar, titulo, amarillo, error, SEPARADOR


def menu():
    while True:
        titulo("BLOQUE 01_constructor  —  Constructor __init__")
        print(f"[{amarillo('1')}] Ejercicio 1 - Crear una clase de producto y instanciar 2 productos (validación con precios negativos)")
        print(f"[{amarillo('2')}] Ejercicio 2 - Crear clase con estudiante y si notas = None. Inicia lista vacia ")
        print(f"[{amarillo('3')}] Ejercicio 3 - Agrega un @classmethod desde_diccionario que cree un Estudiante desde un dict")
        print(f"[{amarillo('4')}] Ejercicio 4 - Ej extra una clase auto y sus atributos con @classmethod desde_cadena ")
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
            error("opción incorrecta, por favor ingresar un num válido")
            pausar()
    
def _ej1():
    titulo("BLOQUE 01_constructor  —  Ejercicio 1")
    class Producto:
        def __init__(self, codigo, nombre, precio):
            if precio < 0:
                raise ValueError("el precio no puede ser negativo")

            self.codigo = codigo
            self.nombre = nombre
            self.precio = precio
      

    prod1 = Producto("#1", "Aire acondicionado", 400)
    prod2 = Producto("#2", "Iphone 13 pro max", 450)
    
    print(f"{prod1.codigo}, {prod1.nombre}, {prod1.precio}")
    print(f"{prod2.codigo}, {prod2.nombre}, {prod2.precio}")
    pausar()
            
def _ej2():
    titulo("BLOQUE 01_constructor  —  Ejercicio 2")
    class Estudiante:
        def __init__(self, nombre, notas):
            if notas is None:
                notas = []
            self.nombre = nombre
            self.notas = notas
    
    p1 = Estudiante("Isaac Silva", None)
    p2 = Estudiante("Elian Galeas", None)

    print(f"{p1.nombre}, {p1.notas}")
    print(f"{p2.nombre}, {p2.notas}")
    pausar()
  

def _ej3():
    titulo("BLOQUE 01_constructor  —  Ejercicio 3")
    
    class Estudiante:
        def __init__(self, nombre, notas=None):
            if notas is None:
                notas = []
            self.nombre = nombre
            self.notas = notas
        
        @classmethod
        def desde_diccionario(cls, datos):
            return cls(datos["nombre"], datos["notas"])
    
    datos = {"nombre": "Ana", "notas": [8, 9, 10]}
    e = Estudiante.desde_diccionario(datos)
    print(f"{e.nombre}, {e.notas}")
    pausar()


def _ej4():
    titulo("BLOQUE 01_constructor  —  Ejercicio 4")
    class Auto:
        def __init__(self, marca, modelo, año):
            self.marca = marca
            self.modelo = modelo
            self.año = año
    
        @classmethod
        def desde_cadena(cls, datos):
            return cls(datos["marca"], datos["modelo"], datos["año"])
        @classmethod
        def from_text(cls, datos):
            partes = datos.split(",")
            return cls(partes[0], partes[1], partes[2])
        

    datos2 = Auto.from_text("Nissan, NP300, 1985")

    print(datos2.marca, datos2.modelo, datos2.año)       
    
    datos = {"marca": "Nissan", "modelo": "NP300", "año": 1985}
    e = Auto.desde_cadena(datos)
    print(f"{e.marca}, {e.modelo}, {e.año}")
    pausar()

    


     

