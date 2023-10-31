from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast,fastNext = 0, 1, 1
        while True:
            fastNext = (fast+1)%len(nums)
            if (slow != fast and nums[slow] == nums[fast]) or (slow != fastNext and nums[slow] == nums[fastNext]) :
                return nums[slow]
            slow = (slow+1)%len(nums)
            fast = (fast+2)%len(nums)

solution = Solution()

nums = [1,3,4,2,1]

# # for n = 4, max sum = 20
# # 1
# nums = [1,1,1,1,1] # sum=5
# nums = [1,1,1,3,4] # sum=10
# nums = [1,1,2,3,4] # sum=11
# # 2
# nums = [2,2,2,2,2] # sum=10
# nums = [2,2,2,1,3] # sum=10
# nums = [2,2,1,3,4] # sum=12
# # 3
# nums = [3,3,3,3,3] # sum=15
# nums = [3,3,1,2,4] # sum=13
# # 4
# nums = [4,4,4,4,4] # sum=20
# nums = [4,4,1,2,3] # sum=14



print(solution.findDuplicate(nums))