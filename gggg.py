from collections import deque

class Queue:
    def __init__(self):
        self.elements = deque()

    def enqueue(self, data):
        self.elements.append(data)

    def dequeue(self):
        return self.elements.popleft()

    def size(self):
        return len(self.elements)

    def last_in_line(self):
        return self.elements[-1]


queue = Queue()

queue.enqueue("Person1")
queue.enqueue("Person2")
queue.enqueue("Person3")

print("Number of people in the queue: ", queue.size())
print("Last person in the queue: ", queue.last_in_line())
