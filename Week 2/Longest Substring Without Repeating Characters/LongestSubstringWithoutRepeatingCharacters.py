class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        occurences = {}
        substr = ""
        for c in s:
            if c not in occurences:
                occurences[c] = True
                substr += c
                longest = max(len(substr), longest)
            else:
                ind = substr.index(c)+1
                if ind < len(substr):
                    substr = substr[ind:] + c
                else:
                    substr = c
                print(substr)
                occurences = {}
                for c in substr:
                    occurences[c] = True
        return longest
