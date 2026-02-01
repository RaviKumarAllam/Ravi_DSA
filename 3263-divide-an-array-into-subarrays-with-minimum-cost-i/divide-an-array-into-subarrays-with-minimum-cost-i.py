class Solution:
    def minimumCost(self, nums: List[int]) -> int:

        a = 50
        b = a
        c = a

        for i in range(1, len(nums)):
            if nums[i] < b:
                c = b
                b = nums[i]
            elif nums[i] < c:
                c = nums[i]

        return nums[0] + b + c
        