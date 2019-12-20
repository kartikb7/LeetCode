class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        if len(A) < 3:
            return True

        monIncrease = True
        for i in range(len(A) - 1):
            if (A[i] > A[i + 1]):
                monIncrease = False

        monDecrease = True
        for i in range(len(A) - 1):
            if (A[i] < A[i + 1]):
                monDecrease = False

        if monIncrease or monDecrease:
            return True
        else:
            return False