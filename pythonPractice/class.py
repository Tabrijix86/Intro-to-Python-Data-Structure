# class Node:
#     a = 12
#
#
# n = Node
# n.a = 13
# print(n.a)

class Node:
    def __init__(self):
        self.a = 12
        print(f"self.a: {self.a}")
        f = 39

    def callme(self, val):
        b = val + self.a
        print(f"b: {b}")
        d = None

    e = 33


n = Node()
print(n.a)

n.b = 89
print(n.b)
print(n.callme(59))

n.e = 78
print(n.e)
