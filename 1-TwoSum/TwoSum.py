class Solution(object):
    """
    :type nums: List[int] -> array of integers
    :type target: int
    :rtype: List[int]
    """
    def linearSort(nums):
        curValue = nums[0]
        change = True
        while (change):
            change = False
            for index0 in range(len(nums) - 1):
                if (nums[index0] > nums[index0 + 1]):
                    temp = nums[index0]
                    nums[index0] = nums[index0 + 1]
                    nums[index0 + 1] = temp
                    change = True

    def twoSum(self, nums, target):
        solution = []
        for index0 in range(len(nums)):
            for index1 in range(index0 + 1, len(nums)):
                if ((nums[index0] + nums[index1]) == target):
                    solution.append(index0)
                    solution.append(index1)
        return solution
