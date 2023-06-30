from collections import deque


class CreateQueue:
    def __init__(self):
        self.list = deque()  # Deque (Doubly Ended Queue) in Python can be
        # implemented using the module 'collections'. Deque is preferred over
        # a list in the cases where we need quicker append and pop operations
        # from both the ends of the container, as deque provides an O(1) time
        # complexity for append and pop operations as compared to a list
        # that provides O(n) time complexity.

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
            return self.list.popleft()  # popleft() function is used to delete
            # an argument from the left end of the deque.

    def peek(self):  # returns the head data of the queue
        if self.is_empty():
            print("Queue is empty!")
        else:
            return self.list[0]


queue = CreateQueue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.list)
print("After dequeue: ")
queue.dequeue()
print(queue.list)
print(queue.peek())
