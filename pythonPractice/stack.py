class CreateStack:
    def __init__(self):
        self.list = list()

    def push(self, item):
        self.list.append(item)

    def size(self):
        return len(self.list)

    def pop(self):
        return self.list.pop()

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def peek(self):  # returns the top element in the stack
        if self.is_empty():
            print("Stack is empty!")
        else:
            return self.list[-1]

    def print_item(self):
        for i in range(self.size()):
            print(self.list[i], end=' ')
        print()


s = CreateStack()
s.push(10)
s.push(20)
s.push(30)
s.print_item()
print(s.size())
print(s.peek())
s.pop()
s.pop()
s.pop()
print(s.is_empty())
