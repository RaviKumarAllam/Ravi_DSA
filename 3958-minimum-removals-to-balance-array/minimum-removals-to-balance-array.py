from typing import List
from bisect import bisect_right


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
            nums.sort()
            max_ele = 0
            for i, min_value in enumerate(nums):
                right_b = bisect_right(nums, k * min_value)
                max_ele = max(max_ele, right_b - i)

            return len(nums) - max_ele

