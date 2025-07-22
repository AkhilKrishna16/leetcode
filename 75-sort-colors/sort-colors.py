class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # have one pointer marking red and one marking blue
        # iterate through the list and follow this:
        # 1. whenever we have a 0, move it to the front and shift the red pointer by 1 to the right
        # 2. whenever we have a 1, move it to the back and shift the blue pointer by 1 to the left
        # 3. whenever we have a 2, leave it ig
        red = 0
        blue = len(nums) - 1
        i = 0
        while i <= blue:
            if nums[i] == 0:
                nums[i], nums[red] = nums[red], nums[i]
                red += 1
                i = red
            elif nums[i] == 2:
                nums[i], nums[blue] = nums[blue], nums[i]
                blue -= 1
            else:
                i += 1
        

            
        