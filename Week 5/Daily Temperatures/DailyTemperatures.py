from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        for i in range(len(temperatures)):
            foundHigher = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    foundHigher = j
                    break
            if foundHigher:
                output[i] = foundHigher-i
        return output
        
solution = Solution()
temperatures = [73,74,75,71,69,72,76,73]
print(solution.dailyTemperatures(temperatures))