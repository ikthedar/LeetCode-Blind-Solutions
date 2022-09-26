class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set() # we could have used lists/ any other DS here, why using Set? = Because of Set's times complexity?
        l = 0
        res = 0
        
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        
        return res


'''class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        
        for r in range(len(s)): #since right pointer will go through every single character
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1 # we keep doing that while that duplicate remains in the character set
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res'''
