class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occurances = []
        ret = [-1] * len(queries)

        for i in range(len(nums)):
            if nums[i] == x:
                occurances.append(i)
        
        for i in range(len(queries)):
            if queries[i] > len(occurances):
                continue
            else:
                ret[i] = occurances[queries[i] - 1]
        
        return ret