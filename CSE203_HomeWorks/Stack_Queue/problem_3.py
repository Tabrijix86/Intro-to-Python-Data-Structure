class CreateStack:
    def __init__(self):
        self.list = list()

    def push(self, item):
        self.list.append(item)

    def pop(self):
        return self.list.pop()

    def size(self):
        return len(self.list)


def largest():
    lar = stack.list[0]
    for i in range(stack.size()):
        if stack.list[i] > lar:
            lar = stack.list[i]
        else:
            continue
    print(lar)


stack = CreateStack()
stack.push(7)
stack.push(4)
stack.push(2)
stack.push(1)
stack.push(5)
largest()
