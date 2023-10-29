from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strDict = {}

        for str in strs:
            sortedStr = ''.join(sorted(str))
            if sortedStr not in strDict:
                strDict[sortedStr] = []
            strDict[sortedStr].append(str)
        
        return list(strDict.values())



solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(strs))