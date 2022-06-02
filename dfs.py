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
     o no, cuando el nodo es dirigido debe verificar que el siguiente tenga el permiso o la dirección correcta 
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

    def dfs(self, start, target, path = [], visited = set()):
        path.append(start)
        visited.add(start)
        if start == target:
            return path
        for (neighbour, weight) in self.m_adj_list[start]:
            if neighbour not in visited:
                result = self.dfs(neighbour, target, path, visited)
                if result is not None:
                    return result
        path.pop()
        return None


if __name__ == "__main__":
   
    # Crea una instancia de gráficos identificando que no está dirigido.
    g = Grafico(5, dirigido=False)
    #Pide al usuario ingresar datos
    valor0=int(input("Ingrese un número: "))
    valor1=int(input("Ingrese un número: "))
    valor2=int(input("Ingrese un número: "))
    valor3=int(input("Ingrese un número: "))
    valor4=int(input("Ingrese un número: "))
    valor5=int(input("Ingrese un número: "))
    valor6=int(input("Ingrese un número: "))
    valor7=int(input("Ingrese un número: "))
    valor8=int(input("Ingrese un número: "))
    # Agrega los atributos del gráficos con sus respectivos pesos de border.
    g.add_edge(valor0, valor1,valor1)   
    g.add_edge(valor0,valor2,valor2)
    g.add_edge(valor2,valor1,valor4)
    g.add_edge(valor1,valor4,valor6)
    g.add_edge(valor4,valor3,valor5)
    g.add_edge(valor3,valor2,valor3)
   
    # Imprime las listas adyacentes  con su respectivo nodo y peso del borde.
    g.print_adj_lista()

    traversal_path = []
    traversal_path = graph.dfs(0, 3)
    print(f" The traversal path from node 0 to node 3 is {traversal_path}")




# Execution Steps
# Current Node	Path	Visited
# 0	[0]	{0}
# 1	[0, 1]	{0, 1}
# 3	[0, 1, 3]	{0, 1, 3}