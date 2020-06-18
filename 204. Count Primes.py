class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        prime_numbers = [2]
        count = 1

        for i in range(3, n, 2):
            prime = True
            for j in prime_numbers:
                if j > i ** 0.5 + 1:
                    break
                if i % j == 0:
                    prime = False

            if prime:
                prime_numbers.append(i)
                count += 1

        return count