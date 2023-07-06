class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        nC = 0
        if len(word) == 1:
            return True
        for letter in word:
            if letter.isupper():
                nC += 1
        if nC < len(word):
            if nC == 1 and word[0].isupper():
                return True
            elif nC == 0:
                return True
        elif nC == len(word):
            return True
