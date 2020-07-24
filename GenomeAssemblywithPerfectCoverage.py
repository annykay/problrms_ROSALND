
# coding: utf-8

# In[ ]:


class DeBruijnGraph():
    """To describe and operate with de Bruijn graph. Structure - dictionary of sets
    
       Atributes:
       :self.v: int - the number of vertexes
       :self.len_words: int - lenth of words
       :self.graph:dict - to describe edges
       
       Functions:
       :add_edge(word): - add an edge
       :find_cycle(dict:graph): list - a cycle, found in the graph
       :remove_cycle: - delete cycle from graph
       :euler_cycle: - make a cucle for all vertexes
       """
    
    def __init__(self, n,vert ):
        self.v = vert
        self.len_words = n
        self.graph = {}
        
    def add_edge(self, word):
        """Function adds an edge in the graph
           :word: str - a word to add to graph
        """
        
        u = word[:-1]
        v = word[1:]
        if u in self.graph.keys():
            self.graph[u].add(v)
        else:
            self.graph.update({u:set()})
            self.graph[u].add(v)
     

    def find_cycle(self, graph):
        """Function to find a cycle, including the first vertex in the graph
           :graph: dict - where to search
           """
        
        color = {i:'white' for i in graph.keys()}
        cycle = []
        def dfs(ver):
            color[ver] = 'grey'
            #cycle.append(ver)
            for v in graph[ver]:
                if color[v] == 'white':
                    cycle.append(v)
                    dfs(v)
                if color[v]=='grey':
                    #cycle.append(v)
                    return cycle
            color[ver] = 'black'
       
        
        for i in graph.keys():
            if not cycle:
                dfs(i)
            if cycle:
                cycle.append(i)
            break
            
        return cycle
    
    def remove_cyсle(self, cycle, graph):
        """function to remove cycle from graph
           :cycle: list - cycle to remove
           :graph: dict - graph to remove cycle from
           """
        
        for i in range(len(cycle)-1):
            if cycle[i+1] in graph[cycle[i]]:
                graph[cycle[i]].remove(cycle[i+1])
            else:
                return
        graph[cycle[-1]].remove(cycle[0])
        return graph
        
    def euler_cycle(self):
        """Function to find euler cycle"""
        cycles = []
        graph = self.graph
        cycle = self.find_cycle(graph)
        while cycle:
            cycles.extend(cycle)
            
            graph = self.remove_cyсle(cycle, graph)
            cycle = self.find_cycle(graph) 
        return cycles

