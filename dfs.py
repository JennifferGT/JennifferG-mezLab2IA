from queue import Queue
#Crea una función llamada gráfico.
class Grafico:
    #Crea objetos instanciando los atributos.
    def __init__(self, numero_de_nodos, dirigido=True):
        #Ingresa por medio de atributos el número de nodos.
        self.m_numero_de_nodos = numero_de_nodos
        #Ingresa el número de nodos mediante el rango usando el atributo numero de nodos.
        self.m_nodos = range(self.m_numero_de_nodos)
        # Instancia el atributo dirigido.
        self.m_dirigido = dirigido
       
        #Se implementa una lista adyacente mediante un diccionario.
    
        '''Para agregar un diccionario tenemos como parámetro crear un objeto por lista agregando
        un bucle de recorrido que empieza de nodo=0 hasta el rango asignado'''
        self.m_adj_lista = {nodo: set() for nodo in self.m_nodos}      
   
    # Se agrega un constructor instanciado declarando como atributo dos nodos y el peso.
    '''Permite agregar los dos nodos y el peso de los bordes para cada nodo, verificando si el nodo es dirigido 
     o no, cuando el nodo es dirigido debe verificar que el siguiente nodo tenga el permiso o la dirección correcta 
     para continuar al siguiente nodo, cuando no es dirigido puede ir por cualquier dirección'''
    def add_edge(self, nodo1, nodo2, weight=1):
        #Si el nodo1 es dirigido agrega un vertice del nodo1 al nodo2
        self.m_adj_lista[nodo1].add((nodo2, weight))
        # Cuando el nodo no está dirigido.
        if not self.m_dirigido:
            #Si el nodo2 no es dirigido agrega un vertice del nodo2 al nodo1
         self.m_adj_lista[nodo2].add((nodo1, weight))
    
    ''' Para imprimir la lista de los nodos y su peso de borde se debe agregar la instancia como atributo, 
    agregar un bucle de recorrido que permita imprimir el posicion del nodo, con los respectivos datos 
    almacenados en el diccionario de la lista adyacente imprimiendo en el orden del primer nodo'''
    # Imprime la representación gráfica del atributo.
    def print_adj_lista(self):
        #Realiza un sentencia identificando el número de llaves que están conectadas al nodo.
        for llave in self.m_adj_lista.keys():
            #Imprime en orden el número de nodos ingresados con los datos almacenados en el diccionaro
            print("nodo", llave, ": ", self.m_adj_lista[llave])
            '''Dentro del constructor de dfs se implementan 5 atributos,
            la instancia, incio, objetivo, trayecto y visitado '''
    #Dentro del constructor dfs 
    def dfs(self, inicio, objetivo, trayecto = [], visitado = set()):
        #En el trayecto adjunta los nodos de inicio
        trayecto.append(inicio)
        #En cada nodo de inicio visitado lo va agregando
        visitado.add(inicio)
        #Dentro de la condición if pregunta si el nodo de inicio es igual al nodo de los  objetivos
        if inicio == objetivo:
            #Si son iguales termina el trayecto
            return trayecto
        '''Realiza  una sentencia de recorrido mediante los nodos vecinos y el peso de la aristas
        hasta el primer número de listas adyacentes'''
        for (vecino, weight) in self.m_adj_lista[inicio]:
            #Cuando los vicinos aun no son visitados
            if vecino not in visitado:
                #Crea un atributo especificando los parametros, llamando al constructor
                '''El constructor es el encargado de preguntar si fue visitado o no, permite adjuntar y agregarlo como nodo de inicio'''
                result = self.dfs(vecino, objetivo, trayecto, visitado)
                #Verfica si el resultado  es ninguno termina el trayecto
                if result is not None:
                    return result
        trayecto.pop()
        #Terminado el recorrido
        return None


if __name__ == "__main__":
   
    # Crea una instancia de gráficos identificando que no está dirigido.
    g = Grafico(7, dirigido=True)
    #Pide al usuario ingresar datos
    
    valor1=int(input("Ingrese un número: "))
    valor2=int(input("Ingrese un número: "))
    valor3=int(input("Ingrese un número: "))
    valor4=int(input("Ingrese un número: "))
    valor5=int(input("Ingrese un número: "))
    valor6=int(input("Ingrese un número: "))
    valor7=int(input("Ingrese un número: "))
    
    # Agrega los atributos del gráficos con sus respectivos pesos de border.
    g.add_edge(valor5, valor1)   
    g.add_edge(valor5, valor4)
    g.add_edge(valor2, valor5)
    g.add_edge(valor4, valor2)
    g.add_edge(valor4, valor3)
    g.add_edge(valor3, valor6)
    g.add_edge(valor6, valor5)
    g.add_edge(valor5, valor7)
    
    
    # Imprime las listas adyacentes  con su respectivo nodo y peso del borde.
    g.print_adj_lista()
    #Crea un atributo que almacena el recorrido de la ruta dentro de un diccionario
    recorrido_ruta = []
    #Agrega el nodo inicial y el nodo objetivo
    recorrido_ruta = g.dfs(4,7)
    print(f" El camino recorrido del nodo 4 al nodo 7 es {recorrido_ruta}")

