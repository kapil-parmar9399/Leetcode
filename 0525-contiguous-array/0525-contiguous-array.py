
class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = 0
        max_length = 0
        seen = {0: -1}

        for i in range(len(nums)):
            if nums[i] == 0:
                count -= 1
            else:
                count += 1

            if count in seen:
                length = i - seen[count]

                if length > max_length:
                    max_length = length
            else:
                seen[count] = i

        return max_length
