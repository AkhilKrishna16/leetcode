class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        curr = []

        def dfs(i):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            elif i >= len(nums):
                return
            
            for j in range(len(nums)):
                if nums[j] not in curr:
                    curr.append(nums[j])
                    dfs(j)
                    curr.pop()
        dfs(0)
        return res