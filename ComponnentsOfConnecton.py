
# coding: utf-8

# In[ ]:


class Not_weighted_Graph():
    """Класс невзвешенных графов. Для представления графа используется словарь множеств
       
       Атрибуты:
       :self.v: int - количество вершин в графе
       :self.graph: dict - словарь множеств с информацией о вершинах 
       
       Функции: 
       :add_edge(u, v, oriented = False): - добавляет ребро между вершинами u и v 
       :components_of_connection: int - возвращает число  компонент связности графа. Отицательных ребер не должно быть 
    
    """
    
    def __init__(self, vert):
        self.v = vert
        self.graph = {i:set() for i in range(vert)}
        
    def add_edge(self, u, v, oriented = False):
        self.graph[u-1].add(v-1)
        if oriented == False:
            self.graph[v-1].add(u-1)
    
    def components_of_connection(self):
        visited = [False]*self.v  # создаём массив посещённых вершины длины n, заполненный false изначально
        
        def dfs(u: int):
            visited[u] = True
            for v in self.graph[u]:
                if not visited[v]:
                    dfs(v)
        n_comp = 0
        for i in range(1, self.v):
            if not visited[i]:
                dfs(i)
                n_comp+=1
        return n_comp
    
    if __name__ == "__main__":
    print('Enter the amount of Vertexes and edges in the graph')
    n, m = [int(i) for i in input().split()]
    Graph = Not_weighted_Graph(n)
    for i in range(m):
        print('Enter the new Edge')
        u, v = [int(i) for i in input().split()]
        Graph.add_edge(u,v)
    print(Graph.components_of_connection())
        

