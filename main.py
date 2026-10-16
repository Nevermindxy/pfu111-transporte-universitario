
from trufi import Trufi
from minibus import Minibus
from radiotaxi import Radiotaxi

vehiculos = []   



def leer_texto(msg):
    while True:
        valor = input(msg).strip()
        if valor:
            return valor
        print("  Error: no puede estar vacio.")


def leer_entero(msg):
    while True:
        try:
            valor = int(input(msg))
            if valor < 0:
                print("  Error: no puede ser negativo.")
                continue
            return valor
        except ValueError:
            print("  Error: ingrese un numero entero valido.")


def leer_decimal(msg, minimo_exclusivo=False):
    while True:
        try:
            valor = float(input(msg))
            if valor < 0 or (minimo_exclusivo and valor == 0):
                print("  Error: valor no valido (negativo o cero).")
                continue
            return valor
        except ValueError:
            print("  Error: ingrese un numero valido.")


def datos_comunes():
    codigo = leer_texto("Codigo: ")
    if any(v.codigo == codigo for v in vehiculos):
        print("  Error: ya existe un vehiculo con ese codigo.")
        return None
    marca = leer_texto("Marca: ")
    capacidad = leer_entero("Capacidad de pasajeros: ")
    kilometraje = leer_decimal("Kilometraje recorrido: ")
    return codigo, marca, capacidad, kilometraje


# ---------- Opciones del menu ----------
def registrar_trufi():
    datos = datos_comunes()
    if datos is None:
        return
    rutas = leer_entero("Numero de rutas: ")
    costo = leer_decimal("Costo por km (Bs): ", True)
    vehiculos.append(Trufi(*datos, rutas, costo))
    print("  Trufi registrado correctamente.")


def registrar_minibus():
    datos = datos_comunes()
    if datos is None:
        return
    viajes = leer_entero("Numero de viajes: ")
    costo = leer_decimal("Costo por km (Bs): ", True)
    vehiculos.append(Minibus(*datos, viajes, costo))
    print("  Minibus registrado correctamente.")


def registrar_radiotaxi():
    datos = datos_comunes()
    if datos is None:
        return
    area = leer_texto("Area asignada: ")
    costo = leer_decimal("Costo por km (Bs): ", True)
    vehiculos.append(Radiotaxi(*datos, area, costo))
    print("  Radiotaxi registrado correctamente.")


def mostrar_vehiculos():
    if not vehiculos:
        print("  No hay vehiculos registrados.")
        return
    for v in vehiculos:
        print(" ", v.mostrar_informacion())


def calcular_costos():
    if not vehiculos:
        print("  No hay vehiculos registrados.")
        return
    for v in vehiculos:                      # POLIMORFISMO: sin if/elif
        print(f"  {v.codigo}: {v.calcular_costo_operativo():.2f} Bs")


def calcular_total():
    total = sum(v.calcular_costo_operativo() for v in vehiculos)
    print(f"  Costo operativo total: {total:.2f} Bs")


def menu():
    opciones = {
        "1": registrar_trufi,
        "2": registrar_minibus,
        "3": registrar_radiotaxi,
        "4": mostrar_vehiculos,
        "5": calcular_costos,
        "6": calcular_total,
    }
    while True:
        print("\n=== TRANSPORTE UNIVERSITARIO ===")
        print("1. Registrar trufi")
        print("2. Registrar minibus")
        print("3. Registrar radiotaxi")
        print("4. Mostrar vehiculos registrados")
        print("5. Calcular costo operativo de cada vehiculo")
        print("6. Calcular costo operativo total")
        print("7. Salir")
        op = input("Elija una opcion: ").strip()
        if op == "7":
            print("Hasta luego.")
            break
        accion = opciones.get(op)
        if accion:
            accion()
        else:
            print("  Opcion no valida.")


if __name__ == "__main__":
    menu()

