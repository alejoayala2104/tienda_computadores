from ed.jerarquicas.nodo import NodoArbolBinario
from ed.jerarquicas.arbolBinario import ArbolBinario

class ArbolBinarioBusqueda(ArbolBinario):
    """Clase que representa el funcionamiento de un árbol binario de búsqueda.
    Hereda de la clase ArbolBinario.

    :param ArbolBinario: Herencia de la clase ArbolBinario
    :type ArbolBinario: ArbolBinario
    """    

    def __init__(self):
        """Constructor de la clase ArbolBinarioBusqueda.
        Cada árbol se crea con una raíz vacía o None.
        Hereda el constructor de la clase ArbolBinario.
        """ 

        ArbolBinario.__init__(self)
        self.raiz = None

    def adicionar(self, nueva_clave): 
        """Método que añade un nodo con una nueva clave al árbol.
        Se añade el nodo dependiendo de si su clave es mayor o menor
        al nodo en análisis. No acepta una clave duplicada.

        :param nueva_clave: Dato o clave del nodo a añadir
        :type nueva_clave: object
        """  

        self.raiz = self.__adicionar(self.raiz, nueva_clave)

    def __adicionar(self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = NodoArbolBinario(nueva_clave)  
        elif sub_arbol.clave > nueva_clave:#Intento de adición por izq
            sub_arbol.izq = self.__adicionar(sub_arbol.izq, nueva_clave)
        elif sub_arbol.clave < nueva_clave:#Intento de adición por der
            sub_arbol.der = self.__adicionar(sub_arbol.der, nueva_clave)        
        return sub_arbol
    
    def buscar(self, clave_buscar): 
        """Método que busca por un nodo que contenga la clave ingresada.
        Si lo encuentra, se retorna la clave encontrada. Si no,
        retorna None.

        :param clave_buscar: Dato o clave a buscar
        :type clave_buscar: object
        :return: Clave encontrada, por defecto None
        :rtype: object
        """      

        return self.__buscar(self.raiz, clave_buscar)

    def __buscar(self, sub_arbol, clave_buscar):
        if sub_arbol is not None:
            if sub_arbol.clave == clave_buscar:
                return sub_arbol.clave
            #Intento de búsqueda por la Izq
            elif clave_buscar < sub_arbol.clave:
                return self.__buscar(sub_arbol.izq, clave_buscar)
            else: #Intento de búsqueda por Der
                return self.__buscar(sub_arbol.der, clave_buscar)
        return None

    def buscar_minimo(self):
        """Método que retorna la clave con el valor mínimo respecto a todo el árbol.

        :return: Valor minimo del árbol
        :rtype: object
        """        

        return self.__minimo(self.raiz)

    def __minimo(self, sub_arbol):
        if sub_arbol:
            if sub_arbol.izq:
                return self.__minimo(sub_arbol.izq)
            else:
                return sub_arbol.clave
        return None

    def buscar_maximo(self):
        """Método que retorna la clave con el valor máximo respecto a todo el árbol.

        :return: Valor máximo del árbol
        :rtype: object
        """    

        return self.__maximo(self.raiz)

    def __maximo(self, sub_arbol):
        if sub_arbol:
            if sub_arbol.der:
                return self.__maximo(sub_arbol.der)
            else:
                return sub_arbol.clave
        return None

    def borrar(self, clave_borrar):
        """Método que elimina el nodo con la clave ingresada como parámetro.
        En caso de no encontrar un nodo con dicha clave, retorna None.

        :param clave_borrar: Dato o clave del nodo a borrar
        :type clave_borrar: object
        """        

        self.raiz = self.__borrar(self.raiz,clave_borrar)            
      

    def __buscarPadreNodo(self, sub_arbol, clave_buscar):
        """Retorna el padre del nodo a buscar.
        Si no encuentra un nodo con la clave a buscar, retorna None

        :param sub_arbol: Raíz del sub árbol a buscar
        :type sub_arbol: NodoArbolBinario
        :param clave_buscar: Dato o clave a buscar
        :type clave_buscar: object
        :return: Padre del nodo encontrado
        :rtype: NodoArbolBinario
        """

        padre_nodo = None #Variable temporal a retornar

        if sub_arbol is None: #Si el árbol está vacío, retorna None.
            return None
        
        #Verifica si tiene hijo izq
        if sub_arbol.izq:
            #Verifica si ese hijo tiene la clave buscada
            if sub_arbol.izq.clave == clave_buscar:
                return sub_arbol #Retorna el padre de izq que contiene la clave buscada

        #Verifica si tiene hijo der
        if sub_arbol.der:
            #Verifica si ese hijo tiene la clave buscada
            if sub_arbol.der.clave == clave_buscar:
                return sub_arbol #Retorna el padre de der que contiene la clave buscada

        #Si los hijos inmediatos de sub_arbol no tienen la clave buscada,
        #se procede a buscar recursivamente en los demás nodos.

        #Si el dato a buscar es menor al del sub_arbol,
        #se busca por el lado izquierdo (verificando antes su existencia)
        if sub_arbol.izq and clave_buscar < sub_arbol.clave:
            padre_nodo = self.__buscarPadreNodo(sub_arbol.izq, clave_buscar)

        #Si el dato a buscar es mayor al del sub_arbol,
        #se busca por el lado derecho (verificando antes su existencia)
        if sub_arbol.der and clave_buscar > sub_arbol.clave:
            padre_nodo = self.__buscarPadreNodo(sub_arbol.der, clave_buscar)

        return padre_nodo


    def __borrar(self, sub_arbol, clave_borrar):
        if sub_arbol:
            if sub_arbol.clave == clave_borrar:#Si lo encontró, sub_arbol es el nodo a borrar
                #Si no tiene hijos
                if not sub_arbol.tiene_hijos():  
                    sub_arbol = None #Borro el nodo retornando None
                    return sub_arbol
                #Si tiene hijo izq y no tiene hijo der
                elif sub_arbol.izq and sub_arbol.der is None:                    
                    return sub_arbol.izq
                #Si tiene hijo der y no tiene hijo izq
                elif sub_arbol.der and sub_arbol.izq is None:                    
                    return sub_arbol.der
                else: #Si tiene dos hijos

                    #Cambia la clave del nodo a borrar
                    #con el menor de los mayores, es decir,
                    #el dato hacia la extrema izquierda del nodo
                    #derecho (nodo mínimo de esa rama).
                    clave_minimo = self.__minimo(sub_arbol.der)
                    sub_arbol.clave = clave_minimo

                    #Se elimina dicho nodo mínimo.
                    sub_arbol.der = self.__borrar(sub_arbol.der, clave_minimo)
                             
            elif clave_borrar < sub_arbol.clave: #Intento de búsqueda por la Izq
                sub_arbol.izq = self.__borrar(sub_arbol.izq, clave_borrar)
            else:                                #Intento de búsqueda por Der
                sub_arbol.der = self.__borrar(sub_arbol.der, clave_borrar)
        return sub_arbol #Si sub_arbol es None, se retorna None