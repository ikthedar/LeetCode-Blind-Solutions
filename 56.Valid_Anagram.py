class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ## Sorting method
        ## return sorted(s) == sorted(t) 
        
        
        if len(s) != len(t):
            return False
        
        #creating HashMap in Python
        countS, countT = {}, {}
        
        # Here we built the hashmap and counted each character by iterating through s and t list
        for i in range(len(s)): # since length of s and t will be same, using just len of s
            countS[s[i]] = 1 + countS.get(s[i], 0) # we used .get funct since if there is no char
            countT[t[i]] = 1 + countT.get(t[i], 0) # in the hash, by default we will say 1 + 0
        
        # iterate through key values and make sure equal count
        for c in countS:
            if countS[c] != countT.get(c, 0): #using get if the key c of S doesn't exist in T, it will give 0 i
                return False
        
        return True
