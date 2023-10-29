from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        m = {
            '2': ['a','b','c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r','s'],
            '8': ['t','u','v'],
            '9': ['w','x','y','z']
            }
        output = []
        def dfs(digits, output, path):
            if not digits:
                if path:
                    output.append(path)
                return
            for c in m[digits[0]]:
                dfs(digits[1:], output, path+c)
        dfs(digits, output, '')
        return output

solution = Solution()
digits = '23'
print(solution.letterCombinations(digits))