class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i in range(len(nums)):
            if (i > 0):
                diff = (target - nums[i])
                if (not dic.get(diff) == None):
                    return [dic.get(diff), i]
            dic[nums[i]] = i