class NumArray(object):

    def __init__(_self, _nums):
        """
        :type nums: List[int]
        """
        _self.nums = _nums
        

    def sumRange(_self, _left, _right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        return sum(_self.nums[_left:_right + 1:1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
