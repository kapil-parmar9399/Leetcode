class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        prefix=[]
        total=0
        for i in range (len(nums)):
            total=total+nums[i]
            prefix.append(total)

        return prefix    