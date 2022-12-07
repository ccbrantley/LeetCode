class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        myDict = {}
        for x in nums:
            myDict[x] = 0
        for x in nums:
            myDict[x] += 1
            if(myDict[x] > 1):
                return True
        return False
