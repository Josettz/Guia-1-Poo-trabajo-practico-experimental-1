import os


def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def gotoxy(x, y):
    print(f"\033[{y};{x}H", end="", flush=True)


def pausar():
    input("\n  Presiona Enter para continuar...")


ANCHO = 52

def titulo(texto):
    limpiar()
    print(SEPARADOR_DOBLE)
    print(f"  {texto}".center(ANCHO))
    print(SEPARADOR_DOBLE)
    print()

def subtitulo(texto):
    print(f"\n  ── {texto} ──\n")

SEPARADOR       = "─" * ANCHO
SEPARADOR_DOBLE = "═" * ANCHO


def _color(texto, cod):
    return f"\033[{cod}m{texto}\033[0m"

def verde(t):    return _color(t, 32)
def rojo(t):     return _color(t, 31)
def azul(t):     return _color(t, 34)
def amarillo(t): return _color(t, 33)
def cyan(t):     return _color(t, 36)
def negrita(t):  return _color(t, 1)



def ok(msg):    print(f"  {verde('✔')}  {msg}")
def error(msg): print(f"  {rojo('✘')}  {msg}")
def info(msg):  print(f"  {cyan('ℹ')}  {msg}")


def pedir_entero(prompt):
    while True:
        try:
            return int(input(f"  {prompt}: "))
        except ValueError:
            error("Ingresa un número entero válido.")

def pedir_float(prompt):
    while True:
        try:
            return float(input(f"  {prompt}: "))
        except ValueError:
            error("Ingresa un número decimal válido.")

def pedir_texto(prompt):
    while True:
        valor = input(f"  {prompt}: ").strip()
        if valor:
            return valor
        error("El campo no puede estar vacío.")