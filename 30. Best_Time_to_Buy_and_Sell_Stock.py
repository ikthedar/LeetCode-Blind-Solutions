# We used the most common programmin technique "Two Pointers" to solve this problem.
# No extra memory is used since we just used pointers, no array. So, Space = O(1).
# Time complexity = O(n), since time is linear here, didn't use any brute force method.

# my solution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxP = 0
        
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
                r = r + 1
            else:
                curP = prices[r] - prices[l]
                maxP = max(curP, maxP)
                r = r + 1
                
        return maxP

# NeetCode example
'''class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1 # Left=buying, right=selling
        maxP = 0
        
        while r < len(prices):
            #profitable?
            if prices[l] < prices[r]:
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r
            r +=1
        return maxP'''
