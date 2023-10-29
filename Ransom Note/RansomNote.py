class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ranDict = {}
        magDict = {}
        for c in ransomNote:
            if c not in ranDict:
               ranDict[c] = 0
            else:
                ranDict[c] += 1
        for c in magazine:
            if c not in magDict:
               magDict[c] = 0
            else:
                magDict[c] += 1
        for l in ranDict:
            if l not in magDict:
                return False
            if magDict[l] < ranDict[l]:
                return False
        return True