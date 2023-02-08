class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seenDict = {x : True for x in nums}
        unseenList = []
        for x in range(1, len(nums) + 1):
            value = seenDict.setdefault(x, False)
            if (not value):
                unseenList.append(x)
        return unseenList
