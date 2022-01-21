def preorden(arbol_bin):
    """Imprime en consola el recorrido del árbol binario dispuesto en preorden.

    :param arbol_bin: Árbol binario a recorrer
    :type arbol_bin: ArbolBinario
    """    

    __preorden(arbol_bin.raiz)

def __preorden(sub_arbol):
    if sub_arbol:
        print(str(sub_arbol.clave))
        __preorden(sub_arbol.izq)
        __preorden(sub_arbol.der)

def cad_preorden(arbol_bin, sep ="^"):
    """Método que devuelve una cadena con el recorrido en 
    preorden de un árbol binario.

    :param arbol_bin: Arbol binario a recorrer
    :type arbol_bin: ArbolBinario
    :param sep: Separador, por defecto "^"
    :type sep: str, optional
    :return: Cadena con el recorrido en preorden
    :rtype: str
    """   

    cad = ""
    cad = __cad_preorden(cad, arbol_bin.raiz, sep)
    return cad

def __cad_preorden(cad, sub_arbol, sep):
    if sub_arbol:
        if cad == "":
            cad += str(sub_arbol.clave)
        else:
            cad += sep + str(sub_arbol.clave)
        cad = __cad_preorden(cad, sub_arbol.izq,sep)
        cad = __cad_preorden(cad, sub_arbol.der,sep)
    return cad

def inorden(arbol_bin):
    """Imprime en consola el recorrido del árbol binario dispuesto en inorden.

    :param arbol_bin: Árbol binario a recorrer
    :type arbol_bin: ArbolBinario
    """ 

    __inorden(arbol_bin.raiz)

def __inorden(sub_arbol):
    if sub_arbol:
        __inorden(sub_arbol.izq)
        print(str(sub_arbol.clave))
        __inorden(sub_arbol.der)

def cad_inorden(arbol_bin, sep="-"):
    """Método que devuelve una cadena con el recorrido en 
    inorden de un árbol binario.

    :param arbol_bin: Arbol binario a recorrer
    :type arbol_bin: ArbolBinario
    :param sep: Separador, por defecto "^"
    :type sep: str, optional
    :return: Cadena con el recorrido en inorden
    :rtype: str
    """ 

    cad = ""
    cad = __cad_inorden(cad, arbol_bin.raiz, sep)
    return cad

def __cad_inorden(cad, sub_arbol, sep):
    if sub_arbol:
        cad = __cad_inorden(cad, sub_arbol.izq, sep)
        if cad == "":
            cad += str(sub_arbol.clave)
        else:
            cad += sep + str(sub_arbol.clave)
        cad = __cad_inorden(cad, sub_arbol.der, sep)
    return cad
    
def postorden(arbol_bin):
    """Imprime en consola el recorrido del árbol binario dispuesto en postorden.

    :param arbol_bin: Árbol binario a recorrer
    :type arbol_bin: ArbolBinario
    """ 

    __postorden(arbol_bin.raiz)

def __postorden(sub_arbol):
    if sub_arbol:
        __postorden(sub_arbol.izq)
        __postorden(sub_arbol.der)
        print(str(sub_arbol.clave))

def cad_postorden(arbol_bin, sep="-"):
    """Método que devuelve una cadena con el recorrido en 
    postorden de un árbol binario.

    :param arbol_bin: Arbol binario a recorrer
    :type arbol_bin: ArbolBinario
    :param sep: Separador, por defecto "^"
    :type sep: str, optional
    :return: Cadena con el recorrido en postorden
    :rtype: str
    """ 

    cad = ""
    cad = __cad_postorden(cad, arbol_bin.raiz, sep)
    return cad

def __cad_postorden(cad, sub_arbol, sep):
    if sub_arbol:
        cad = __cad_postorden(cad, sub_arbol.izq,sep)
        cad = __cad_postorden(cad, sub_arbol.der,sep)
        if cad == "":
            cad += str(sub_arbol.clave)
        else:
            cad += sep + str(sub_arbol.clave)
    return cad