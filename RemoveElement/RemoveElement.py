class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        curIndex = 0
        while curIndex < len(nums):
            if nums[curIndex] == val:
                del nums[curIndex]
            else:
                curIndex += 1
