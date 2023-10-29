class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[1] * (n+1) for _ in range(m+1)]
        for i in range(2, m+1):
            for j in range(2, n+1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]

solution = Solution()
print(solution.uniquePaths(10, 10))