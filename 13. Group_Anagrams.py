class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list) # defaultdict(list). It means "Defining a dictionary with values as a list"
        
        for s in strs:
            count = [0] * 26 # creating a list to keep as Keys in the Hashmap
            
            for c in s:
                count [ord(c) - ord("a")] += 1 # counting how many of each charater we have in each string
                
            res [tuple(count)].append(s) # since Python doesn't allow list to be stored as Keys, we need to use Tuple
            
        return res.values() # We will just retun the Values of hashmap not the keys
                
