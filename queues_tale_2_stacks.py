class MyQueue(object):
    def __init__(self):
        self.s1 = []
        self.s2 = []
        
    def empty(self):
        n = len(self.s1)
        for i in range(len(self.s1)):
            self.s2.append(self.s1[n-i-1])
        self.s1 = []
    
    def peek(self):
        if self.s2 == []:
            self.empty()
        return self.s2[-1]
        
    def pop(self):
        if self.s2 == []:
            self.empty()
        self.s2.pop(-1)
        
    def put(self, value):
        self.s1.append(value)

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())

class MyQueue(object):
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    
    def peek(self):
        if not self.stack2:
            self.stack2 = list(reversed(self.stack1))
            self.stack1 = []
        return self.stack2[-1]
        
    def pop(self):
        head = self.peek()

        self.stack2.pop(-1)
        
    def put(self, value):
        self.stack1.append(value)