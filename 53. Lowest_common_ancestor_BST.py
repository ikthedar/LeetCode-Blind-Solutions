# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        
        while curr:
            # if given value of p and q both are more then current node(root) value, shift the current node to the right (BST rule)
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right 
            # if given value of p and q both are less then current node(root) value, shift the current node to the left (BST rule)
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
               
            else:
                return curr
            
