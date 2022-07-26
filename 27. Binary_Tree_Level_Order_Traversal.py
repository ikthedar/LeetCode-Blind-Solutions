# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        
        q = collections.deque()
        if root:
            q.append(root)
        
        # now start running the BFS
        
        # BFS will end when our queue is empty
        while q:
            qLen = len(q) # assiging the length of the q/ how many elements in the q currently
            # we are gonna loop through every single one of those values
            # qLen is basically ensuring that we iterate through one level at a time
            
            # now with those nodes, from that level, we will be adding to its own list
            # and then we add that list to the res list
            val = []
            
            # so we will loop through every value of this 
            for i in range(qLen):
                node = q.popleft # we will always pop nodes from the left of the queue; First In First Out (FIFO)
                val.append(node.val)
                if node: # the node could be null, so we will checkit here with the if statement
                    q.append(node.left)
                    q.append(node.right)
            if val:
                res.append(val) # adding all the level sublists to the main result list
                    
        return res
