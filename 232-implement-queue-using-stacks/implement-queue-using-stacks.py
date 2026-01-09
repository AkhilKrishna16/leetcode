class MyQueue:

    def __init__(self):
        self.queue = [] # this simulates the reverse insertion order stack

    def push(self, x: int) -> None:
        temp = [] # this will hold the elements for reverse order
        while self.queue:
            temp.append(self.queue.pop())
        temp.append(x)
        while temp:
            self.queue.append(temp.pop())

    def pop(self) -> int:
        return self.queue.pop()

    def peek(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()