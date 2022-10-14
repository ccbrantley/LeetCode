class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) != 1:
            curNum = nums[0]
            curIndex = 1
            while True:
                while curNum == nums[curIndex]:
                    del nums[curIndex]
                    if curIndex == len(nums):
                        break
                if curIndex == len(nums):
                    break
                curNum = nums[curIndex]
                curIndex += 1
                if curIndex == len(nums):
                    break
