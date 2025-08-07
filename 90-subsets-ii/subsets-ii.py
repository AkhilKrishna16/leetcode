class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        curr = []
        nums = sorted(nums)

        def dfs(i):
            if i >= len(nums):
                if curr.copy() not in ret:
                    ret.append(curr.copy())
                return
            
            curr.append(nums[i])
            dfs(i + 1)

            curr.pop()
            dfs(i + 1)

        dfs(0)
        return ret