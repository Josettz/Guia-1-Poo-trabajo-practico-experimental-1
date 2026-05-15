git add README.md# 🐍 Guía Práctica Experimental N°1 — POO en Python

## 👨‍💻 Información 

| Campo | Detalle |
|-------|---------|
| **Nombre** | Jose Antonio Torres Torres |
| **Carrera** | Ingeniería en Software |
| **Semestre** | 4to Semestre |
| **Institución** | Universidad Estatal de Milagro — UNEMI |
| **Materia** | Programación Orientada a Objetos |
| **Trabajo** | S3 — Trabajo Práctico Experimental #1 |
| **Fecha de entrega** | Jueves, 15 de mayo de 2026 |

---

## 📋 Descripción

Proyecto interactivo de consola que cubre **18 bloques temáticos** de Programación Orientada a Objetos en Python. Cada bloque contiene ejercicios prácticos navegables desde un menú general, con submenús por bloque.

---

## 🗂️ Estructura del Proyecto

```
Guia 1/
│
├── main.py                        # Punto de entrada — menú principal
│
├── utils/
│   └── consola.py                 # Librería de utilidades de terminal
│
└── modules/
    ├── bloque_00_intro.py         # Introducción a la POO
    ├── bloque_01_constructor.py   # Constructor __init__
    ├── bloque_02_variables.py     # Variables y Tipos de Datos
    ├── bloque_03_operadores.py    # Operadores
    ├── bloque_04_io.py            # Entrada y Salida
    ├── bloque_05_condicionales.py # Condicionales
    ├── bloque_06_bucles.py        # Bucles
    ├── bloque_07_funciones.py     # Funciones
    ├── bloque_08_listas.py        # Listas
    ├── bloque_09_tuplas.py        # Tuplas
    ├── bloque_10_diccionarios.py  # Diccionarios
    ├── bloque_11_conjuntos.py     # Conjuntos (set)
    ├── bloque_12_excepciones.py   # Excepciones
    ├── bloque_13_decoradores.py   # Decoradores
    ├── bloque_14_unpacking.py     # Unpacking
    ├── bloque_15_orden_superior.py# Funciones de Orden Superior
    ├── bloque_16_archivos_json.py # Archivos y JSON
    └── bloque_17_mixins/
        ├── __init__.py
        ├── ej1_promedio.py
        ├── ej2_validacion.py
        └── ej3_exportar.py
```

---

## 🧩 Bloques Temáticos

| # | Tema | Conceptos Clave |
|:-:|------|-----------------|
| 00 | **Introducción a la POO** | Clase, objeto, instancia, paradigma |
| 01 | **Constructor `__init__`** | `self`, parámetros por defecto, `@classmethod` |
| 02 | **Variables y Tipos** | `int`, `float`, `str`, `bool`, `list`, `dict`, `set`, slicing |
| 03 | **Operadores** | Aritméticos, comparación, lógicos, precedencia, `==` vs `is` |
| 04 | **Entrada y Salida** | `input()`, `print()`, f-strings, casting |
| 05 | **Condicionales** | `if/elif/else`, ternario, `match-case`, short-circuit |
| 06 | **Bucles** | `for`, `while`, `break`, `continue`, list comprehension |
| 07 | **Funciones** | `*args`, `**kwargs`, `lambda`, recursividad |
| 08 | **Listas** | Métodos, `sort()`, referencia vs copia |
| 09 | **Tuplas** | Inmutabilidad, unpacking, conversión |
| 10 | **Diccionarios** | Acceso, métodos, dict comprehension, anidados |
| 11 | **Conjuntos** | Unión, intersección, diferencia, deduplicación |
| 12 | **Excepciones** | `try/except/else/finally`, `raise`, excepciones personalizadas |
| 13 | **Decoradores** | `wrapper`, `@decorador`, casos de uso reales |
| 14 | **Unpacking** | `*`, `**`, en funciones y bucles |
| 15 | **Funciones de Orden Superior** | `map()`, `filter()`, `reduce()` |
| 16 | **Archivos y JSON** | `open()`, modos, `json.dump()`, `json.load()` |
| 17 | **Mixins** | Herencia múltiple, MRO, reutilización de código |

---

## ▶️ Cómo ejecutar

**Requisitos:** Python 3.10 o superior

```bash
# Ubicarse en la carpeta del proyecto
cd "Guia 1"

# Ejecutar
python main.py
```

Navegación completamente por teclado desde el menú de consola.

---

## 🛠️ Módulo `utils/consola.py`

Librería interna de utilidades visuales para la terminal:

