class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -1
        j=0
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                continue
            else:
                nums[j]=nums[i]
                j+=1
        if len(nums) != 1:
            nums[j] = nums[i+1]
        return j+1