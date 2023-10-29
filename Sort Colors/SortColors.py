from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        zeroStart = 0
        oneStart = 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(zeroStart, 0)
                zeroStart += 1
                oneStart += 1
            elif nums[i] == 1:
                nums.pop(i)
                nums.insert(oneStart, 1)
                oneStart += 1
            i += 1

solution = Solution()
nums = [2,0,2,1,1,0]
solution.sortColors(nums)