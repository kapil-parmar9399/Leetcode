
class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        prefix_sum = 0
        rimender_count = {0: -1}

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if k != 0:
                rimender = prefix_sum % k
            else:
                rimender = prefix_sum

            if rimender in rimender_count:
                length = i - rimender_count[rimender]

                if length >= 2:
                    return True
            else:
                rimender_count[rimender] = i

        return False
