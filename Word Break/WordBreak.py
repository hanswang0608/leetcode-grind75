from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = {}
        def helper(s):
            if s in dp:
                return dp[s]
            if s == '':
                return True
            for word in wordDict:
                if (s.startswith(word) and helper(s[len(word):])) or (s.endswith(word) and helper(s[:-len(word)])):
                    dp[s] = True
                    return True
            dp[s] = False
            return False
        return helper(s)
    
solution = Solution()
s = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab'
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
s1 = 'leetcode'
wordDict1 = ['leet', 'code']
print(solution.wordBreak(s, wordDict))