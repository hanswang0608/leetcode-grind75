from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        p1 = p2 = p3 = n1 = n2 = 1
        maxProduct = 0
        for num in nums:
            if num < 0:
                p3 = p2
                p2 = p1
                p1 = 1
                n2 = n1
                n1 = num
            else:
                p1 *= num
            maxProduct = max(p1, p2, p3, p1*p2*p3*n1*n2, maxProduct)
        return maxProduct
    
        # negCountArr = [0] * len(nums)
        # negCount = 0
        # for i in reversed(range(len(nums)-1)):
        #     if nums[i+1] < 0:
        #         negCount += 1
        #     negCountArr[i] = negCount
        # print(negCountArr)

        # intervalStart = 0
        # negCount = 0
        # possibleIntervals = []
        # for i in range(len(nums)):
        #     if nums[i] < 0:
        #         negCount += 1
        #     elif nums[i] > 0:
        #         possibleIntervals.append((intervalStart, i))
        #     if negCount == 2:
        #         possibleIntervals.append((intervalStart, i))
        #         intervalStart = i
        #         negCount = 1
        #     elif negCount == 1:
        #         possibleIntervals.append((intervalStart, i-1))
        # print(possibleIntervals)
                

        # maxProduct = curProduct = nums[0]
        # for i in range(1, len(nums)):
        #     if negCountArr[i] % 2 == 1 and curProduct * nums[i] < 0:
        #         curProduct = curProduct * nums[i]
        #     else:
        #         curProduct = max(curProduct * nums[i], nums[i])
        #     maxProduct = max(maxProduct, curProduct)
        # return maxProduct

solution = Solution()
nums = [2,3,-2,4]
nums = [-2,3,-4]
nums = [2,2,-5,2,2,-4,2,2,-3,2,2]
nums = [2,-5,-2,-4,3]
print(solution.maxProduct(nums))