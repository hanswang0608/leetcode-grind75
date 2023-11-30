from typing import List

# reuses elements, wrong solution
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        dp = {}
        #find any subarr == sum(nums)/2
        if sum(nums) % 2 != 0:
            return False
        def dfs(target, nums, s):
            if target in dp:
                return dp[target]
            dp[s] = True
            if target == 0:
                return True
            for i, num in enumerate(nums):
                if dfs(target-num, nums[i+1:], s+num):
                    return True
            return False
        return dfs(sum(nums)/2, nums, 0)
    
solution = Solution()
nums = [1,2,5]
print(solution.canPartition(nums))