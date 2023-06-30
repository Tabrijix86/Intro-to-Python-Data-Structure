class Stack:
    def __init__(self):
        self.list = []

    def size(self):
        return len(self.list)

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def push(self, data):
        self.list.append(data)

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.list.pop()

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            return self.list[-1]

    def print_all(self):
        print(self.list)


def balance_sum(x, y):
    sum_x = 0
    temp_x = Stack()
    while x.is_empty() is not True:
        sum_x = sum_x + x.peek()
        temp_x.push(x.peek)
        x.pop()
    sum_y = 0
    temp_y = Stack()
    while y.is_empty() is not True:
        sum_y = sum_y + y.peek()
        temp_y.push(y.peek)
        y.pop()
    c = sum_y - sum_x
    while temp_x.is_empty() is not True:
        x.push(temp_x.peek())
        temp_x.pop()
    while not temp_y.is_empty():
        y.push(temp_y.peek())
        temp_y.pop()
    if c == 0:
        return "Balanced"
    else:
        x.push(c)
    x.print_all()
    y.print_all()


a = Stack()
b = Stack()
a.push(1)
a.push(5)
a.push(11)
a.push(4)
b.push(4)
b.push(32)
b.push(-1)
b.push(1)
a.print_all()
b.print_all()
balance_sum(a, b)
