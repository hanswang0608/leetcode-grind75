class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        winSum = float('-inf')
        for num in nums:
            winSum = winSum + num
            if winSum >= num and winSum >= maxSum:
                maxSum = winSum
            elif num >= winSum and num >= maxSum:
                maxSum = num
                winSum = num
            elif num >= winSum:
                winSum = num
        return maxSum