class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c == ')' or c == ']' or c == '}':
                if not stack:
                    return False
                popped = stack.pop()
                if (popped == None):
                    return False
                if (c == ')' and popped != '('):
                    return False
                elif (c == ']' and popped != '['):
                    return False
                elif (c == '}' and popped != '{'):
                    return False
            else:
                stack.append(c)
        if stack:
            return False
        return True