class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        winSum = float('-inf')
        for num in nums:
            winSum = max(winSum + num, num)
            maxSum = max(maxSum, winSum)
        return maxSum