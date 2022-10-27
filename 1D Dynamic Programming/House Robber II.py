class Solution:
    def rob(self, nums: List[int]) -> int:
        # nums[1:] is array except the first one; nums[:-1] array except the last one
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1])) 
        
        
    def helper(self, nums):
            robBefAdj, robAdj = 0, 0
            
            for n in nums:
                newRob = max(robBefAdj + n, robAdj) #  eg: [1, 3, 4, 5, 2] for 5 newRob ... 
                robBefAdj = robAdj
                robAdj = newRob
                
            return robAdj
