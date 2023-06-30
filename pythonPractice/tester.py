class Graph:
    def __init__(self, n, direction=False):
        self.n = n
        self.dir = direction
        self.adj = [[0 for i in range(n)] for j in range(n)]  # list comprehension

    def add_node(self):
        self.n = self.n + 1
        # initializing the new elements to 0
        for i in range(0, self.n):
            self.adj[i][self.n - 1] = 0
            self.adj[self.n - 1][i] = 0
        return self.adj[self.n - 1][self.n - 1]

    def remove_node(self, x):
        if x > self.n:
            print("Vertex not present !")
        else:
            # removing the vertex
            while x < self.n:
                # shifting the rows to left side
                for i in range(0, self.n):
                    self.adj[i][x] = self.adj[i][x + 1]
                # shifting the columns upwards
                for i in range(0, self.n):
                    self.adj[x][i] = self.adj[x + 1][i]
                x = x + 1
            # decreasing the number of vertices
            self.n = self.n - 1

    def add_edge(self, st, ed):
        self.adj[st][ed] = 1
        if not self.dir:
            self.adj[ed][st] = 1

    def remove_edge(self, st, ed):
        self.adj[st][ed] = 0
        if not self.dir:
            self.adj[ed][st] = 0

    def __repr__(self):  # for printing
        ret = '   ' + ' '.join([str(i) for i in range(len(self.adj))]) + '\n'
        ret += '   ' + ('↓ ' * len(self.adj)) + '\n'
        for i in range(len(self.adj)):
            ret += f'{i}→ ' + ' '.join([str(x) for x in self.adj[i]]) + '\n'

        return ret
