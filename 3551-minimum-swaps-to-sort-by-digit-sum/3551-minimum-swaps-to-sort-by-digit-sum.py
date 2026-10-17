
class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        arr = []

        for num in nums:
            total = 0

            for digit in str(num):
                total += int(digit)

            arr.append((total, num))

        arr.sort()

        sorted_nums = []

        for total, num in arr:
            sorted_nums.append(num)

        pos = {}

        for i in range(len(nums)):
            pos[nums[i]] = i

        swaps = 0

        for i in range(len(nums)):
            if nums[i] != sorted_nums[i]:
                swaps += 1

                j = pos[sorted_nums[i]]

                pos[nums[i]] = j
                pos[sorted_nums[i]] = i

                nums[i], nums[j] = nums[j], nums[i]

        return swaps
