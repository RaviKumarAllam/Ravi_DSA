class Solution:
    def addBinary(self, a: str, b: str) -> str:
        d_a = int(a, 2)
        d_b = int(b, 2)
        d_sum = d_a + d_b
        b_result = bin(d_sum)[2:]
        return b_result  