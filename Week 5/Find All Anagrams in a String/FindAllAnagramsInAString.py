from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        start, end = 0, len(p)
        output = []
        pCount = Counter(p)
        windowCount = {}
        while end <= len(s):
            if not windowCount:
                windowCount = Counter(s[start:end])
            else:
                if s[end-1] not in windowCount:
                    windowCount[s[end-1]] = 0
                windowCount[s[end-1]] += 1
                windowCount[s[start-1]] -= 1
            if windowCount == pCount:
                output.append(start)
            start += 1
            end = start + len(p)
            
        return output
    
solution = Solution()
s = "cbaebabacd"
p = "abc"
print(solution.findAnagrams(s, p))