from ed.secuenciales.nodo import NodoLSE

class NodoPrioridad(NodoLSE):
    """Clase que hereda el funcionamiento de NodoLSE y añade
    un atributo de prioridad.
    """

    def __init__(self,dato,prioridad):
        """Constructor de la clase NodoPrioridad.
        Recibe como parámetro cualquier tipo de dato
        y un entero que termina la prioridad de dicho dato

        :param dato: Dato que el nodo contiene
        :type dato: object
        :param prioridad: Número que indica la prioridad del dato
        :type prioridad: int
        """    

        NodoLSE.__init__(self,dato)
        self.prioridad = prioridad

    def __str__(self):
        """Método que retorna una cadena con la impresión del dato
        y su prioridad, según su clase lo determine.

        :return: Cadena con la información del dato
        :rtype: str
        """  

        return "Dato:" + str(self.dato) + " - Prioridad:" + str(self.prioridad)