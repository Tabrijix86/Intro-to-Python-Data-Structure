class CreateStack:
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def is_empty(self):
        if self.size() == 0:
            return True
        return False

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
        else:
            return self.items[-1]

    def print_data(self):
        for i in range(self.size()):
            print(self.items[i], end=' ')
        print("")


def sorted_stack():
    while stack.is_empty() is not True:
        temp = stack.peek()
        stack.pop()
        while temp_stack.is_empty() is False and int(temp_stack.peek() > int(temp)):
            stack.push(temp_stack.peek())
            temp_stack.pop()
        temp_stack.push(temp)
    return temp_stack


temp_stack = CreateStack()
stack = CreateStack()
stack.push(34)
stack.push(17)
stack.push(56)
stack.push(12)
stack.push(3)
stack.push(45)
stack.push(-1)
stack.push(110)
stack.push(55)
sorted_stack()
temp_stack.print_data()
