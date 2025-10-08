# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        q = deque([root])

        while q and root:
            n = len(q)
            m = float('-inf')
            for _ in range(n):
                el = q.popleft()
                m = max(el.val, m)
                if el.left:
                    q.append(el.left)
                if el.right:
                    q.append(el.right)
            ret.append(m)
        return ret