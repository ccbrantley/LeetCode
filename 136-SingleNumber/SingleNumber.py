class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        minOfNum = min(nums)
        maxOfNum = max(nums)
        countOfNumDict = {x : 0 for x in range(minOfNum, maxOfNum + 1)}
        for num in nums: countOfNumDict[num] += 1
        for num in nums:
            if countOfNumDict[num] == 1:
                return num
