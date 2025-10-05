# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, currMax):
            if not root:
                return 0
            
            count = 1 if currMax <= root.val else 0
            print(count)
            return count + dfs(root.left, max(currMax, root.val)) + dfs(root.right, max(currMax, root.val))
        count = dfs(root, float('-inf'))
        return count