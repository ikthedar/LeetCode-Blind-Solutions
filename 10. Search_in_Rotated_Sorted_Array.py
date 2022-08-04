class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            
            #left sorted portion
            if nums[l] <= nums[mid]:
                if target > nums[mid] or target < nums[l]: # then we search the right portion hence left pointer will be shifted to mid + 1
                    l = mid + 1
                else:
                    r = mid - 1
            #right sorted portion
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        
        return -1
                
                
