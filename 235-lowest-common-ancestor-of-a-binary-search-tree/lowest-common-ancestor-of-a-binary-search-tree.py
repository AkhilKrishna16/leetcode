# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if the current node is equal to p or q, then return that node
        # if both nodes are less than the current value -> traverse left side
        # if both nodes are greater than the current value -> traverse right side
        # if one is greater and one is less than -> return the current node
        # if null node currently, you couldn't find a node thats equal to the curren 
        if not root:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        elif p.val < root.val and q.val > root.val or q.val < root.val and p.val > root.val:
            return root
        
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right, p, q)
        
        return root
