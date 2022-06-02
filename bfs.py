'''En el presente codigo permite obtener el recorrido y el orden de los nodos del grafo,
mediante los vertices asignados en cada nodo, recordando que solo puede ser visitado una vez cada nodo
 indicando si el nodo es dirigido o no, cuando son dirigidos debe seguir su direcciín indicada'''

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
        '''Para agregar un diccionario tenemos como parametro crear un objeto por lista agregando
        un bucle de recorrido que empieza de nodo=0 hasta el rango asignado'''
        self.m_adj_lista = {nodo: set() for nodo in self.m_nodos}      
   
    # Se agrega un constructor instanciado declarando como atributo dos nodos y el peso.
    '''Permite agregar los dos y el peso de los bordes para cada nodo, verificando si el nodo es dirigido 
     o no, cuando el nodo es dirigido debe veridicar que el siguiente tenga el permiso o la dirección correcta 
     para continuar al siguiente nodo, cuando no es dirigido puede ir por cualquier dirección'''
    def add_edge(self, nodo1, nodo2, weight=1):
        #Si el nodo1 es dirigido agrega un vertice del nodo1 al nodo2
        self.m_adj_lista[nodo1].add((nodo2, weight))
        # Cuando el nodo no está dirigido.
        if not self.m_dirigido:
            #Si el nodo2 no es dirigido agrega un vertice del nodo2 al nodo1
         self.m_adj_lista[nodo2].add((nodo1, weight))
    ''' Para imprimir la lsita de los nodos y su peso de borde se debe agregar la instancia como atributo, 
    agregar un bucle de recorrido que permita imprimir el posicion del nodo, con los respectivos datos 
    almacenados en el diccionario de la lista adyacente imprimiendo en el orden del primer nodo'''
    # Imprime la representación gráfica del atributo.
    def print_adj_lista(self):
        #Realiza un sentencia identificando el número de llaves que están conectadas al nodo.
        for llave in self.m_adj_lista.keys():
            #Imprime en orden el número de nodos ingresados con los datos almacenados en el diccionaro
            print("nodo", llave, ": ", self.m_adj_lista[llave])
 
    #En el constrructor se agrega los atributos de la instancia y el nodo inicial.
    def bfs_traversal(self, iniciar_nodo):
        #el atributo visitado almacena en una lista los nodos recorridos sin ser repetidos
        visitado = set()
        #Almacena los datos despues de ser visitados    2
        queue = Queue()
 
        # Mediante la lista de visitados y la cola se procede a añadir el nodo.
        queue.put(iniciar_nodo)
        visitado.add(iniciar_nodo)
 
        #Mientras no tenga colas vacías.
        while not queue.empty():
            # Puede desencolar los vértices.
            actual_nodo = queue.get()
            #Imprime el nodo actual y el final.
            print(actual_nodo, end = " ")
            #Obtiene todos los vértices adyacentes de los nodos, agregando un conector a cada nodo.
            for (siguiente_nodo, weight) in self.m_adj_lista[actual_nodo]:
                #Verifica que el siguiente nodo no ha sido visitado.
                if siguiente_nodo not in visitado:
                    #Procede a ponerlo dentro de una cola.
                    queue.put(siguiente_nodo)
                    #Agrega los datos del siguiente módulo visitado.
                    visitado.add(siguiente_nodo)
 
 
if __name__ == "__main__":
   
    # Crea una instancia de gráficos identificando que no está dirigido.
    g = Grafico(8, dirigido=True)
    #Pide al usuario ingresar datos
    valor1=int(input("Ingrese un número: "))
    valor2=int(input("Ingrese un número: "))
    valor3=int(input("Ingrese un número: "))
    valor4=int(input("Ingrese un número: "))
    valor5=int(input("Ingrese un número: "))
    valor6=int(input("Ingrese un número: "))
    valor7=int(input("Ingrese un número: "))
    valor8=int(input("Ingrese un número: "))
    # Agrega los atributos del gráficos con sus respectivos pesos de border.
    g.add_edge(valor1, valor2,valor5)
    g.add_edge(valor1,valor3,valor6)
    g.add_edge(valor2,valor5,valor1)
    g.add_edge(valor3,valor5,valor7)
    g.add_edge(valor5,valor1,valor8)
    g.add_edge(valor5,valor3,valor1)
    g.add_edge(valor3,valor4,valor5)
    g.add_edge(valor4,valor7,valor1)
    g.add_edge(valor7,valor8,valor4)
    g.add_edge(valor8,valor3,valor2)
    g.add_edge(valor3, valor7,valor8)
 
    # Imprime las listas adyacentes  con su respectivo nodo y peso del borde.
    g.print_adj_lista()
    #Imprime el recorrido de la anchura que tiene el nodo.
    print ("El siguiente es el primer recorrido de anchura"
                    " (A partir del vértice 0)")
    #Indica el número de búsqueda de anchura.
    g.bfs_traversal(0)
    print()