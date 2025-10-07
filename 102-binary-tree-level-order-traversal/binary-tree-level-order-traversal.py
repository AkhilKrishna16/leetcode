# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []    
        q = deque([root])

        while q and root:
            n = len(q)
            curr = []
            for _ in range(n):
                el = q.popleft()
                curr.append(el.val)
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
            ret.append(curr)
        
        return ret
                