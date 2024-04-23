class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}

        # add the pairs of indices and numbers
        # if you encounter a 'target - value = complement', add the indices to the array and return

        for i, num in enumerate(nums):
            hash_map[num] = i

        for i, num in enumerate(nums):
            complement = target - num
            if complement in hash_map and hash_map[complement] != i:
                return [i, hash_map[complement]]

            if complement in hash_map and hash_map[complement] != i:
                return [i, hash_map[complement]]
