class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        f=0
        while f<n-2 and nums[f]<nums[f+1]:
            f+=1
        if f==0:
            return False
        v=f
        while v<n-1 and nums[v] > nums[v +1]:
            v +=1
        if v==f or v==n-1:
            return False
        f=v
        while f <n-1 and nums[f] < nums[f+1]:
            f+=1
        return f ==n-1
        