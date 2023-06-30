class Graph:
    def __init__(self, vertices, direction=False):
        self.n = vertices
        self.dir = direction
        # self.adj = [[0 for i in range(n)] for j in range(n)]  # list comprehension
        self.adj_mtx = list()
        for i in range(vertices):
            self.adj_mtx.append(list())  # This helps to create list of lists
            for j in range(vertices):
                self.adj_mtx[i].append(0)

    def add_edge(self, st, ed):
        self.adj_mtx[st][ed] = 1
        if self.dir is False:
            self.adj_mtx[ed][st] = 1

    def remove_edge(self, st, ed):
        self.adj_mtx[st][ed] = 0
        if self.dir is False:
            self.adj_mtx[ed][st] = 0

    def in_degrees(self):
        deg = list()
        for i in range(self.n):
            count = 0
            for lst in self.adj_mtx:
                if lst[i]:
                    count += 1
            deg.append(count)
        return deg

    def out_degrees(self):
        return [lst.count(1) for lst in self.adj_mtx]

    def __repr__(self):  # for printing purpose
        ret = '    ' + ' '.join([str(i) for i in range(len(self.adj_mtx))]) + '\n'
        ret += '    ' + ('↓ ' * len(self.adj_mtx)) + '\n'
        for i in range(len(self.adj_mtx)):
            ret += f'{i} → ' + ' '.join([str(x) for x in self.adj_mtx[i]]) + '\n'

        return ret


G = Graph(5)
print(G)
G1 = Graph(5, True)  # example of a directed graph
G1.add_edge(0, 1)  # a to b
G1.add_edge(0, 3)  # a to d
G1.add_edge(3, 1)  # d to b
G1.add_edge(1, 2)  # b to c
print(G1)
print(f'The in degree is: {Graph.in_degrees(G1)}')
print(f'The out degree is: {Graph.out_degrees(G1)}')
