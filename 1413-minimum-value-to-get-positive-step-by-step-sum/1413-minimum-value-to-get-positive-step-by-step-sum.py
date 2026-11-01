class Solution:
    def minStartValue(self, nums: list[int]) -> int:
        prefix_sum = 0
        minimum = 0

        for i in range(len(nums)):
            prefix_sum += nums[i]

            if prefix_sum < minimum:
                minimum = prefix_sum

        starting_value = 1 - minimum

        return starting_value
