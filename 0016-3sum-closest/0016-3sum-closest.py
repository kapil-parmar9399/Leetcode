
class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(target - current_sum) < abs(target - closest):
                    closest = current_sum

                if current_sum == target:
                    return current_sum

                elif current_sum < target:
                    left += 1

                else:
                    right -= 1

        return closest
