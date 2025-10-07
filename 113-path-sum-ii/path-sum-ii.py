# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ret = []

        def dfs(root, curr, curr_sum):
            if not root:
                return
            curr_sum = curr_sum + root.val
            curr.append(root.val)

            if not root.left and not root.right and targetSum == curr_sum:
                ret.append(curr.copy())
            else:
                dfs(root.left, curr, curr_sum)
                dfs(root.right, curr, curr_sum)
            curr.pop()
        dfs(root, [], 0)
        return ret
