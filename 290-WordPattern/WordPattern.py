class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        mapping1 = {}
        mapping2 = {}
        wordBank = s.split(" ")
        if (len(pattern) != len(wordBank)):
            return False
        for index, word in enumerate(wordBank):
            value = mapping1.setdefault(pattern[index], word)
            if value != word:
                return False
            value = mapping2.setdefault(word, pattern[index])
            if (value != pattern[index]):
                return False
        return True
