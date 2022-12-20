class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict1 = {}
        for letter in s:
            dict1.setdefault(letter, 0)
            dict1[letter] += 1
        for index, letter in enumerate(s):
            if dict1[letter] == 1:
                return index
        return -1
