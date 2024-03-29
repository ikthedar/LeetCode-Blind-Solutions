class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        # creating a helper function inside the original function
        def valid(node, left, right):
            if not node:
                return True # in any binary search recursive function, if node is empty, that is a BST
            
            if not (node.val < right and node.val > left):
                return False
            
            return (valid(node.left, left, node.val) and
                    valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("inf"))
