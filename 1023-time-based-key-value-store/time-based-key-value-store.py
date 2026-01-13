class TimeMap:

    def __init__(self):
        self.structure = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.structure[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.structure:
            for i in range(len(self.structure[key]) - 1, -1, -1):
                if self.structure[key][i][0] <= timestamp:
                    return self.structure[key][i][1]
        return ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)