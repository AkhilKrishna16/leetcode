class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        # find the complement of each value, if it exists and it is not the same index as the one currently, you have your value

        for i, num in enumerate(nums):
            hash_map[num] = i
        
        # iterate through the keys and find the complement of each key's value 
        # return the value that corresponds to the complement 

        # complement = key - target
        # if hash_map[complement] exists and hash_map[complement] != hash_map[key], return pair

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map and hash_map[complement] != i:
                return [i, hash_map[complement]]
        
