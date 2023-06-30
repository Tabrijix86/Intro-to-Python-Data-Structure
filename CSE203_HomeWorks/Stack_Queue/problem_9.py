from collections import deque


class CreateQueue:
    def __init__(self):
        self.list = deque()

    def enqueue(self, data):
        self.list.append(data)

    def size(self):
        return len(self.list)

    def is_empty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            return self.list.popleft()

    def peek(self):
        if self.is_empty():
            print("Queue is empty!")
        else:
            return self.list[0]


def get_binary(num):
    queue.enqueue("1")
    i = 0
    while i < num:
        a = queue.dequeue()
        queue.enqueue(a + "0")
        queue.enqueue(a + "1")
        print(i + 1, a)
        i += 1


queue = CreateQueue()
binary = int(input())
get_binary(binary)
