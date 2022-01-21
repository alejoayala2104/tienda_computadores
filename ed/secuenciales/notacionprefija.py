from ed.secuenciales.pila import Pila

class Prefija:

    def __init__(self,expresión_infija:str):
        
        self.expresión_infija = expresión_infija
        self.operadores=[Operador('^',3,4),
                        Operador('*',2,2),
                        Operador('/',2,2),
                        Operador('+',1,1),
                        Operador('-',1,1),
                        Operador(')',5,0),
                        Operador('(',0,0),                        
                        ]

    def infija(self):
        
        if self.expresión_infija == "":
            return ""
        else:
            #Se quitan los espacios a los extremos de la cadena.
            aux = self.expresión_infija.strip()
            infija = ""

            #j: elemento actual, i:indice actual
            for i, j in enumerate(aux):
                
                #Al decir aux[i+1], al llegar al final ese valor no existe,
                #entonces si se tiene que i(iterador actual) es igual al último iterador,
                #simplemente se agrega el caracter sin espacio.
                if i == len(aux)-1:
                    infija += j
                    break
                #Si el elemento actual es un dígito, agreguelo a la cadena infija
                #y verifique si el próximo caracter también es un número para no 
                #separar valores con más de un digito(ej. 1223). En caso de que el
                #siguiente caracter no sea un dígito, agregue un espacio.
                if j.isdigit():
                        infija += j
                        if aux[i+1].isdigit():
                            pass
                        else:
                            infija += ' '
                #Sino es un dígito, entonces es un espacio o un operador.
                #Solo se agrega si es un operador, y se agrega un espacio
                else:
                    if j != ' ':
                        infija += j
                        infija += ' '

            return infija

    def prefija(self):
        
        pila_oper = Pila()
        infija = self.infija()

        #Si la cadena está vacía, retornar lo mismo.
        if infija == "":
            return ""

        infija_inversa = infija[::-1]        
        prefija = ""
        
        for indice, caracter in enumerate(infija_inversa):
                      
            #Si el elemento actual es un dígito, agreguelo a la cadena infija
            #y verifique si el próximo caracter también es un número para no 
            #separar valores con más de un digito(ej. 1223). En caso de que el
            #siguiente caracter no sea un dígito, agregue un espacio.
            if caracter.isdigit():
                prefija += caracter
                #Si es el último
                if indice == len(infija_inversa)-1:
                    #Se agrega un espacio por si después del último
                    #digito se agregan operadores. En todo caso,
                    #al final de la iteración se eliminan los espacios excedentes.
                    prefija += ' '
                #Analiza si el siguiente es un dígito.
                elif infija_inversa[indice+1].isdigit():
                    pass
                else:
                    prefija += ' '
            else:
                #Si no es un dígito y tampoco es un espacio, es un operador.             
                if caracter != ' ':
                    #Compara el caracter con los operadores prestablecidos.
                    for op in self.operadores:
                        if caracter == op.operador:
                            #Si la pila de operadores está vacía,
                            #solo se agrega el operador.
                            if pila_oper.es_vacia():
                                pila_oper.apilar(op)
                            #Si el operador es ( se desapila la pila de operadores
                            #y se añaden a la expresión prefija seguidos de un espacio.
                            elif caracter == '(':
                                while not pila_oper.es_vacia() and Pila.cima(pila_oper).operador != ')':
                                    prefija += pila_oper.desapilar().operador
                                    prefija += ' '
                                #Se elimina el ( que quedó en la cima.                                
                                pila_oper.desapilar()                                
                            else:
                                #Compara la prioridad del operador de la expresión
                                #y el operador en la cima de la pila.
                                #Se añade la cima de la pila de operadores a la 
                                #expresión prefija hasta que se cumpla la condición
                                #o hasta que la pila quede vacía. Después se añade el
                                #operador con la condición validada.
                                
                                while not pila_oper.es_vacia() and not (op.prio_expr >= Pila.cima(pila_oper).prio_pila):
                                    prefija += pila_oper.desapilar().operador                                    
                                    prefija += ' '                                                                
                                pila_oper.apilar(op)  
                                
        #Si ese caracter era el último, significa que se terminó de leer
        #la expresión infija, entonces se vacía la pila de operadores
        #añadiendo dichos operadores en la expresión prefija                
        while not pila_oper.es_vacia():
            prefija += pila_oper.desapilar().operador
            prefija += ' '

        #Se eliminan espacios innecesarios a los extremos y se 
        #invierte la caedna para mostrar la verdadera expresión infija.
        pref_ordenada = prefija[::-1].strip()
        return pref_ordenada

    def eval_expr_aritm(self):
        #Si está vacía retorne 0        
        if self.prefija() == "":
            return 0
        
        resultado = 0.0
        eval_expr = 0.0        
        pref_inversa = self.prefija()[::-1]
        # print(self.prefija())
        pila_oprndos = Pila()
        aux_digito = ""
        for indice, caracter in enumerate(pref_inversa):   
            
            #Bandera para que no busque el indice+1 del último 
            ultimo = False
            if indice == len(pref_inversa)-1:
                ultimo = True
            
            if caracter.isdigit():
                if aux_digito == "": #Es decir, si tiene algo, no lo sobreescriba.
                    aux_digito = caracter
                #Se iguala aux_digito al caracter sólo en el primer dígito.
                if not ultimo and pref_inversa[indice+1].isdigit(): #Y verifica que no sea el último
                    aux_digito += pref_inversa[indice+1]
                else:
                    pila_oprndos.apilar(float(aux_digito[::-1]))                                     
                    aux_digito = ""
            else:
                if caracter != ' ':
                    try:
                        if not pila_oprndos.es_vacia():
                            op1 = pila_oprndos.desapilar()
                            op2 = pila_oprndos.desapilar()                            
                            operador = caracter                            
                            if operador == '+':
                                resultado = op1+op2
                            elif operador == '-':
                                resultado = op1-op2
                            elif operador == '*':
                                resultado = op1*op2
                            elif operador == '/':
                                resultado = op1/op2
                            elif operador == '^':
                                resultado = op1**op2
                            else:
                                return 0.0
                            pila_oprndos.apilar(resultado)
                    except:
                        print("ERROR: Valores inválidos en la expresión infija.")

        #Se desapila el último valor, el cual es el resultado.
        eval_expr = pila_oprndos.desapilar()
        return eval_expr

        


class Operador:

    def __init__(self,operador,prio_expr,prio_pila):
        self.operador = operador
        self.prio_expr = prio_expr
        self.prio_pila = prio_pila