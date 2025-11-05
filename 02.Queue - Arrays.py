# Implementation of Queue using Arrays - Collection Module

from collections import deque

class Queue:
    def __init__(self):
        self.data = deque() # Double-Ended Queue - allows to add or remove data from both ends

    def enqueue(self, value):
        return self.data.append(value) # append at right

    def enqueue_2(self, value):
        return self.data.appendleft(value)  # append at right

    def dequeue(self):
        if len(self.data) == 0:
            return f"Queue is empty"
        else:
             return f"Popped Value: {self.data.pop()}"

    def dequeue_2(self):
        if len(self.data) == 0:
            return f"Queue is empty"
        else:
             return f"Popped Value: {self.data.popleft()}"

    def display(self):
        if len(self.data) == 0:
            print("Queue is empty")
        else:
            for i in range(len(self.data)):
              print(self.data[i], end=" ")

    def peek(self):
        if len(self.data) == 0:
            return f"Queue is empty"
        else:
            return f"Peek Value: {self.data[0]}"

    def is_empty(self):
        if len(self.data) == 0:
            return "Queue is empty"
        else:
            return "Queue is not empty"

    def size(self):
        if len(self.data) == 0:
            return "Queue is empty"
        else:
            return f"Size of Queue is: {len(self.data)}"

    def clear(self):
        self.data = deque()

    def display_2(self):
        if len(self.data) == 0:
            return "Queue is empty"
        else:
            return f" | ".join(map(str, self.data))

    def display_3(self):
        def print_recursive(values, i=0):
            if i == len(values):
                return
            print(values[i], end=" ")
            print_recursive(values, i+1)
        if len(self.data) == 0:
            print("Queue is empty")
        else:
            print_recursive(self.data)

    def search(self, value):
        if len(self.data) == 0:
            return "Queue is empty"
        if value in self.data:
            index = self.data.index(value)
            return f"Value {value} found in Queue at index {index}"
        else:
            return f"Value {value} not found in Queue"

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)

# queue.display()

queue.enqueue_2(0)
queue.enqueue_2(0)

print("")

queue.display()

print(queue.dequeue())

print("")

queue.display()

print(queue.dequeue_2())

print("")

queue.display()

print("")

print(queue.data[0])






