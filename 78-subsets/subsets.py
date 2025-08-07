class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        curr = []
        i = 0
        def dfs(i):
            if i >= len(nums):
                ret.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i + 1)

            curr.pop()
            dfs(i + 1)

        dfs(0)
        return ret