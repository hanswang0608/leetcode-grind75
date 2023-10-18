from typing import List

# d is all of the currently possible sums, where each nth bit denotes that n can be summed to
# d = 1011 means 0, 1, 3 can be summed to
# d << 3 = 1011000 adds 3 to all of the previous summable values, so now 3,4,6 can be summed to
# d |= d << 3 combines previously summable values with new values
# loop through all of nums to calculate all summable values
# check whether or not halfSum can be reached using bitwise& to check the halfsum-th bit
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s&1: return False
        d, halfSum = 1, s//2
        for num in nums:
            # using "bitset" to replace the inner loop of traditional knapsack problem
            d  |= d << num
        return d&1<<halfSum

solution = Solution()
nums = [10000,10000]
print(solution.canPartition(nums))