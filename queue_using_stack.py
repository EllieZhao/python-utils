class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.l = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.l.append(x)

    # @return nothing
    def pop(self):
        if self.l:
            x = self.l.pop()
            return x
        else:
            return None

    # @return an integer
    def top(self):
        if self.l:
            return self.l[-1]
        else:
            return None

    def size(self):
        return len(self.l)

    def empty(self):
        return not self.l

class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.s1.push(x)

    # @return nothing
    def pop(self):
        if not self.s2.empty():
            return self.s2.pop()
        while not self.s1.empty():
            x = self.s1.pop()
            self.s2.push(x)
        return self.s2.pop()

    # @return an integer
    def peek(self):
        if not self.s2.empty():
            return self.s2.top()
        while not self.s1.empty():
            x = self.s1.pop()
            self.s2.push(x)
        return self.s2.top()

    # @return an boolean
    def empty(self):
        return self.s1.empty() and self.s2.empty()

s = Stack()
s.push(1)
s.push(2)
s.push(3)
s.push(4)
print s.top()
print s.pop()
print s.pop()

q = Queue()
q.push(1)
q.push(2)
q.push(3)
q.push(4)
q.push(5)
print q.peek()
print q.pop()
print q.pop()
