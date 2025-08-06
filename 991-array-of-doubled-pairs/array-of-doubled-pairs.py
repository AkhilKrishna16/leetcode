class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # count the number of elements
        m = Counter(arr)
        for num in sorted(arr, key=abs):
            if m[num] == 0:
                continue
            if m[num * 2] == 0:
                return False
            m[num * 2] -= 1
            m[num] -= 1
        return True