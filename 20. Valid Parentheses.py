class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in '{([':
                stack.append(s[i])
            elif s[i] in '})]':
                temp = stack.pop() if stack else 'a'
                if temp != '(' and s[i] == ')':
                    return False
                elif temp != '{' and s[i] == '}':
                    return False
                elif temp != '[' and s[i] == ']':
                    return False
        return not stack
