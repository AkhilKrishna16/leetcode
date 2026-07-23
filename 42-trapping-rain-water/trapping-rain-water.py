class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0

        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        curr = 0

        while l < r:
            if maxL <= maxR:
                l += 1
                curr += max(0, min(maxL, maxR) - height[l])
                maxL = max(maxL, height[l])
            else:
                r -= 1
                curr += max(0, min(maxL, maxR) - height[r])
                maxR = max(maxR, height[r])
        
        return curr
                