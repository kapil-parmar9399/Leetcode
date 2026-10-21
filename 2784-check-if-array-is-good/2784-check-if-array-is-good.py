
class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = max(nums)

        if len(nums) != n + 1:
            return False

        if nums.count(n) != 2:
            return False

        for i in range(1, n):
            if nums.count(i) != 1:
                return False

        return True
