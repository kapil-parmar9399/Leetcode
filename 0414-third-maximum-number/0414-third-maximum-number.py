class Solution:
    def thirdMax(self, nums: list[int]) -> int:

        new = list(set(nums))
        new.sort()

        n = len(new)

        if n >= 3:
            return new[-3]
        else:
            return new[-1]