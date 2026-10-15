class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:
    
        dict = {}
        ans = []

        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1

        for i in dict:
            if dict[i] > len(nums) // 3:
                ans.append(i)

        return ans