class Queue:
    def __init__(self):
        self.l = []

    def push(self, x):
        self.l.append(x)

    def pop(self):
        return self.l.pop(0)

    def peek(self):
        if self.l:
            return self.l[0]

    def size(self):
        return len(self.l)

    def empty(self):
        return not self.l

class Stack:
    # initialize your data structure here.
    def __init__(self):
        self.q1 = Queue()       
        self.q2 = Queue()       

    # @param x, an integer
    # @return nothing
    def push(self, x):
        if self.q2.empty():
            self.q1.push(x)
        else:
            self.q2.push(x)

    # @return nothing
    def pop(self):
        if self.q1.empty() and self.q2.empty():
            return None
        while self.q1.size() > 1:
            x = self.q1.pop()
            self.q2.push(x)
        if self.q1.size() == 1:
            return self.q1.pop()
        while self.q2.size() > 1:
            x = self.q2.pop()
            self.q1.push(x)
        if self.q2.size() == 1:
            return self.q2.pop()

    # @return an integer
    def top(self):
        if self.q1.empty() and self.q2.empty():
            return None
        while self.q1.size() > 1:
            x = self.q1.pop()
            self.q2.push(x)
        if self.q1.size() == 1:
            x = self.q1.pop()
            self.q2.push(x)
            return x
        while self.q2.size() > 1:
            x = self.q2.pop()
            self.q1.push(x)
        if self.q2.size() == 1:
            x = self.q2.pop()
            self.q1.push(x)
            return x

    # @return an boolean
    def empty(self):
        return self.q1.empty() and self.q2.empty()

q = Stack()
q.push(1)
q.push(2)
q.push(3)
print q.top()
print q.pop()
print q.pop()
print q.pop()


