# 2. Use a stack to create a new list with the items in the following list reversed: [1, 2, 3, 4, 5].

class Stack():
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

st = Stack()
list = []
l2 = []

for i in range(1, 6, 1):
    st.push(i)

print(st.items)

for i in range(st.size()-1, -1, -1):
    list.append(st.items[i])

print(list)

for i in range(st.size()):
    l2.append(st.pop())

print(l2)