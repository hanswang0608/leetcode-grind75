class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(filter(str.isalnum, s))
        for i in range(floor(len(s)/2)):
            if (s[i] != s[len(s)-i-1]):
                return False
        return True