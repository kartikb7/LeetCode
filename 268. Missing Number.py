class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None:
            return None
        end = max(nums)
        if end + 1 == len(nums):
            end += 1
        nums.sort()

        for i in range(0, end):
            if i != nums[i]:
                return i

        return i + 1