class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
      
        for i, value in enumerate(nums):
            if value == 0:
                res.append(0)
            else:
               
                tar_index = (i + value + n) % n
                res.append(nums[tar_index])
              
        return res