| Función | Descripción |
|---------|-------------|
| `limpiar()` | Limpia la pantalla (`cls` en Windows / `clear` en Linux) |
| `pausar()` | Pausa la ejecución hasta presionar Enter |
| `gotoxy(x, y)` | Posiciona el cursor con escape ANSI `\033[y;xH` |
| `titulo(texto)` | Encabezado principal centrado con `═══` |
| `subtitulo(texto)` | Encabezado secundario con `──` |
| `verde/rojo/cyan/amarillo/negrita(t)` | Colores ANSI |
| `ok(msg)` | Mensaje de éxito `✔` en verde |
| `error(msg)` | Mensaje de error `✘` en rojo |
| `info(msg)` | Mensaje informativo `ℹ` en cyan |
| `pedir_entero(prompt)` | Input validado para enteros |
| `pedir_float(prompt)` | Input validado para decimales |
| `pedir_texto(prompt)` | Input validado para texto no vacío |

---

## 🤖 Documentación del Uso de IA

> **IA utilizada:** Claude (Anthropic) — claude.ai

---

### BLOQUE 00 — Introducción a la POO

**Prompt para entender el ejercicio:**
> "Explícame qué es la Programación Orientada a Objetos, la diferencia entre clase y objeto, y cómo identificar clases en un sistema del mundo real como una biblioteca."

**Prompt para generar un proceso similar:**
> "Genera un ejercicio similar donde tenga que identificar 5 clases para un sistema de hospital, y crear una clase simple con nombre y especialidad."

**Resolución propia:** Se identificaron las clases `Libro`, `Usuario`, `Prestamo`, `Autor`, `Categoria` para el sistema de biblioteca, y se creó la clase `Persona` con atributos `nombre` y `edad`, instanciando 3 objetos distintos.

---

### BLOQUE 01 — Constructor `__init__`

**Prompt para entender el ejercicio:**
> "Explícame cómo funciona el constructor __init__ en Python, para qué sirve self, y cómo agregar validaciones dentro del constructor."

**Prompt para generar un proceso similar:**
> "Dame un ejercicio similar donde tenga que crear una clase Vehiculo con marca, modelo y año, con validación de que el año no sea negativo, y un @classmethod que cree el objeto desde un diccionario."

**Resolución propia:** Se creó la clase `Producto` con código, nombre y precio, validando que el precio no sea negativo. Se añadió `Estudiante` con lista de notas por defecto vacía y constructor alternativo `desde_diccionario`.

---

### BLOQUE 02 — Variables y Tipos de Datos

**Prompt para entender el ejercicio:**
> "Explícame los tipos de datos en Python (int, float, str, bool, list, tuple, dict, set), cómo acceder por índice y cómo funciona el slicing."

**Prompt para generar un proceso similar:**
> "Genera un ejercicio donde declare variables de cada tipo, cree una lista de 5 nombres y practique slicing para obtener distintas porciones."

**Resolución propia:** Se declararon variables de todos los tipos, se creó una lista con 5 elementos y se aplicó slicing. Se creó una clase con un método que maneja `str`, `list` y `dict` simultáneamente.

---

### BLOQUE 03 — Operadores

**Prompt para entender el ejercicio:**
> "Explícame todos los operadores en Python: aritméticos, de comparación y lógicos. También explícame la diferencia entre == e is, y cómo funciona la precedencia de operadores."

**Prompt para generar un proceso similar:**
> "Dame un ejercicio con a=15, b=3 donde use todos los operadores aritméticos, y otro que demuestre la diferencia entre == e is con dos listas de contenido idéntico."

**Resolución propia:** Se usó `a=20, b=4` con todos los operadores. Se demostró que dos listas con igual contenido tienen `== True` pero `is False`. Se evaluó y explicó `x = 2 + 1 * 2 % 2 + (2**1)//2` → resultado `3`.

---

### BLOQUE 04 — Entrada y Salida

**Prompt para entender el ejercicio:**
> "Explícame cómo funciona print() con f-strings, sep y end, y por qué input() siempre devuelve string. ¿Qué pasa si intento sumar un input sin convertirlo?"

**Prompt para generar un proceso similar:**
> "Genera un ejercicio donde pida nombre y edad al usuario, calcule el año de nacimiento y lo muestre con f-string formateado."

**Resolución propia:** Se solicitó nombre y edad con f-string. Se leyeron dos números y se calculó suma y promedio. Se demostró la concatenación inesperada: `"10" + "5" = "105"`.

---

### BLOQUE 05 — Condicionales

**Prompt para entender el ejercicio:**
> "Explícame if/elif/else en Python, el operador ternario, match-case y cómo funciona la evaluación corta (short-circuit) con and/or."

**Prompt para generar un proceso similar:**
> "Dame un ejercicio de sistema de descuentos: si el cliente tiene más de 5 compras y es VIP, 30% de descuento; si solo es VIP, 15%; si no, precio normal."

