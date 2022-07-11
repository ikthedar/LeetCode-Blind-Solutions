class Solution:
    def climbStairs(self, n: int) -> int:
        one, two = 1, 1 # setting two pointers to 1 
        
        for i in range (n-1):
            temp = one
            one = one + two
            two = temp
            
        return one
