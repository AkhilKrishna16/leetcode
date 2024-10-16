# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        paths = []
        # backtracking
        # once we reach the end such that there are no children of the specific node we append the specific string that is generated
        # pass the current string, and the node and add on to the string
        # 
        def dfs(root, s):
            # base case: we have no more children

            if not root: # base case
                return 

            s += str(root.val) # choice 
            if not root.left and not root.right:
                paths.append(s) # base case 

            dfs(root.left, s + '->') # recursion
            dfs(root.right, s + '->') # recursion


        dfs(root, '')
        return paths

        

        
        
