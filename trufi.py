# Integrante 2: Yasser Rodrigo Caba Murillo
# Clase Trufi

from vehiculo import Vehiculo


class Trufi(Vehiculo):

    def __init__(self, codigo, marca, capacidad, kilometraje, numero_rutas, costo_por_km):
        super().__init__(codigo, marca, capacidad, kilometraje)

        if numero_rutas < 0:
            raise ValueError("El numero de rutas no puede ser negativo")
        if costo_por_km <= 0:
            raise ValueError("El costo por km debe ser mayor que cero")

        self.numero_rutas = numero_rutas
        self.costo_por_km = costo_por_km

    def calcular_costo_operativo(self):
        return self.kilometraje * self.costo_por_km

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return "[TRUFI] " + info + " | Rutas: " + str(self.numero_rutas) + " | Costo por km: " + str(self.costo_por_km) + " Bs"
