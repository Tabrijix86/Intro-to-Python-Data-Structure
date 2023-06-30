class CreateStack:
    def __init__(self):
        self.items = list()

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


def rev_word(word):
    for words in word:
        stack.push(words)
    while stack.size():
        print(stack.pop(), end=" ")


stack = CreateStack()
line = input().split()
rev_word(line)