**Resolución propia:** Se creó un programa para detectar par/impar, un clasificador de notas (A/B/C/D) y un sistema de login que valida usuario y contraseña con `and`.

---

### BLOQUE 06 — Bucles

**Prompt para entender el ejercicio:**
> "Explícame for, while, break, continue y enumerate() en Python. También explícame list comprehension con condición."

**Prompt para generar un proceso similar:**
> "Genera un ejercicio donde recorra una lista de productos con enumerate() y otro donde cree una list comprehension con los cubos de los números impares del 1 al 10."

**Resolución propia:** Se imprimieron números del 1 al 10 con `while`. Se recorrió lista de frutas con `enumerate()`. Se generó `[4, 16, 36, 64, 100]` con list comprehension.

---

### BLOQUE 07 — Funciones

**Prompt para entender el ejercicio:**
> "Explícame cómo definir funciones en Python con parámetros por defecto, *args, **kwargs, funciones lambda y recursividad con factorial y fibonacci."

**Prompt para generar un proceso similar:**
> "Dame un ejercicio donde cree una función recursiva para calcular la suma de los primeros n números naturales, y otra con *args que calcule el producto de todos los argumentos."

**Resolución propia:** Se creó `doble(x)`, una función que suma con `*args`, y la función recursiva `factorial(n)` que produce `factorial(5) = 120`.

---

### BLOQUE 08 — Listas

**Prompt para entender el ejercicio:**
> "Explícame los métodos principales de las listas en Python (append, extend, insert, pop, sort, etc.) y la diferencia entre referencia y copia con .copy()."

**Prompt para generar un proceso similar:**
> "Dame un ejercicio donde cree una lista de calificaciones, la ordene, calcule el promedio, y demuestre qué pasa al asignar la lista a otra variable sin .copy()."

**Resolución propia:** Se creó una lista, se agregaron 3 elementos con `append()`, se ordenó. Se calculó suma, máximo y mínimo. Se demostró que sin `.copy()` ambas variables apuntan al mismo objeto.

---

### BLOQUE 09 — Tuplas

**Prompt para entender el ejercicio:**
> "Explícame por qué las tuplas son inmutables, cómo funciona el unpacking con *, y cuándo conviene usar tuplas en lugar de listas."

**Prompt para generar un proceso similar:**
> "Genera un ejercicio donde use unpacking de tuplas para intercambiar dos variables sin variable temporal, y otro donde recorra una lista de coordenadas (x, y, z)."

**Resolución propia:** Se intentó modificar una tupla y se observó el `TypeError`. Se usó `a, b, *resto = (100, 200, 300, 400)`. Se recorrió lista de coordenadas con `for x, y in coordenadas`.

---

### BLOQUE 10 — Diccionarios

**Prompt para entender el ejercicio:**
> "Explícame cómo acceder, modificar y eliminar elementos de un diccionario en Python, la diferencia entre [] y .get(), y cómo funcionan los diccionarios anidados."

**Prompt para generar un proceso similar:**
> "Dame un ejercicio con un diccionario de inventario donde pueda agregar productos, actualizar cantidades y mostrar todos los items con sus valores."

**Resolución propia:** Se creó un dict de persona, se accedió con `[]` y con `get()`. Se iteró sobre `.items()`. Se demostró el problema de referencia sin `.copy()`.

---

### BLOQUE 11 — Conjuntos (set)

**Prompt para entender el ejercicio:**
> "Explícame los conjuntos en Python: por qué eliminan duplicados, las operaciones matemáticas (unión, intersección, diferencia) y la diferencia simétrica."

**Prompt para generar un proceso similar:**
> "Genera un ejercicio con dos grupos de estudiantes matriculados en materias distintas, donde encuentre los que están en ambas, solo en una, y en ninguna."

**Resolución propia:** Se crearon dos conjuntos y se calcularon unión, intersección y diferencia. Se eliminaron duplicados con `set()`. Se calculó `(A|B) - (A&B)` como diferencia simétrica.

---

### BLOQUE 12 — Excepciones

**Prompt para entender el ejercicio:**
> "Explícame la estructura try/except/else/finally en Python, cómo lanzar errores con raise, cómo crear excepciones personalizadas y para qué sirve assert."

**Prompt para generar un proceso similar:**
> "Dame un ejercicio donde capture múltiples excepciones al dividir números ingresados por el usuario, incluyendo ValueError y ZeroDivisionError."

**Resolución propia:** Se capturó `ValueError` al convertir input. Se capturó `IndexError` al acceder fuera de rango. Se manejaron `ValueError` y `ZeroDivisionError` en un solo bloque.

