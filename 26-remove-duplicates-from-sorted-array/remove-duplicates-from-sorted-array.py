class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # have a marker for the section of "waste" or dup. elements
        # whenever we have a duplicate, just subtract one from the dup. elements
        # whenever 


        insert_pos = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                nums[insert_pos] = nums[i]
                insert_pos += 1
        
        return insert_pos
        