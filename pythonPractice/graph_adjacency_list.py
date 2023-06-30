class Graph:
    def __init__(self, direction=False):
        self.dir = direction
        self.adj_list = dict()

    def add_edge(self, st, ed):
        if self.adj_list.get(st) is None:
            self.adj_list[st] = list()
        if self.adj_list.get(ed) is None:
            self.adj_list[ed] = list()
        self.adj_list[st].append(ed)
        if self.dir is False:  # To use non-directed/directed graph
            self.adj_list[ed].append(st)

    def remove_edge(self, st, ed):
        self.adj_list[st].remove(ed)
        if self.dir is False:
            self.adj_list[ed].remove(st)

    def __repr__(self):
        ret = str()
        for key, val in self.adj_list.items():
            ret += f'{key} → [{", ".join(val)}]\n'
        return ret


# G = Graph()
# print(G)
G1 = Graph()
G1.add_edge('a', 'b')  # a to b
G1.add_edge('a', 'd')  # a to d
G1.add_edge('d', 'b')  # d to b
G1.add_edge('b', 'c')  # b to c
print(G1)
