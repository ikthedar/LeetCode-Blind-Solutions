# Instead of using Sort or Brute force method, we are using Hash technique to get more effeciency for Time Complexity.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        
        for n in nums:
            if n in hashset:
                return True
                
            
            hashset.add(n)
        return False
            
            
           
