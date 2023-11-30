from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(nums, path, output):
            output.append(path)
            if not nums:
                return
            for i in range(len(nums)):
                dfs(nums[i+1:], path + [nums[i]], output)

        output = []
        dfs(nums, [], output)
        return output

solution = Solution()
nums = [1,2,3]
print(solution.subsets(nums))