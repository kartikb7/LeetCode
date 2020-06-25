class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        val = -1
        for i in range(0, len(nums), 2):
            if i != len(nums) - 1:
                if nums[i] != nums[i + 1]:
                    val = i
                    break
            else:
                val = i
        return nums[val]
