class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n = len(nums)
        count = {}

        for i in range(len(nums)):
            if nums[i] in count:
                count[nums[i]] += 1
            else:
                count[nums[i]] = 1

        mx = max(count)
        base = mx

        if len(nums) == base + 1:
            if count.get(base) != 2:
                return False

            if len(count) != base:
                return False

            for i in count:
                if i != base and count[i] != 1:
                    return False

            return True

        else:
            return False