class Solution(object):
    # WIP
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == None or len(num1) == 0:
            return num2
        if num2 == None or len(num2) == 0:
            return num1

        overhead = 0
        result = ''
        if len(num1) > len(num2):
            small_len = len(num2)
        else:
            small_len = len(num1)
        for i in range(small_len - 1, -1, -1):
            new_num = int(num1[i]) + int(num2[i]) + overhead
            if new_num > 10:
                overhead = 1
                new_num %= 10
            result = str(new_num) + result

        if small_len == len(num2):
            for i in range(len(num1) - 1, -1, -1):
                new_num = int(num1[i]) + overhead
            if new_num > 10:
                overhead = 1
                new_num %= 10
            result = str(new_num) + result
        else:

        return result