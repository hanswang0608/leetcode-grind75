from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p1 = p2 = p3 = n1 = n2 = 1
        maxProduct = float('-inf')
        for num in nums:
            if num < 0:
                p3 = p2
                p2 = p1
                p1 = 1
                n2 = n1
                n1 = num
                maxProduct = max(p2*p3*n1*n2, maxProduct, num)
            else:
                p1 = p1*num
                maxProduct = max(p1, p1*p2*p3*n1*n2, maxProduct, num)
        return maxProduct

solution = Solution()
nums = [2,3,-2,4]
nums = [-2,3,-4]
nums = [-2,0,-1]
nums = [2,-5,-2,-4,3]
nums = [-3,0,1,-2]
nums = [-2]
nums = [2,2,-5,2,2,-4,2,2,-3,2,2]
print(solution.maxProduct(nums))