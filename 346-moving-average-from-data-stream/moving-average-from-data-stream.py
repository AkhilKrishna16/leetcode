class MovingAverage:

    def __init__(self, size: int):
        self.window = size
        self.con = deque()

    def next(self, val: int) -> float:
        self.con.append(val)
        temp = deque(list(self.con))
        i = 0
        ret = 0 
        while temp and i < self.window:
            ret += temp.pop()
            i += 1
        return ret / i



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)