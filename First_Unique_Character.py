class Solution:
    def firstUniqChar(self, s: str) -> int:
        charDict = {}

        for i in range(len(s)):
            if s[i] in charDict.keys():
                charDict[s[i]] += 1
            else:
                charDict[s[i]] = 1

        for k in charDict.keys():
            if charDict[k] == 1:
                return s.find(k)

        return -1