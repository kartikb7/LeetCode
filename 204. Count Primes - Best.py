class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        prime_numbers = [1] * n
        prime_numbers[0] = prime_numbers[1] = 0

        for i in range(2, int(n ** 0.5) + 1):
            if prime_numbers[i] == 1:
                for j in range(i * i, n, i):
                    prime_numbers[j] = 0

        return sum(prime_numbers)