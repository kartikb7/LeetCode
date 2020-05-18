class Solution:
    def addBinary(self, a: str, b: str) -> str:

        binDec = 0
        for i in range(len(a)):
            binDec += int(a[::-1][i]) * int(math.pow(2, i))

        binDec2 = 0
        for i in range(len(b)):
            binDec2 += int(b[::-1][i]) * int(math.pow(2, i))

        binSum = binDec + binDec2

        result = ""
        if binSum == 0:
            result = "0"

        while (binSum > 0):
            result += str(binSum % 2)
            binSum = binSum//2

        return result[::-1]
