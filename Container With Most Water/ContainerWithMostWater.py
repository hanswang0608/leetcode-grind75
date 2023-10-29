from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        biggest = 0
        while l < r:
            biggest = max(biggest, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return biggest

solution = Solution()
height = [1,8,6,2,5,4,8,3,7]
print(solution.maxArea(height))