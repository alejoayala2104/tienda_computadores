from ed.secuenciales.nodoprioridad import NodoPrioridad

class ColaDePrioridad:    
    """Clase que implementa el funcionamiento del TAD
    Cola de Prioridad, utilizando un nodo especial del tipo
    NodoPrioridad. Serán atentidos primeramente, o tienen
    MAYOR prioridad los nodos que poseen, por el contrario
    un número menor de prioridad.
    """

    def __init__(self):
        """Constructor de la clase ColaDePrioridad.
        Crea una cola de prioridad con su frente None por defecto
        """

        self.frente = None

    def es_vacia(self):
        """Método que determina si la cola de prioridad está vacía o no.
        """

        return self.frente is None

    def encolar(self,nuevo_dato,prioridad):
        """Método que adiciona un nuevo dato al final de la cola de prioridad
        y la reordena según prioridad de entrada (a través
        del ordenamiento burbuja).
        Realiza una verificación de homogeneidad de datos cuando
        no está vacía.

        :param nuevo_dato: Nuevo dato. Del mismo tipo de dato de la cola
        :type nuevo_dato: object
        :return: Valor que determina si se pudo encolar el nuevo dato o no
        :rtype: bool
        """

        #Primero se agrega el elemento como si fuese una cola normal.
        if prioridad < 1:
            print("La prioridad del dato debe ser mayor o igual a 1")
            return False

        if self.es_vacia():
            self.frente = NodoPrioridad(nuevo_dato,prioridad)
            return True
        else:
            #Validación homogeneidad de datos
            if type(self.frente.dato) is not type(nuevo_dato):
                return False
            
            nodo_actual = self.frente
            while nodo_actual.sig:
                nodo_actual = nodo_actual.sig            
            nodo_actual.sig = NodoPrioridad(nuevo_dato,prioridad)
        
        #Después se reordena la cola como una cola de prioridad,
        #a través del algoritmo de ordenamiento burbuja.      
        cola_ordenada = False
        nodo_actual = self.frente
        nodo_anterior = nodo_actual            
        while not cola_ordenada: #Mientras la cola no esté ordenada                              
            cola_ordenada = True
            nodo_actual = self.frente
            nodo_anterior = nodo_actual                             
            #Recorrer la lista
            while nodo_actual.sig:                                 
                nodo_siguiente = nodo_actual.sig
                #Si la prioridad actual es mayor a la del siguiente,
                #intercambie los nodos de posición.
                if nodo_actual.prioridad > nodo_actual.sig.prioridad:                         
                    cola_ordenada = False                       
                    nodo_actual.sig = nodo_siguiente.sig
                    nodo_siguiente.sig = nodo_actual  

                    if nodo_actual is self.frente:
                        self.frente = nodo_siguiente
                    else:
                        nodo_anterior.sig = nodo_siguiente

                    #Se guarda el nodo_anterior para la siguiente iteración
                    nodo_anterior = nodo_siguiente                        
                else:
                    nodo_anterior = nodo_actual
                    nodo_actual = nodo_actual.sig

        return True

    def desencolar(self):
        """Método que devuelve el dato del frente de la
        cola de prioridad y elimina el nodo correspondiente.

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
        """Devuelve el dato del frente de la cola de prioridad.
        Si está vacía retorna None

        :return: Dato del frente de la cola
        :rtype: object
        """

        return self.frente.dato

    def __len__(self):
        """Determina cuántos elementos tiene la cola de prioridad.

        :return: Valor entero correspondiente al tamaño de la cola
        :rtype: int
        """

        ctr_len = 0
        nodo_actual = self.frente            
        while nodo_actual:
            ctr_len += 1
            nodo_actual = nodo_actual.sig
        return ctr_len

    def __str__(self):
        """Método que devuelve una cadena con la información de la
        cola de prioridad en un formato determinado.

        :return: Cadena con los datos de la cola de prioridad
        :rtype: str
        """       

        if self.es_vacia():
            return ""               
        prioridad = self.frente.prioridad        
        cadena = "|#%i|:" % prioridad
        nodo_actual = self.frente
        while nodo_actual:
            if prioridad != nodo_actual.prioridad:
                prioridad = nodo_actual.prioridad
                cadena += "|#%i|:" % prioridad
            cadena += str(nodo_actual.dato)
            if nodo_actual.sig and prioridad == nodo_actual.sig.prioridad:
                cadena += "->"
            nodo_actual = nodo_actual.sig
        return cadena