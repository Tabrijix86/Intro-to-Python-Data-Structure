# 1. Take a string from the user and print
# it in the reverse order using stack data structure.
class CreateStack:
    def __init__(self):
        self.list = list()

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def size(self):
        return len(self.list)


stack = CreateStack()
s = str(input())
for i in range(len(s)):
    stack.push(s[i])
for i in range(stack.size()):
    print(stack.pop(), end="")
