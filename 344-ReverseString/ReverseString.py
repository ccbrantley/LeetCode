class Solution(object):
    def reverseString(_self, _s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        for index, value in enumerate(_s[::-1]):
            _s[index] = value
