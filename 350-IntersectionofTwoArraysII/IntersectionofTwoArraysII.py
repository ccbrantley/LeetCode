class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dict1 = {}
        for num in nums1:
            value = dict1.setdefault(num, 0)
            dict1[num] += 1
        dict2 = {}
        for num in nums2:
            value = dict2.setdefault(num, 0)
            dict2[num] += 1
        intersection = []
        for key in dict1.keys():
            value1 = dict1[key]
            value2 = dict2.setdefault(key, 0)
            if value2 < value1:
                for x in range(value2):
                    intersection.append(key)
            else:
                for x in range(value1):
                    intersection.append(key)
        return intersection
