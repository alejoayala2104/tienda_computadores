from ed.secuenciales.nodo import NodoLSE

class Cola:    
    """Clase que implementa en funcionamiento de la estructura de datos
    Cola, a través del uso de la clase NodoLSE
    """

    def __init__(self):
        """Constructor de la clase Cola. Crea una cola
        con su frente None por defecto
        """

        self.frente = None

    def es_vacia(self):
        """Método que determina si la cola está vacía o no.
        """  

        return self.frente is None

    def encolar(self,nuevo_dato):
        """Método que adiciona un nuevo dato al final de la cola.
        Realiza una verificación de homogeneidad de datos cuando
        no está vacía

        :param nuevo_dato: Nuevo dato. Del mismo tipo de dato de la cola
        :type nuevo_dato: object
        :return: Valor que determina si se pudo encolar el nuevo dato o no
        :rtype: bool
        """

        if self.es_vacia():
            self.frente = NodoLSE(nuevo_dato)
            return True
        else:
            #Validación homogeneidad de datos
            if type(self.frente.dato) is not type(nuevo_dato):
                return False
            
            nodo_actual = self.frente
            while nodo_actual.sig:
                nodo_actual = nodo_actual.sig            
            nodo_actual.sig = NodoLSE(nuevo_dato)

        return True

    def desencolar(self):
        """Método que devuelve el dato del frente y lo elimina.

        :return: Dato del frente de la fila
        :rtype: object
        """

        if self.es_vacia():
            return None
        else:
            antiguo_frente = self.frente
            self.frente = self.frente.sig
            return antiguo_frente.dato

    def frente(self):
        """Devuelve el dato del frente de la cola.
        Si está vacía retorna None

        :return: Dato del frente de la cola
        :rtype: object
        """     

        return self.frente.dato

    def __len__(self):
        """Determina cuántos elementos tiene la cola

        :return: Valor entero correspondiente al tamaño de la cola
        :rtype: int
        """

        ctr_len = 0
        nodo_actual = self.frente            
        while nodo_actual:
            ctr_len += 1
            nodo_actual = nodo_actual.sig
        return ctr_len