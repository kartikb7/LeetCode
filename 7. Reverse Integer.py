class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == None:
            return 0

        isNegative = False
        if x < 0:
            isNegative = True

        newNum = int(str(abs(x))[::-1])
        if not isNegative and newNum > pow(2, 31) - 1:
            return 0
        if isNegative and newNum > pow(2, 31):
            return 0

        if isNegative:
            return '-' + str(newNum)
        else:
            return str(newNum)

