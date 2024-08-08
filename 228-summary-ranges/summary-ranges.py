class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        sr = []
        
        # mark the start of each range 
        # match values and if they match, add to the range
        # else finish the value and add based on whether the start is the same as the num or not
        # if reach the end of the list, add to the list the start and the end value
        if not nums:
            return []
        start = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1] + 1:
                if nums[i - 1] == start:
                    sr.append(f"{start}")
                elif nums[i - 1] != start:
                    sr.append(f"{start}->{nums[i - 1]}")

                start = nums[i] 
        
        if start == nums[-1]:
            sr.append(f"{start}")
        elif start != nums[-1]:
            sr.append(f"{start}->{nums[-1]}")

        return sr