class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return -1
        elif len(s) == 1:
            return True
        else:
            s = s.lower()
            clearString = ''

            for i in range(len(s)):
                if re.match(r'[a-zA-Z0-9]', s[i]):
                    clearString += s[i]

            palindrome = True
            for i in range(len(clearString) // 2):
                if clearString[i] != clearString[-1 - i]:
                    palindrome = False
            return palindrome
