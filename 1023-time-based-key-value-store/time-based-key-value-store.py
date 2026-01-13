class TimeMap:

    def __init__(self):
        self.structure = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.structure[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.structure:
            values = self.structure[key]
            low, high = 0, len(values) - 1
            res = ""
            while low <= high:
                mid = (low + high) // 2
                if values[mid][0] <= timestamp:
                    res = values[mid][1]
                    low = mid + 1
                else:
                    high = mid - 1
            return res
        return ""



# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)