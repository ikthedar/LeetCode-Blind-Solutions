class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # using XOR operation
        res = len(nums)
        for i in range(len(nums)):
            res ^= i ^ nums[i]
        return res

-----
     # using SUM method   
        res = len(nums)

        for i in range(len(nums)):
            res += i - nums[i]
        return res
