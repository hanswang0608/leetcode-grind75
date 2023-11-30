class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = float('inf')
        for str in strs:
            if len(str) < shortest:
                shortest = len(str)
        i = 0
        output = ''
        while i < shortest:
            c = strs[0][i]
            for str in strs:
                if str[i] != c:
                    return output
            output += strs[0][i]
            i += 1
        return output