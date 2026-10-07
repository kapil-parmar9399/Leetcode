class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        result = {}

        for i in range(len(nums)):
            if nums[i] in result:
                old_index = result[nums[i]]

                if i - old_index <= k:
                    return True

            result[nums[i]] = i

        return False