class Solution:
    def numberOfSteps(self, num: int, count: int = 0) -> int:

        if num == 0:
            return count

        if num % 2 == 0:
            num = num // 2
        else:
            num = num - 1

        count += 1

        return self.numberOfSteps(num, count)