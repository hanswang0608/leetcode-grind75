class Solution:
    def longestPalindrome(self, s: str) -> int:
        m = {}
        for c in s:
            if c not in m:
                m[c] = 1
            else:
                m[c] += 1
        output = 0
        hasOdd = False
        for c in m:
            if m[c] % 2 == 0:
                output += m[c]
            else:
                hasOdd = True
                output += m[c] - 1
        if hasOdd:
            output += 1
        return output