"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # have a graph that contains the mappings between numbers and clones
        if not node:
            return None
        og_clone = Node(node.val, [])
        q = deque([node])
        clone_map = {node.val: og_clone}

        while q:
            curr = q.popleft() # actual 
            curr_clone = clone_map[curr.val] # clone 

            for neighbor in curr.neighbors:
                if neighbor.val not in clone_map:
                    clone_map[neighbor.val] = Node(neighbor.val, [])
                    q.append(neighbor)
                curr_clone.neighbors.append(clone_map[neighbor.val])
        
        return clone_map[node.val]