from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        largestStart = curStart = 0
        largestSum = curSum = gas[0]-cost[0]
        for i in range(1, len(gas)*2-1):
            j = i % len(gas)
            difference = gas[j]-cost[j]
            if curSum + difference > difference:
                curSum += difference
            else:
                curStart = j
                curSum = difference
            if curSum > largestSum:
                largestSum = curSum
                largestStart = curStart
        return largestStart

            
solution = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
# gasUponReachingStation = [0, -2, -4, -6, -3]
# gas/cost difference = [-2, -2, -2, 3, 3]


gas =  [10, 0, 5]
cost = [1, 10, 4]
# gasUponReachingStation = [0, 9, -1]
# gas/cost difference = [9, -10, 1]
print(solution.canCompleteCircuit(gas, cost))

gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
# gas/cost difference = [1, -3, 1, -2, 3]
# [1, -3, 1, -2, 3 | 1, -3, 1, -2]

