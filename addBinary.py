class Solution:
    def addBinary(self, a: str, b: str) -> str:

        binDec = 0
        for i in range(len(a)):
            binDec += int(a[::-1][i]) * math.pow(2, i)

        binDec2 = 0
        for i in range(len(b)):
            binDec2 += int(b[::-1][i]) * math.pow(2, i)

        binSum = binDec + binDec2
        print(binDec)
        print(binDec2)
        result = ""
        if binSum == 0:
            result = "0"

        while (binSum > 0):
            result += str(int(binSum % 2))
            binSum = (binSum - binSum % 2) / 2

        return result[::-1]

# Doesn't give the correct answer for large binary numbers