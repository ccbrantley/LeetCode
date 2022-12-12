class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for index in range(len(nums))[::-1]:
            if nums[index] == 0:
                del nums[index]
                nums.append(0)
