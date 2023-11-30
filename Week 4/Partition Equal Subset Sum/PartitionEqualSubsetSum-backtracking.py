from typing import List

# solve by checking all permutations and backtracking, time limit error
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #find any subarr == sum(nums)/2
        if sum(nums) % 2 != 0:
            return False
        def dfs(target, nums):
            if target == 0:
                return True
            for i, num in enumerate(nums):
                if dfs(target-num, nums[i+1:]):
                    return True
            return False
        return dfs(sum(nums)/2, nums)
    
solution = Solution()
nums = [1,2,5]
print(solution.canPartition(nums))