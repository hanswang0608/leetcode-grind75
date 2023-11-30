class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = self.helper(s)
        t = self.helper(t)
        return s == t

    def helper(self, s):
        i = 0
        while i < len(s):
            if s[i] == '#':
                l = 0
                if i > 0:
                    l = i - 1
                s = s[:l] + s[i+1:]
                i -= 1
                if i < 0:
                    i = 0
            else:
                i += 1
        return s