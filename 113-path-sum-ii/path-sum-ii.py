# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret = []
        curr_path = []

        def dfs(node, s):
            if not node:
                return
            curr_path.append(node.val)
            # one for the left, one for the right
            if not node.left and not node.right and targetSum == s + node.val:
                ret.append(curr_path.copy())
            else:
                if node.right:
                    dfs(node.right, s + node.val)
                if node.left:
                    dfs(node.left, s + node.val)
            
            curr_path.pop()
            
        dfs(root, 0)
        return ret