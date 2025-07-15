class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # sort the two arrays
        # initialize the two pointers together and 

        nums1 = sorted(nums1)
        nums2 = sorted(nums2)

        pointer1 = 0
        pointer2 = 0

        ret = []

        while pointer1 < len(nums1) and pointer2 < len(nums2):
            if nums2[pointer2] < nums1[pointer1]:
                while pointer2 < len(nums2) and nums2[pointer2] < nums1[pointer1]:
                    pointer2 += 1
            
            if pointer1 < len(nums1) and pointer2 < len(nums2) and nums2[pointer2] == nums1[pointer1] and nums1[pointer1] not in ret:
                ret.append(nums1[pointer1])
            
            pointer1 += 1
        
        return ret
