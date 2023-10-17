from typing import List

# use backtracking to find the actual 2 subarrays that are equal, time limit error
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        return len(self.combinationSum(nums, sum(nums)/2)) > 0
    
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        def dfs(target, candidates, candidate = None):
            if target == 0:
                return [[candidate]]
            if target < 0:
                return None
            paths = []
            for i, num in enumerate(candidates):
                ret = dfs(target-num, candidates[i+1:], num)
                if not ret:
                    continue
                for path in ret:
                    if candidate:
                        paths.append([candidate] + path)
                    else:
                        paths.append(path)
            return paths
        return dfs(target, candidates)
    
solution = Solution()
nums = [1,2,3,5]
print(solution.canPartition(nums))