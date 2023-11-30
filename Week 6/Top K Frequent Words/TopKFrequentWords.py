from collections import Counter, defaultdict
from typing import List


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wordCount = Counter(words)
        sortedDict = sorted(wordCount)
        sortedDict = sorted(wordCount.items(), key=lambda x:x[1], reverse=True)
        return [sortedDict[i][0] for i in range(k)]
        
        
        



solution = Solution()
words = ["i","love","leetcode","i","love","coding"]
k = 3
print(solution.topKFrequent(words, k))