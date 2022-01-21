class NodoArbolBinario:
    """Clase que representa un nodo de un árbol binario.
    Cada nodo tiene una referencia hacia la izquierda y la derecha,
    además de ser contenedor de un dato o clave.
    """  

    def __init__(self, clave):
        """Constructor de la clase NodoArbolBinario

        :param clave: Dato o clave del nodo a crear
        :type clave: object
        """    

        self.clave = clave
        self.izq = None #Arista izquierda
        self.der = None #Arista derecha

    def __str__(self):
        return str(self.clave)
    
    def __repr__(self):
        return str(self.clave)

    def tiene_hijos(self):
        """Método que devuelve un booleano dependiendo
        de si el nodo tiene hijos o no.

        :return: Valor que indica si el nodo tiene hijos o no
        :rtype: bool
        """        
        return self.izq is not None or self.der is not None