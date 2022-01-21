from ed.secuenciales.nodo import NodoLSE

class Pila:
    """Clase que implementa el funcionamiento de la estructura de datos
    pila, a través del uso de la clase NodoLSE
    """
    def __init__(self):
        """Constructor de la clase Pila. Crea una pila
        con su cima None por defecto        
        """

        self.cima = None

    def es_vacia(self):
        """Determina si la pila está vacía o no

        :return: Valor que compara la cima de la pila con None
        :rtype: bool
        """      

        return self.cima is None

    def cima(self):
        """Retorna el dato de la cima de la pila

        :return: Dato de la cima de la pila
        :rtype: object
        """   

        return self.cima.dato

    def apilar(self,nuevo_dato):
        """Método que adiciona un nuevo dato en la cima de la pila.
        Realiza una verificación de homogeneidad de datos cuando
        no está vacía

        :param nuevo_dato: Nuevo dato. Del mismo tipo de dato de la pila
        :type nuevo_dato: object
        :return: Valor que determina si se pudo apilar el nuevo dato o no
        :rtype: bool
        """  

        if self.es_vacia():
            self.cima = NodoLSE(nuevo_dato)
            return True
        else:
            #Validación homogeneidad de datos
            if type(self.cima.dato) is not type(nuevo_dato):
                return False

            antigua_cima = self.cima
            nueva_cima = NodoLSE(nuevo_dato)         
            nueva_cima.sig = antigua_cima
            self.cima = nueva_cima
        return True

    def desapilar(self):
        """Método que devuelve el dato de la cima y lo elimina.        

        :return: Dato de la cima de la pila
        :rtype: object
        """

        if self.es_vacia():
            return None
        else:
            antigua_cima = self.cima
            self.cima = self.cima.sig
            return antigua_cima.dato

    def __len__(self):
        """Determina cuántos elementos tiene la pila

        :return: Valor entero correspondiente al tamaño de la pila
        :rtype: int
        """  

        nodo_actual = self.cima
        ctr_len = 0
        while nodo_actual:
            nodo_actual = nodo_actual.sig
            ctr_len += 1
        return ctr_len