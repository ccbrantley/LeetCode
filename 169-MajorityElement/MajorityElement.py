class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_count = {}
        for num in nums:
            nums_count[num] = nums_count.get(num, 0) + 1
        return max(nums_count.keys(), key = lambda k: nums_count[k])