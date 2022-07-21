class Solution:

    def encode(self, strs): # we are taking a list of strings
        # write your code here
        res = "" # we are creating a single string
        
        for s in strs: # will travers each string "s" from the list of strings "strs"
            res += str(len(s)) + "#" + s
        return res

      
    def decode(self, str):
        # write your code here
        res, i = [], 0

        while i < len(str):
            j = i
            while str[j] != "#":
                j += 1
            length = int(str[i:j]) # will take the digit between i and j
            res.append(str[j + 1 : j + 1 + length]) # since this is a list, we are using .append
            i = j + 1 + length
        return res