---

### BLOQUE 13 — Decoradores

**Prompt para entender el ejercicio:**
> "Explícame cómo funcionan los decoradores en Python: qué es una función wrapper, cómo se aplica con @, y para qué se usan en proyectos reales."

**Prompt para generar un proceso similar:**
> "Genera un decorador que mida el tiempo de ejecución de una función y lo imprima en milisegundos."

**Resolución propia:** Se creó un decorador que imprime "Iniciando..." antes de ejecutar. Se creó un decorador que valida que el argumento sea positivo antes de calcular su cuadrado.

---

### BLOQUE 14 — Unpacking

**Prompt para entender el ejercicio:**
> "Explícame el unpacking en Python con *, cómo usarlo en funciones con *lista y **dict, y cómo combinar dos diccionarios con ** sin modificar el original."

**Prompt para generar un proceso similar:**
> "Dame un ejercicio donde desempaquete una lista de 6 elementos en primera, *medio, ultima, y otro donde combine tres diccionarios en uno nuevo."

**Resolución propia:** Se desempaquetó `(10, 20, 30, 40)` en `primera, *mitad, ultima`. Se pasó `[2,3,4]` con `*lista`. Se combinaron dos dicts con `**`.

---

### BLOQUE 15 — Funciones de Orden Superior

**Prompt para entender el ejercicio:**
> "Explícame map(), filter() y reduce() en Python con lambdas, y cómo encadenarlos para transformar y filtrar una colección en un solo paso."

**Prompt para generar un proceso similar:**
> "Genera un ejercicio donde use map() para convertir precios de dólares a pesos, filter() para quedarse con los mayores a 100, y reduce() para sumarlos."

**Resolución propia:** `map()` sobre `[2,4,6]` → `[3,5,7]`. `filter()` de mayores a 3. `reduce()` multiplicando `[1,2,3,4]` → `24`.

---

### BLOQUE 16 — Archivos y JSON

**Prompt para entender el ejercicio:**
> "Explícame cómo leer y escribir archivos de texto en Python con open() y with, los modos r/w/a/x, y cómo guardar y cargar datos con json.dump() y json.load()."

**Prompt para generar un proceso similar:**
> "Dame un ejercicio donde guarde una lista de productos con nombre y precio en un archivo JSON, lo vuelva a cargar y muestre solo los que cuestan más de 50."

**Resolución propia:** Se escribió y leyó un archivo de texto. Se guardó y cargó `{"x":10, "y":20}` en JSON. Se recorrió una lista de 2 usuarios desde JSON con `for u in data`.

---

### BLOQUE 17 — Mixins

**Prompt para entender el ejercicio:**
> "Explícame qué es un Mixin en Python, cómo difiere de la herencia normal, para qué sirve el MRO, y cómo implementar un PromedioMixin, un ValidacionMixin y un ExportarMixin."

**Prompt para generar un proceso similar:**
> "Genera un ejercicio con un LogMixin que registre en un archivo cada vez que se llama a un método, e intégralo en una clase Producto."

**Resolución propia:**
- **Ejercicio 1:** `PromedioMixin` con `calcular_promedio(notas)` integrado en clase `Estudiante`. Notas `[8, 9, 10]` → promedio `9.0`.
- **Ejercicio 2:** `ValidacionMixin` con `validar_email()` (verifica `@` y `.com`) y `validar_edad()` (≥ 18) integrado en clase `Usuario`.
- **Ejercicio 3:** `ExportarMixin` con `exportar_json(datos)` y `exportar_csv(datos)` integrado en clase `Reporte`.

---

## 📊 Vista del Menú Principal

```
════════════════════════════════════════════════════════
         GUÍA PRÁCTICA 1  —  POO en Python
════════════════════════════════════════════════════════

  Selecciona un bloque:

  [ 0]  Introducción a la POO
  [ 1]  Constructor __init__
  [ 2]  Variables y Tipos de Datos
  [ 3]  Operadores
  [ 4]  Entrada y Salida
  [ 5]  Condicionales
  [ 6]  Bucles
  [ 7]  Funciones
  [ 8]  Listas
  [ 9]  Tuplas
  [10]  Diccionarios
  [11]  Conjuntos (set)
  [12]  Excepciones
  [13]  Decoradores
  [14]  Unpacking
  [15]  Funciones de Orden Superior
  [16]  Archivos y JSON
  [17]  Mixins

────────────────────────────────────────────────────────
  [ S]  Salir
────────────────────────────────────────────────────────
```

---

<div align="center">

Desarrollado por **Jose Antonio Torres Torres**
🏛️ Universidad Estatal de Milagro — UNEMI · 2026

</div>