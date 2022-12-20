class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = {num : 0 for num in nums1}
        dict2 = {num : 0 for num in nums2}
        return [key for key in dict1.keys() if dict2.setdefault(key, 1) == 0]
