
# coding: utf-8

# In[ ]:


class Weighted_Graph():
    """Класс взвешенных графов. Для представления графа используется список ребер
       
       Атрибуты:
       :self.v: int - количество вершин
       :self.graph: list - список ребер 
       
       Функции: 
       :add_edge(u,v,w): добавляет ребро весом w между вершинами u и v
       :ford_bellman_algo(s = 0): list - возвращает минимальные расстояния от вершины s до остальных вершиню при наличии
       ребер отрицательного веса - возвращает х
       :list_to_dict(Oriented = False): - меняет представление графа из списка ребер в словарь словарей 
       :components_of_connection: int - возвращает колличество компонент связанности, работает только с представлением 
       графа в виде словаря словарей
       """
    def __init__(self, vert):
        
        self.v = vert
        self.graph = []
    
    def add_edge(self, u, v, w=1):
        
        self.graph.append((u-1, v-1, w))
        
    def ford_bellman_algo(self, s = 0):
        
        m = len(self.graph)
        
        d = [None]*self.v #заводим массив для записи результатов
        d[s] = 0 #путь до стартовой вершины равен 0
        b = float('inf') 
        
        for i in range(self.v - 1): 
            for u, v, w in self.graph: 
                if d[u] is not None: 
                    d[v] = min(b if d[v] is None else d[v], d[u] + w) # релаксация

        graph = list(d) 

        #проверка на ребра отрицательного веса 
        for u, v, w in self.graph: #проводим еще одну фазу
            #print('--->', u,v,w)
            if d[u] is not None: 
                d[v] = min(b if d[v] is None else d[v], d[u] + w) 

        #сравниваем, поменялись ли стоимости путей 
        for i in range(self.v): 
            if d[i] != graph[i] or d[i] == None:
                d[i] = 'x'  
                
        return d
    
    def list_to_dict(self, Oriented = False):
        graph = {i:{} for i in range(self.v)}
        for u, v, w in self.graph:
            graph[u].update({v: w})
            if not Oriented:
                graph[v].update({u: w})
        self.graph = graph
        
    def components_of_connection(self):
        visited = [False]*self.v  # создаём массив посещённых вершины длины n, заполненный false изначально
        
        def dfs(u: int):
            visited[u] = True
            for v in self.graph[u].keys():
                if not visited[v]:
                    dfs(v)
        n_comp = 0
        for i in range(1, self.v):
            if not visited[i]:
                dfs(i)
                n_comp+=1
        return n_comp

    if __name__ == "__main__":
        string = input('Enter the string ')
        pattern = input('Enter the substring ')
        print(' '.join(map(str, FindSubString(string, pattern))))
