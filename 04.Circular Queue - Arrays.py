# Circular Queue using Arrays

class CircularQueue:
    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.capacity = capacity
        self.front = -1
        self.rear = -1

    def is_full(self):
        return (self.rear + 1) % self.capacity == self.front

    def is_empty(self):
        return self.front == -1

    def enqueue(self, value):
        if self.is_full():
            print("Queue is full!")
            return
        if self.is_empty():
            self.front = 0
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = value
        print(f"Inserted {value}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty!")
            return None
        value = self.queue[self.front]
        if self.front == self.rear:
            self.front = self.rear = -1
        else:
            self.front = (self.front + 1) % self.capacity
        print(f"Removed {value}")
        return value

    def display(self):
        if self.is_empty():
            print("Queue is empty!")
            return
        i = self.front
        print("Queue elements:", end=" ")
        while True:
            print(self.queue[i], end=" ")
            if i == self.rear:
                break
            i = (i + 1) % self.capacity
        print()

cq = CircularQueue(5) # Queue Capacity - 5
cq.enqueue(1)
cq.enqueue(2)
cq.enqueue(3)
cq.enqueue(4)
cq.enqueue(5)

cq.enqueue(6) # Exceed Size

cq.display()

print(cq.is_full())
print(cq.is_empty())

cq.dequeue()

cq.display()
print(cq.is_full())

cq.enqueue(6)
cq.display()
