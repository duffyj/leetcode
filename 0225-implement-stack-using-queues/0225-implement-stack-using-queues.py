class MyStack:

    def __init__(self):
        self.mainQueue = deque([])

    def push(self, x: int) -> None:
        self.mainQueue.append(x)

    def pop(self) -> int:
        return self.top(isTop=False)

    def top(self, isTop=True) -> int:
        if len(self.mainQueue) == 1:
            return self.mainQueue[0] if isTop else self.mainQueue.popleft()
        tmpQ = []
        for _ in range(len(self.mainQueue)-1):
            tmpQ.append(self.mainQueue.popleft())
        v = self.mainQueue.popleft()
        self.mainQueue = deque(tmpQ)
        if isTop:
            self.mainQueue.append(v)
        return v        
        

    def empty(self) -> bool:
        return len(self.mainQueue) == 0

# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()