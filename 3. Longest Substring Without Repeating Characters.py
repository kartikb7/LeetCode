class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is None:
            return s
        if len(s) <= 1:
            return len(s)
        substring = s[0]
        max_string = len(substring)
        for i in range(1,len(s)):
            if s[i] in substring:
                substring = substring.split(s[i],1)[1]
            substring += s[i]
            if len(substring) > max_string:
                max_string = len(substring)
        return max_string