class Solution:
    def myAtoi(self, s: str) -> int:
        i = 0
        neg = False
        num = 0

        def whitespace(s):
            nonlocal i
            while i < len(s) and s[i] == ' ':
                i += 1
        def sign(s):
            nonlocal i, neg
            if i >= len(s):
                return
            if s[i] == '-':
                neg = True
                i += 1
            elif s[i] == '+':
                i += 1
        def number(s):
            nonlocal i, neg, num
            numStr = ''
            while i < len(s) and 48 <= ord(s[i]) <= 57:
                numStr += s[i]
                i += 1
            for power, digit in enumerate(reversed(numStr)):
                num += (ord(digit)-48) * 10**power
            if neg:
                num = -num
            num = max(-2**31, num)
            num = min(2**31-1, num)
        
        whitespace(s)
        sign(s)
        number(s)
        return num

solution = Solution()
print(solution.myAtoi('12349812374981237442'))