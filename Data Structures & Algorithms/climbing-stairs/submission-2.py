class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)

        def backtrack(num):
            if num < 0:
                return 0
            if num == 0:
                return 1
            if memo[num] != -1:
                return memo[num]

            memo[num] = backtrack(num-1) + backtrack(num-2)
            return memo[num]

        return backtrack(n)