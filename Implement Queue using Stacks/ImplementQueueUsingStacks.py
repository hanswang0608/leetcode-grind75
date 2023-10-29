class MyQueue:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        temp = []
        while len(self.stack) > 0:
            temp.append(self.stack.pop())
        ret = temp.pop()
        while len(temp) > 0:
            self.stack.append(temp.pop())
        return ret

    def peek(self) -> int:
        temp = []
        while len(self.stack) > 0:
            temp.append(self.stack.pop())
        ret = temp[-1]
        while len(temp) > 0:
            self.stack.append(temp.pop())
        return ret

    def empty(self) -> bool:
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()