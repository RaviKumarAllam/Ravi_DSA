class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        pre_bit = -1
    
        while n > 0:
            curr_bit = n & 1
            if pre_bit == curr_bit:
                return False
            pre_bit = curr_bit
            n >>= 1
        return True      