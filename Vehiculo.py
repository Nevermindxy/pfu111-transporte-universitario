"""EMILIO WALTER GARCIA BURGOA: clase base Vehiculo."""


class Vehiculo:
    """Clase base con los atributos comunes de todo vehiculo universitario."""

    def __init__(self, codigo, marca, capacidad, kilometraje):
        self.codigo = codigo
        self.marca = marca
        self.capacidad = capacidad         
        self.kilometraje = kilometraje     

   
    @property
    def codigo(self):
        return self._codigo

    @codigo.setter
    def codigo(self, valor):
        valor = str(valor).strip()
        if not valor:
            raise ValueError("El codigo no puede estar vacio.")
        self._codigo = valor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, valor):
        valor = str(valor).strip()
        if not valor:
            raise ValueError("La marca no puede estar vacia.")
        self._marca = valor

    @property
    def capacidad(self):
        return self._capacidad

    @capacidad.setter
    def capacidad(self, valor):
        if not isinstance(valor, int) or valor < 0:
            raise ValueError("La capacidad debe ser un entero no negativo.")
        self._capacidad = valor

    @property
    def kilometraje(self):
        return self._kilometraje

    @kilometraje.setter
    def kilometraje(self, valor):
        if not isinstance(valor, (int, float)) or valor < 0:
            raise ValueError("El kilometraje no puede ser negativo.")
        self._kilometraje = float(valor)

    # ---------- Comportamientos ----------
    def mostrar_informacion(self):
        """Informacion general reutilizada por todas las clases derivadas."""
        return (f"Codigo: {self.codigo} | Marca: {self.marca} | "
                f"Capacidad: {self.capacidad} pasajeros | "
                f"Kilometraje: {self.kilometraje:.2f} km")

    def calcular_costo_operativo(self):
        """Metodo polimorfico: cada clase derivada lo sobrescribe."""
        raise NotImplementedError(
            "Las clases derivadas deben implementar calcular_costo_operativo()."
        )

    def __str__(self):
        return self.mostrar_informacion()

