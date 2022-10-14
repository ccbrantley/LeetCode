class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lowerIndex = 0
        upperIndex = len(nums) - 1
        midpoint = 0
        while upperIndex >= lowerIndex:
            midpoint = (upperIndex + lowerIndex) // 2
            if nums[midpoint] > target:
                upperIndex = midpoint - 1
            elif nums[midpoint] < target:
                lowerIndex = midpoint + 1
            else:
                break
        if nums[midpoint] >  target:
            return (midpoint)
        elif nums[midpoint] < target:
            return (midpoint + 1)
        else:
            return (midpoint)
