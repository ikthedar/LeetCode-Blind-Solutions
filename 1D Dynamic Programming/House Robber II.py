class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))
        
        
    def helper(self, nums):
            robBefAdj, robAdj = 0, 0
            
            for n in nums:
                newRob = max(robBefAdj + n, robAdj)
                robBefAdj = robAdj
                robAdj = newRob
                
            return robAdj
