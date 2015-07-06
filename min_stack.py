class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.mini = None
        self.l = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.l.append(x)
        if self.mini is None:
            self.mini = x
        else:
            self.mini = min(x, self.mini)

    # @return nothing
    def pop(self):
        if self.l:
            x = self.l.pop()
            if not self.l:
                self.mini = None
            elif x == self.mini:
                self.mini = sorted(self.l)[0]
            return x
        else:
            return None

    # @return an integer
    def top(self):
        if self.l:
            return self.l[-1]
        else:
            return None

    # @return an integer
    def getMin(self):
        return self.mini

stack = MinStack()
stack.push(1)
stack.push(2)
stack.push(0)
print stack.top()
print stack.getMin()
print stack.pop()
print stack.getMin()
print stack.pop()
print stack.pop()
