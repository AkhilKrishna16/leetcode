class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = []
        curr = []

        def dfs(i):
            if i > len(nums):
                return
            ret.append(curr.copy())

            for j in range(i, len(nums)):
                curr.append(nums[j])
                dfs(j + 1)
                curr.pop()
            
        
        dfs(0)
        return ret

                
                