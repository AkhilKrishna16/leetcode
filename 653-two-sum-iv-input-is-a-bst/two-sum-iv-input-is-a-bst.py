# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        m = set()

        def dfs(root, k):
            if not root:
                return False
            
            if (k - root.val) in m:
                return True
            else:
                m.add(root.val)
            
            left = dfs(root.left, k)
            right = dfs(root.right, k)
            
            return left or right
        
        return dfs(root, k)
