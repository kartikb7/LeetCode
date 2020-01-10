class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        solution = []

        for i in range(0, len(nums) - 2):
            if i == 0 or nums[i] != nums[i - 1]:
                low = i + 1
                high = len(nums) - 1
                target = 0 - nums[i]
                while low < high:
                    if nums[low] + nums[high] == target:
                        smallSol = [nums[i], nums[low], nums[high]]
                        solution.append(smallSol)
                        low += 1
                        high -= 1
                        while nums[low] == nums[low - 1] and low < high:
                            low += 1
                        while nums[high] == nums[high + 1] and low < high:
                            high -= 1
                    elif nums[low] + nums[high] > target:
                        high -= 1
                    else:
                        low += 1

        return solution
