class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 1
        index = len(digits) - 1
        while carry:
            indexValue = digits[index] + carry
            digits[index] = indexValue % 10
            carry = indexValue // 10
            if index == 0 and carry:
                digits.insert(0, 0)
            else:
                index -= 1
        return digits
