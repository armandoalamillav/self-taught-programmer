class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

qu = Queue()

print(qu.is_empty())

qu.enqueue(1)
print(qu.is_empty())

print(qu.items)

q1 = Queue()

for i in range(5):
    q1.enqueue(i)

print(q1.items)
print(q1.size())

for i in range(5):
    q1.dequeue()

print(q1.items)
print(q1.size())