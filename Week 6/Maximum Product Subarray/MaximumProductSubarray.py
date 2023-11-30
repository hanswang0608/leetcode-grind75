from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        negCount = 0
        product = 1
        firstNeg = lastNeg = None
        maxProduct = float('-inf')
        seenNumber = False
        for num in nums:
            if num == 0:
                product = 1
                maxProduct = max(maxProduct, 0)
                firstNeg = lastNeg = None
                negCount = 0
                seenNumber = False
                continue
            product *= num
            if lastNeg:
                lastNeg *= num
            if num < 0:
                negCount += 1
                if not firstNeg:
                    firstNeg = product
                lastNeg = num
            else:
                seenNumber = True
            p1 = product/firstNeg if firstNeg else float('-inf')
            p2 = product/lastNeg if lastNeg else float('-inf')
            maxProduct = max(maxProduct, product)
            if seenNumber or negCount > 2:
                maxProduct = max(maxProduct, product, p1, p2)
            print(product, firstNeg, lastNeg, p1, p2)
        return int(maxProduct)

solution = Solution()
nums = [-2,0,-1]
nums = [-3,0,1,-2]
nums = [2,-5,-2,-4,3]
nums = [-1,-2,-9,-6]
nums = [2,2,-5,2,2,-4,2,2,-3,2,2]
nums = [2,3,-2,4]
nums = [-2,3,-4]
nums = [-2]
nums = [1,0,-1,2,3,-5,-2]
print(solution.maxProduct(nums))