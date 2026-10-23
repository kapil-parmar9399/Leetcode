class Solution:
    def limitOccurrences(self, nums: List[int], k: int) -> List[int]:
        left = 0

        for right in range(len(nums)):
            if left < k or nums[right] != nums[left - k]:
                nums[left] = nums[right]
                left += 1

        return nums[:left]