from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedStrs = []
        for i in range(len(strs)):
            sortedStrs.append((''.join(sorted(strs[i])), i))
        sortedStrs.sort()
        output = [[strs[sortedStrs[0][1]]]]
        for i in range(1, len(sortedStrs)):
            s, j = sortedStrs[i]
            if s != sortedStrs[i-1][0]:
                output.append([strs[j]])
            else:
                output[-1].append(strs[j])
        return output


solution = Solution()
strs = ["eat","tea","tan","ate","nat","bat"]
print(solution.groupAnagrams(strs))