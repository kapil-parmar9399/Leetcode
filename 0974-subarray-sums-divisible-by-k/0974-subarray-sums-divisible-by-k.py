class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        count=0
        prefix_sum=0
        rimender_count={0:1}

        for i in range (len(nums)):
            prefix_sum +=nums[i]

            rimender=prefix_sum % k

            if rimender in rimender_count:
                count+=rimender_count[rimender]
                rimender_count[rimender] += 1
            else:
                rimender_count[rimender] = 1

        return count
