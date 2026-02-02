from sortedcontainers import SortedList
class Solution:
    def minimumCost(self, nums: List[int], k: int, dist: int) -> int:
        wSum = sum(nums[i] for i in range(1, dist + 2))
        selected = SortedList(nums[i] for i in range(1, dist + 2))
        cand = SortedList()

        def balance() -> int:
            nonlocal wSum
            while len(selected) < k -1:
                minCand = cand[0]
                wSum += minCand
                selected.add(minCand)
                cand.remove(minCand)

            while len(selected) > k -1:
                maxSel = selected[-1]
                wSum -= maxSel
                selected.remove(maxSel)
                cand.add(maxSel)

            return wSum
        wSum = balance()
        minWinSum = wSum

        for i in range(dist + 2, len(nums)):
            OutofScope = nums[i - dist -1]
            if OutofScope in selected:
                wSum -=OutofScope
                selected.remove(OutofScope)
            else:
                cand.remove(OutofScope)

            if nums[i] < selected[-1]:
                wSum += nums[i]
                selected.add(nums[i])
            else:
                cand.add(nums[i])
            wSum = balance()
            minWinSum = min(minWinSum, wSum)
            
        return nums[0] + minWinSum