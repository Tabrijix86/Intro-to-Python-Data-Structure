class CreateStack:
    def __init__(self):
        self.list = list()

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def size(self):
        return len(self.list)

    def push_stack(self, item):
        for i in range(self.size()):
            if item > self.list[i]:
                continue
            else:
                self.list.insert(self.list[i - 1], item)
                return


stack = CreateStack()
stack.push(11)
stack.push(222)
stack.push(3346)
stack.push(5342)
stack.push(6343)
stack.push_stack(44)
print(stack.list)
