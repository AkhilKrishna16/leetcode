class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # 3 -> 1
        # 2 -> 0
        # 3 -> 1

        # 2 -> 1
        res = 0
        majority = 0

        for num in nums:
            if majority == 0:
                res = num
            
            if res == num:
                majority += 1
            else:
                majority -= 1
        
        return res