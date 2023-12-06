class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        foundZero = False
        for num in nums:
            if num == 0 and not foundZero:
                foundZero = True
                continue
            product *= num
        for i in range(len(nums)):
            if nums[i] == 0 and foundZero:
                nums[i] = product
            elif foundZero:
                nums[i] = 0
            else:
                nums[i] = int(product / nums[i])
        return nums