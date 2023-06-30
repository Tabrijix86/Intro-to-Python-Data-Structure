class QueueUsingStack:
    def __init__(self):
        self.data1 = list()
        self.data2 = list()

    def push_enqueue(self, data):
        self.data1.append(data)

    def pop_dequeue(self):
        if len(self.data1) == 0 and len(self.data2) == 0:
            print("Queue is Empty")
            return
        elif len(self.data2) == 0 and len(self.data1) > 0:
            while len(self.data1):
                temp = self.data1.pop()
                self.data2.append(temp)
            return self.data2.pop()
        else:
            return self.data2.pop()


queue = QueueUsingStack()
queue.push_enqueue(10)
queue.push_enqueue(20)
queue.push_enqueue(30)
queue.push_enqueue(40)
print(queue.data1)
print(queue.pop_dequeue())
