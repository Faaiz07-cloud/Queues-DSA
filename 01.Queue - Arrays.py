# Implementation of Queue using Arrays

class Queue:
    def __init__(self):
        self.data = []

    def enqueue(self, value):
        return self.data.append(value)

    def dequeue(self):
        if len(self.data) == 0:
            return f"Queue is empty"
        else:
             return f"Popped Value: {self.data.pop(0)}"

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
        self.data = []

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

queue.display()


print("")

print(queue.peek())

print(queue.dequeue())

queue.display()
print("")
print(queue.peek())

print(queue.is_empty())

print(queue.size())

# queue.clear()
# queue.display()

queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)
queue.enqueue(7)

print(queue.display_2())

print(queue.dequeue())

print("")
print(queue.display_2())

print(queue.peek())

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.enqueue(40)
queue.enqueue(50)
queue.enqueue(60)
queue.enqueue(70)

queue.display_3()
print("")
print(queue.search(20))

#-------------------------------------------------------




