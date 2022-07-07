class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        
        for i in range(32):
            res = res << 1 # Bitwise left shft
            bit = n % 2 
            res += bit
            n = n >> 1 # Bitwise right shift
            
        return res
