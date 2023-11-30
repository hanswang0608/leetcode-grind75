from typing import List

# doesn't work fully
class Solution:
    def maxArea(self, height: List[int]) -> int:
        dp = [None for _ in range(len(height))]
        dp[1] = [0,1]
        def area(a):
            l, r = a
            return min(height[l], height[r]) * (r-l)
        for i in range(2, len(height)):
            if height[i] == 0:
                dp[i] = dp[i-1]
                continue
            a1 = area([dp[i-1][1], i])
            a2 = area([dp[i-1][0], i])
            a3 = area(dp[i-1])
            if max(a1,a2,a3) == a1:
                dp[i] = [dp[i-1][1], i]
            elif max(a1,a2,a3) == a2:
                dp[i] = [dp[i-1][0], i]
            else:
                dp[i] = dp[i-1]
        print(dp)
        return area(dp[-1])

solution = Solution()
height = [2,3,10,5,7,8,9]
print(solution.maxArea(height))