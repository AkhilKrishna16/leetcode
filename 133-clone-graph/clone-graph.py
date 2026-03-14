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
        # start from the node given which is 1
        # then you have to process the following nodes 
        # which is 2, 4 from the node neighbors
        # you basically create a bunch of nodes as a result
        # you can store the map as a result
        # the map should store the nodes and the connections are given as the nodes

        # node: 1 -> 2, 4, 2 -> 3, 1
        # map: {1: Node(1)->[Node(2), Node(4)], 2: Node(2)->[Node(3), Node(1)], 4: Node(4)->[Node(3), Node[1]], 3: Node(3)->[Node(4), Node(2)]}

        # dfs path: {1: Node(1)->[Node(2), Node(4)], 2: Node(2)->[Node(1),Node(3)], 4: Node(4)->[Node(3), Node(1)], 3: Node(3)->[Node(4), Node(2)]}

        # essential steps:
        # start from 1 in the dfs call, have a reference map for all the direct object pointers to nodes
        # then put 1 in the reference map, and then add all neighbors for the current node, if a node is already in the reference map, leave it, but if it is not create the node and add it.

        # dfs to all neighbors that haven't had their neighbors added; the only a node has neighbors is if we have added neighbors to this node, because at a node is when we add them
        
        # then do this until nothing is anymore and you just return
        if not node:
            return node
        reference_map = {1: Node(node.val, [])} 

        def dfs(vertex):
            # essentially if you have added the neighbors already, why re-visit? so return
            if vertex.val in reference_map and reference_map[vertex.val].neighbors:
                return
            
            for neighbor in vertex.neighbors: # then add all the neighbors from the current vertex
                if neighbor.val not in reference_map: # then add all the neighbors through the references of the nodes themselves
                    reference_map[neighbor.val] = Node(neighbor.val, [])
                new_neighbor_node = reference_map[neighbor.val]
                    
                
                reference_map[vertex.val].neighbors.append(new_neighbor_node)
                dfs(neighbor)
        
        dfs(node)
        return reference_map[1]
            

