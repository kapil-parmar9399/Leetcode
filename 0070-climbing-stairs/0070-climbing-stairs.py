class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}

        def solve(n):
            if n == 1:
                return 1

            if n == 2:
                return 2

            if n in dp:
                return dp[n]

            dp[n] = solve(n - 1) + solve(n - 2)

            return dp[n]

        return solve(n)