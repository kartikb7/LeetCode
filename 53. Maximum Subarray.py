class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start = 0
        end = 1
        left_index = start
        right_index = end
        max_sum = sum(nums[start:end])

        if nums == None:
            return 0

        for i in range(len(nums)):
            if sum(nums[start:end])+nums[i] < nums[i]:
                start = i
            end = i + 1

            if sum(nums[start:end]) > max_sum:
                max_sum = sum(nums[start:end])
                left_index = start
                right_index = end

        return sum(nums[left_index:right_index])

