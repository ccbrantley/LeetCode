class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        dict1 = {}
        for letter in magazine:
            value = dict1.setdefault(letter, 0)
            dict1[letter] += 1
        for letter in ransomNote:
            value = dict1.setdefault(letter, 0)
            dict1[letter] -= 1
            if value < 1:
                return False
        return True
