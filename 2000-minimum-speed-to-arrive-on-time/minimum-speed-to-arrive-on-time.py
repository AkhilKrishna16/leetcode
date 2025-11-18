class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def check(speed):
            total = 0
            for i in range(len(dist)):
                total += ceil(dist[i] / speed) if i != len(dist) - 1 else dist[i] / speed
                if total > hour:
                    return False
            return True
        
        low, high = 1, 10 ** 7
        while low <= high:
            mid = (low + high) // 2
            if check(mid):
                high = mid - 1
            else:
                low = mid + 1
            
        return low if check(low) else -1