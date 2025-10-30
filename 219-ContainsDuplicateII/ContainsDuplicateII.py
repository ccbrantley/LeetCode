class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0:
            return False
        j = set()
        for i in range(0, len(nums)):
            if nums[i] in j:
                return True
            else:
                if i >= k:
                    j.discard(nums[i - k])
            j.add(nums[i])
        return False