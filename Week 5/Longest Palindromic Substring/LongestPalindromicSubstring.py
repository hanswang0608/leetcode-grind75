class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == '':
            return ''
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        longest = [0,0]
        for r in range(len(s)):
            for l in range(r-1, -1, -1):
                if s[l] == s[r]:
                    if r-l < 3 or dp[l+1][r-1]:
                        dp[l][r] = True
                        if r-l > longest[1]-longest[0]:
                            longest = [l,r]
        return s[longest[0]:longest[1]+1]
                        
                    

solution = Solution()
s = "bacabad"
print(solution.longestPalindrome(s))