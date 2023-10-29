from typing import *
from math import *

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, u = 0, len(nums)-1
        while l <= u:
            mid = (l+u)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid+1
            else:
                u = mid-1
        return -1
    
solution = Solution()
arr = [-1,0,3,5,9,12]
print(solution.search(arr, 0))