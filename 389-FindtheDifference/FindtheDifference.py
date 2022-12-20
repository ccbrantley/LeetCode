class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dict1 = {}
        for letter in s:
            dict1.setdefault(letter, 0)
            dict1[letter] += 1
        for letter in t:
            dict1.setdefault(letter, 0)
            dict1[letter] -= 1
            if dict1[letter] < 0:
                return letter
        return None
