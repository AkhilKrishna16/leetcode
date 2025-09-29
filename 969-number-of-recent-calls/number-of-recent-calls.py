class RecentCounter:

    def __init__(self):
        self.ping_store = deque([])

    def ping(self, t: int) -> int:
        self.ping_store.append(t)
        count = 0
        while True:
            if self.ping_store[0] < t - 3000:
                self.ping_store.popleft()
                count += 1
            else:
                break
        return len(self.ping_store)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)