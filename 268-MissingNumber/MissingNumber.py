class Solution(object):

    def missingNumber(_self, _nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        _self.quickSort(_nums)
        counter = 0
        for num in _nums:
            if counter != num:
                return counter
            counter += 1
        return _nums[-1] + 1

    def partition (_self, _nums, _low, _high):
        pivotValue = _nums[_high]
        lessIndex = _low
        for index in range(_low, _high):
            if (_nums[index] < pivotValue):
                tempElt = _nums[lessIndex]
                _nums[lessIndex] = _nums[index]
                _nums[index] = tempElt
                lessIndex += 1
        tempElt = _nums[lessIndex]
        _nums[lessIndex] = _nums[_high]
        _nums[_high] = tempElt
        return lessIndex

    def quickSort (_self, _nums):
        indices = [0, len(_nums) - 1]
        while indices != []:
            low = indices.pop(0)
            high = indices.pop(0)
            pivot = _self.partition(_nums, low, high)
            if (pivot - 1 > low):a
                indices.extend([low, pivot - 1])
            if (pivot + 1 < high):
                indices.extend([pivot + 1, high])
