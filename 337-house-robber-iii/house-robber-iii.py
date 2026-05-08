# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # we probably have to return dp[root]
        # if you take root, then you have to skip both children
        # so dp[root] = max(root.val + dp[root.right.left] + dp[root.right.right] + dp[root.left.right] + dp[root.left.left], dp[root.right] + dp[root.left])
        
        # return dp[root]
        # base case: dp[root] if root has no children = root.val

        # now you have to dfs to the bottom and then return up
        # it is a top-down recursion
        @cache
        def dfs(root): # this returns the optimal value for root
            if not root.left and not root.right:
                return root.val
            
            # this first part is to compute the case of skipping the current
            left_child = right_child = 0

            if root.left: 
                left_child = dfs(root.left)
            if root.right:
                right_child = dfs(root.right)
            
            skip = left_child + right_child

            # the next part is to compute the case of taking the current

            left_subtree = right_subtree = 0

            if root.left and root.left.left:
                left_subtree += dfs(root.left.left)
            if root.left and root.left.right:
                left_subtree += dfs(root.left.right)
            if root.right and root.right.right:
                right_subtree += dfs(root.right.right)
            if root.right and root.right.left:
                right_subtree += dfs(root.right.left)
            
            return max(root.val + right_subtree + left_subtree, skip)
        

        return dfs(root)