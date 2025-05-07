# Reverse the string "yesterday" using a stack.

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

for c in "yesterday":
    st.push(c)

print(st.items)
print(st.items[1])

rev = ""

# Get the size of the string
for i in range(st.size()-1, -1, -1):
    # Get the last item, pop it, append it to a string
    rev += st.items[i]

print(rev)