class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dict = {}
        majority = 0
        ans = nums[0]

        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1

        for i in dict:
            if dict[i] > majority:
                majority = dict[i]
                ans = i

        return ans