class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        ret = []

        for i in range(len(nums)):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)

            if q[0] + k == i:
                q.popleft()
            
            if i >= k - 1:
                ret.append(nums[q[0]])
        
        return ret


                
