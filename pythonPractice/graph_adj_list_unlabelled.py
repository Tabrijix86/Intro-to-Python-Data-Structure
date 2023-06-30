class Graph:
    def __init__(self, vertices, direction=False):
        self.v = vertices
        self.dir = direction
        # self.adj = [[] for _ in range(n)]  # list comprehension
        self.adj_list = list()
        for i in range(vertices):
            self.adj_list.append(list())

    def add_edge(self, st, ed):
        self.adj_list[st].append(ed)
        if self.dir is False:
            self.adj_list[ed].append(st)

    def remove_edge(self, st, ed):
        self.adj_list[st].remove(ed)
        if self.dir is False:
            self.adj_list[ed].remove(st)

    def in_degrees(self):
        deg = list()
        for i in range(self.v):
            count = 0
            for lst in self.adj_list:
                if i in lst:
                    count += 1
            deg.append(count)
        return deg

    def out_degrees(self):
        return [len(lst) for lst in self.adj_list]

    def __repr__(self):  # For printing the graph in a list form
        ret = str()
        for i in range(len(self.adj_list)):
            ret += f'{i} → {self.adj_list[i]}\n'
        return ret


G = Graph(5)
print(G)

G1 = Graph(5)
G1.add_edge(0, 1)  # a to b
G1.add_edge(0, 3)  # a to d
G1.add_edge(3, 1)  # d to b
G1.add_edge(1, 2)  # b to c
print(G1)

G2 = Graph(7, direction=True)
G2.add_edge(0, 1)  # a to b
G2.add_edge(0, 3)  # a to d
G2.add_edge(2, 1)  # c to b
G2.add_edge(3, 2)  # d to c
G2.add_edge(4, 2)  # e to c
G2.add_edge(5, 4)  # f to e
G2.add_edge(6, 5)  # g to f
G2.add_edge(6, 0)  # g to a
print(G2)

print(f'The in degree for G2 is: {Graph.in_degrees(G2)}')
print(f'The out degree for G2 is: {Graph.out_degrees(G2)}')
