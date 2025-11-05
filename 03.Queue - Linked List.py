# Implementation of Queue using Linked List

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class QueueLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def enqueue(self,data):
        node = Node(data)
        if self.head is None:
            self.head = node
        if self.tail:
            self.tail.next = node
        self.tail = node
        self.size += 1

    def dequeue(self):
        if self.head is None:
            self.tail = None
            return None
        value = self.head.data
        self.head = self.head.next
        self.size -= 1
        return value

    def display(self):
        current = self.head
        while current:
            print(current.data,'->',end=" ")
            current = current.next
        print("None")

    def peek(self):
        if self.head is None:
            print("Queue is empty!")
            return None
        else:
            return self.head.data

    def size_of_queue(self):
        return self.size

    def display_2(self):
        def print_recursive(value):
            if value is None:
                return
            print(value.data,'->', end=" ")
            print_recursive(value.next)
        if self.head is None:
            print("Queue is empty!")
            return
        print_recursive(self.head)
        print("None")


queue = QueueLinkedList()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

queue.display()

print("")

print("Peek Value -",queue.peek())

print("Popped Value -",queue.dequeue())

print("")

queue.display()

print("")

print("Peek Value -",queue.peek())

print("Size of Queue -",queue.size_of_queue())

queue.display_2()


