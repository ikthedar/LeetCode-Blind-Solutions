# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: # base case
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right)) # recursive case
   
    ## Iterative BFS
    #     if not root:
    #        return 0
        
     #   level = 1 #maintain the current level we are at, so if there is root, the tree will must have 1 level
      #  q = deque([root]) # Represent the array as a queue. Then add the root in the queue.
        
       # while q: # since we are keep going untill the queue is empty
        #    for i in range(len(q)):
         #       root = q.popleft()
          #      if root.left:
           #         q.append(root.left)
            #    if root.right:
             #       q.append(root.right)
           # level += 1
       # return level
        
