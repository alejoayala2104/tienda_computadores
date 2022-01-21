class Computador:
    """Clase que representa el objeto Computador con una marca,
    una velocidad de procesador y un precio de compra.
    """    

    def __init__(self, marca="", vel_cpu="", precio=0.0):
        """Constructor de la clase Computador.

        :param marca: Marca del procesador, defaults to ""
        :type marca: str, optional
        :param vel_cpu: Velocidad del procesador, defaults to ""
        :type vel_cpu: str, optional
        :param precio: Precio de compra, defaults to 0.0
        :type precio: float, optional
        """        
        self.marca = marca
        self.vel_cpu = vel_cpu
        self.precio = precio

    def __eq__(self, otro_computador):
        if type(self) is not type(otro_computador):
            return False
        else:
            return (self.marca == otro_computador.marca) and (self.vel_cpu == otro_computador.vel_cpu)

    def __lt__(self, otro_computador):
        if(type(self) is not type(otro_computador)):
            return False
        else:
            if self.marca < otro_computador.marca:
                return True
            elif self.marca == otro_computador.marca and self.vel_cpu < otro_computador.vel_cpu:
                return True
            else:
                False

    def __str__(self):
        return "\nMarca: " + str(self.marca) + "\nVelocidad del procesador: " + str(self.vel_cpu) + "\nPrecio: " + str(self.precio) + "\n==============="