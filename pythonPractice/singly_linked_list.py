class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
        self.size += 1

    def append_left(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def pop_left(self):
        if self.size == 0:
            print("List is empty")
        else:
            self.size -= 1
            self.head = self.head.next

    def pop(self):
        if self.size == 0:
            print("List is empty")
        else:
            self.size -= 1
            current_node = self.head
            if self.head.next is None:
                self.head = self.head.next
            else:
                while current_node.next is not None:
                    if current_node.next.next is None:
                        current_node.next = current_node.next.next
                    else:
                        current_node = current_node.next

    def delete(self, value_to_be_deleted):
        if self.size == 0:
            print("List is empty!")
        else:
            current_node = self.head
            if current_node.data == value_to_be_deleted:
                self.size -= 1
                self.head = self.head.next
            else:
                while current_node.next is not None:
                    if current_node.next.data == value_to_be_deleted:
                        self.size -= 1
                        current_node.next = current_node.next.next
                        return
                    else:
                        current_node = current_node.next

    def print_all(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def search(self, search_data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == search_data:
                return True
            current_node = current_node.next
        return False


sll = SinglyLinkedList()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.print_all()
print(sll.size)
sll.pop_left()
sll.print_all()
print(sll.search(30))
