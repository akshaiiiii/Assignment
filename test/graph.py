from collections import deque
class graph:
    def __init__(self):
        self.adj_list={}
    def add_node(self,node):
        if node not in self.adj_list:
            self.adj_list[node]=[]
    def add_edge(self,src,dest,bidirection=True):
        self.add_node(src)
        self.add_node(dest)
        self.adj_list[src].append(dest)
        if bidirection:
            self.adj_list[dest].append(src)
    def display(self):
        print(self.adj_list)
def dfs(graph,node,visited=None):
    if visited==None:
        visited=set()
    visited.add(node)
    print(node,end=" ")
    for neighber in graph.adj_list[node]:
        if neighber  not in visited:
            visited.add(neighber)
            dfs(graph,neighber,visited)
def bfs(graph,start):
    visited=set()
    queue=deque([start])
    while queue:
        node=queue.popleft()
        if node not in visited:
            print(node,end=" ")
            visited.add(node)
            queue.extend(neigh for neigh in graph.adj_list[node] if neigh not in visited)


    


g=graph()
g.add_edge('A','B')
g.add_edge('A','C')
g.add_edge('B','C')
g.add_edge('B','D')
g.display()
dfs(g,'A')
print("")
bfs(g,'A')