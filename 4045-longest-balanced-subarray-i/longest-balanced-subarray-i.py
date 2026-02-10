class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)
        max_l = 0
        for i in range(n):
            dist_even = set()
            dist_odd = set()
            for j in range(i, n):
                num = nums[j]
                if num % 2 == 0:
                    dist_even.add(num)
                else:
                    dist_odd.add(num)
                
                if len(dist_even) == len(dist_odd):
                    max_l = max(max_l, j - i + 1)
        return max_l
        