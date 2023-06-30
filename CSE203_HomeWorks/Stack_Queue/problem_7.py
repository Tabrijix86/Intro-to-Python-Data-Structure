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

    def peek(self):  # returns the head data of the queue
        if self.is_empty():
            print("Queue is empty!")
        else:
            return self.list[0]


def reverse_queue_first_k_elements(until):
    if queue.size() == 0 or until > queue.size():
        return
    li = list()
    for i in range(until):
        li.append(queue.list[0])
        queue.dequeue()
    while len(li) != 0:
        queue.enqueue(li[-1])
        li.pop()


queue = CreateQueue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
# queue.enqueue(70)
# queue.enqueue(80)
# queue.enqueue(90)
k = int(input())
reverse_queue_first_k_elements(k)
print(queue.list)
