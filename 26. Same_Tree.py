# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        # DFS: First set the base case
        
        if not p and not q: # if both trees are empty, it will be same tree
            return True
        if not p or not q: # if one of them is null, another one has value, it is not the same tree
            return False
        
        if p.val != q.val:
            return False
          
          # Set the recursive case
        
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right, q.right))
