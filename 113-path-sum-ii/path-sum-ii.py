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
            new_s = s + node.val

            if not node.left and not node.right and new_s == targetSum:
                ret.append(curr_path.copy())
            else:
                dfs(node.right, new_s)
                dfs(node.left, new_s)

            curr_path.pop()
        
            
        dfs(root, 0)
        return ret