class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        leftIndex = 0
        rightIndex = len(s) - 1
        while leftIndex < rightIndex:
            if not s[leftIndex].isalnum():
                leftIndex += 1
                continue
            if not s[rightIndex].isalnum():
                rightIndex -= 1
                continue
            if s[leftIndex].lower() != s[rightIndex].lower():
                return False
            else:
                leftIndex += 1
                rightIndex -= 1
        return True
