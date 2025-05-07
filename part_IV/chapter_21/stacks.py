class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self, item):
        return self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        last = len(self.items)-1
        return self.items[last]
    
    def size(self):
        return len(self.items)

stack = Stack()

print(stack.is_empty())

stack.push(1)

print(stack.is_empty())

new_s = Stack()

for c in "Hello":
    new_s.push(c)

print(new_s.items)

rev = ""

for i in range(0, len(new_s.items)):
    rev += new_s.pop()

print(rev)