class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        i = 0
        j = i + 1
        k = len(nums)-1
        while nums[i] <= 0 and i < len(nums) and j < len(nums) and k < len(nums):
            if (i > 0 and nums[i] == nums[i-1]) or j >= k:
                i += 1
                j = i + 1
                k = len(nums)-1
                continue
            s = nums[i] + nums[j] + nums[k]
            if s == 0:
                triplets.add((nums[i],nums[j],nums[k]))
                j += 1
                k -= 1
            elif s < 0:
                j += 1
            else:
                k -= 1
        return triplets