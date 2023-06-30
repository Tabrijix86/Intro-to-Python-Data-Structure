class CreateStack:
    def __init__(self):
        self.list = list()

    def push(self, item):
        self.list.append(item)

    def size(self):
        return len(self.list)

    def pop(self):
        return self.list.pop()


def is_balanced(parenthesis):
    for i in parenthesis:
        if i in open_brk:
            stack.push(i)
        elif i in close_brk:
            position = close_brk.index(i)
            if (stack.size() > 0) and (open_brk[position] == stack.list[stack.size() - 1]):
                stack.pop()
            else:
                return False
    if stack.size() == 0:
        return True
    else:
        return False


stack = CreateStack()
open_brk = ['[', '{', '(']
close_brk = [']', '}', ')']
inp = str(input())
print(is_balanced(inp))
