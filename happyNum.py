class Solution:
    def isHappy(self, n: int) -> bool:
        if n == 0:
            return -1

        out = set()
        num = n
        while n != 1:
            n = int(sum([math.pow(int(i), 2) for i in list(str(n))]))
            if n in out:
                return False
            out.add(n)

        return True

