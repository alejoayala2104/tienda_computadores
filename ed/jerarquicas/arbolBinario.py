from ed.jerarquicas.nodo import NodoArbolBinario
from random import random

class ArbolBinario:
    """Clase que representa el funcionamiento de un árbol binario
    a través del uso de la clase nodo.
    """    

    def __init__(self):
        """Constructor de la clase ArbolBinario.
        Cada árbol se crea con una raíz vacía o None.
        """        

        self.raiz = None

    def adicionar(self, nueva_clave):
        """Método que añade un nuevo nodo al árbol binario.
        Se añade aleatoriamente a la izquierda o a la derecha
        de cualquier nodo que lo permita.

        :param nueva_clave: Dato o clave del nodo a añadir
        :type nueva_clave: object
        """     

        self.raiz = self.__adicionar(self.raiz, nueva_clave)

    def __adicionar(self, sub_arbol, nueva_clave):
        if sub_arbol is None:
            sub_arbol = NodoArbolBinario(nueva_clave)
        elif random() <= 0.5:#Random genera un número de 0 a 1.
            #Los menores e iguales a 0.5 -> "irse a la izq"
            nodo_izq = self.__adicionar(sub_arbol.izq, nueva_clave)
            sub_arbol.izq = nodo_izq
        else:
            #Los mayores a 0.5 -> "irse por derecha"
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
            else:
                busc_izq = self.__buscar(sub_arbol.izq, clave_buscar)
                if busc_izq is not None:#Si encontró algo
                    return busc_izq
                
                busc_der = self.__buscar(sub_arbol.der, clave_buscar)
                if busc_der is not None:
                    return busc_der
        return None

    def __len__(self):
        return self.__numero_nodos(self.raiz)

    def __numero_nodos(self, sub_arbol):
        if sub_arbol is not None:
            return (1 + 
                    self.__numero_nodos(sub_arbol.izq) + 
                    self.__numero_nodos(sub_arbol.der))
        return 0
    
    def hojas(self):
        """Método que calcula la cantidad de nodos hoja que tiene el árbol.

        :return: Cantidad de hojas del árbol.
        :rtype: int
        """  
             
        return self.__numero_hojas(self.raiz)

    def __numero_hojas(self, sub_arbol):
        if sub_arbol:
            if sub_arbol.tiene_hijos():
                return (0 + self.__numero_hojas(sub_arbol.izq)+
                        self.__numero_hojas(sub_arbol.der))
            else:
                return 1                   
        return 0
    
    def internos(self):
        """Método que calcula el total de nodos internos que tiene el árbol.

        :return: Cantidad de internos del árbol.
        :rtype: int
        """
               
        return self.__numero_internos(self.raiz)

    def __numero_internos(self, sub_arbol):
        if sub_arbol:
            if sub_arbol.tiene_hijos():
                return (1 + 
                        self.__numero_internos(sub_arbol.izq) + 
                        self.__numero_internos(sub_arbol.der))
        return 0

    def altura(self):
        """Método que calcula la altura del árbol.

        :return: Altura del árbol
        :rtype: int
        """      

        return self.__altura(self.raiz)

    def __altura(self, sub_arbol):        
        if sub_arbol is None:
            return 0
        else:
            altura = 1                
            if sub_arbol and sub_arbol.tiene_hijos():
                if sub_arbol.izq:
                    altura = max(altura, self.__altura(sub_arbol.izq))
                if sub_arbol.der:
                    altura = max(altura, self.__altura(sub_arbol.der))

                altura+=1                    
            return altura