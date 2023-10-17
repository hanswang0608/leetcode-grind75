from typing import List

# 0/1 knapsack problem
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        target = int(sum(nums)/2)
        dp = [[False for _ in range(target+1)] for _ in range(len(nums)+1)]
        dp[0][0] = True
        for i in range(1, len(nums)+1):
            for j in range(1, target+1):
                if j-nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[len(nums)][target]


solution = Solution()
nums = [1,5,11,5]
print(solution.canPartition(nums))