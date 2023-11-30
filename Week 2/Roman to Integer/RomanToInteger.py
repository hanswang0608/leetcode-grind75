class Solution:
    def romanToInt(self, s: str) -> int:
        sum = 0
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        for i in range(len(s)):
            if i+1 < len(s) and dict[s[i]] < dict[s[i+1]]:
                sum -= dict[s[i]]
            else:
                sum += dict[s[i]]
        return sum