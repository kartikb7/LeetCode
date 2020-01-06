class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0

        if n % 2 == 0:
            maxTwoCoins = n / 2
        else:
            maxTwoCoins = (n - 1) / 2

        solution = 0
        for i in range(int(maxTwoCoins) + 1):
            solution = solution + math.factorial(n - i) / (math.factorial(n - 2 * i) * math.factorial(i))

        return int(solution)