from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(cost) > sum(gas):
            return -1
        start = tank = 0
        for i in range(len(gas)):
            difference = gas[i] - cost[i]
            tank += difference
            if tank < 0:
                tank = 0
                start = i + 1
        return start


            
solution = Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]
# gasUponReachingStation = [0, -2, -4, -6, -3]
# gas/cost difference = [-2, -2, -2, 3, 3]
print(solution.canCompleteCircuit(gas, cost))


gas =  [10, 0, 5]
cost = [1, 10, 4]
# gasUponReachingStation = [0, 9, -1]
# gas/cost difference = [9, -10, 1]

gas = [5,1,2,3,4]
cost = [4,4,1,5,1]
# gas/cost difference = [1, -3, 1, -2, 3]
# [1, -3, 1, -2, 3 | 1, -3, 1, -2]

