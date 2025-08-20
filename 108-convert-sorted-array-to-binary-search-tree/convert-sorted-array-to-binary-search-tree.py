# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # find the middle value 
        # then update such that the root of the tree is the middle
        # then dfs over the left part of that array and the right part of the array
        # then add the values
        root = TreeNode()
        def buildTree(left, right):
            if left > right:
                return 
            mid = (left + right) // 2
            
            node = TreeNode(nums[mid])

            node.left = buildTree(left, mid - 1)
            node.right = buildTree(mid + 1, right)

            return node
        
        return buildTree(0, len(nums) - 1)
