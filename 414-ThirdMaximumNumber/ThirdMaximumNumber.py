class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if (len(nums) == 1):
            return nums[0]
        if (len(nums) == 2):
            return nums[0] if nums[0] > nums[1] else nums[1]
        firstMax = None
        secondMax = None
        thirdMax = None
        for x in range(len(nums)):
            if (firstMax == nums[x]):
                continue
            elif (secondMax == nums[x]):
                continue
            elif (nums[x] > firstMax):
                thirdMax = secondMax
                secondMax = firstMax
                firstMax = nums[x]
            elif (nums[x] > secondMax):
                thirdMax = secondMax
                secondMax = nums[x]
            elif (nums[x] > thirdMax):
                thirdMax = nums[x]
        if (thirdMax != None):
            return thirdMax
        else:
            return firstMax
