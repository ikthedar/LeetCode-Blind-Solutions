class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        
        while l <= r: # keep running the search while our pointers ar at valid position
            if nums[l] < nums [r]: # means if we got a subarray that is sorted its left pointer will be largar than the right pointer
                res = min(res, nums[l])
                break # then can breakout of this while loop
            
            # if the array is not sorted, thats when we do binary search
            m = (l + r) // 2
            res = min(res, nums[m])
            
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m - 1
        
        return res
