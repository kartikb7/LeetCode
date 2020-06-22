class Solution:
    def isUgly(self, num: int) -> bool:
        if num <= 0:
            return False

        if num == 1:
            return True

        for val in [2, 3, 5]:
            while num % val == 0:
                num = num / val

        return num == 1