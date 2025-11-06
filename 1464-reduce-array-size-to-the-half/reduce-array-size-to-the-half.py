class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        c = Counter(arr)
        c = dict(sorted(c.items(), key=lambda x: x[1], reverse=True))
        l = len(arr)
        total = 0
        for key in c:
            l -= c[key]
            total += 1
            if l <= len(arr) // 2:
                return total
        
        return total
            
