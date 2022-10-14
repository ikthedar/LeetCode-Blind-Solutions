"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        oldToNew = {} # using hashmap to check which nodes are cloned
        
        def dfs(node):
            if node in oldToNew: # if node is in hashmap, means we already made a clone of it
                return oldToNew[node]   # then we can just return the cloned new one
            copy = Node(node.val) # if not exist, we create a new node using the Node constructor
            
            oldToNew[node] = copy   # also take the copy and add to the hashmap
            
            for nei in node.neighbors:
                copy.neighbors.append(dfs(nei))
                
            return copy
        
        return dfs(node) if node else None
