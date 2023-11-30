from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxProduct = maxP = minP = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < 0:
                temp = maxP
                maxP = minP
                minP = temp
            maxP = max(nums[i], maxP*nums[i])
            minP = min(nums[i], minP*nums[i])
            maxProduct = max(maxProduct, maxP)
        return maxProduct

solution = Solution()
nums = [-2,0,-1]
nums = [-3,0,1,-2]
nums = [-1,-2,-9,-6]
nums = [2,2,-5,2,2,-4,2,2,-3,2,2]
nums = [2,3,-2,4]
nums = [-2,3,-4]
nums = [-2]
nums = [1,0,-1,2,3,-5,-2]
nums = [2,-5,-2,-4,3]
print(solution.maxProduct(nums))