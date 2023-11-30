from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev = nums[0]
        cur = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            temp = cur
            cur = max(cur, nums[i] + prev)
            prev = temp
        return cur

solution = Solution()
nums = [2,7,9,3,1]
print(solution.rob(nums))