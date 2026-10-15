class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        dict={}
        majority=nums[0]
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else:
                dict[nums[i]]=1

        for i in dict:
            if dict[i] > len(nums)//2:
                majority=i

        return majority        
