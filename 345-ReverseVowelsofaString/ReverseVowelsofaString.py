class Solution(object):
    def reverseVowels(_self, _s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ["a", "e", "i", "o", "u"] + ["A", "E", "I", "O", "U"]
        lIndex = 0
        rIndex = len(_s) - 1
        lSB = ""
        rSB = ""
        if (len(_s) == 1):
            return _s
        while lIndex < rIndex:
            if _s[lIndex] in vowels and _s[rIndex] in vowels:
                lSB = lSB + _s[rIndex]
                rSB = _s[lIndex] + rSB
                lIndex += 1
                rIndex -= 1
            else:
                if _s[lIndex] not in vowels:
                    lSB = lSB + _s[lIndex]
                    lIndex += 1
                if _s[rIndex] not in vowels:
                    rSB = _s[rIndex] + rSB
                    rIndex -= 1
        if rIndex - lIndex == 0:
            lSB = lSB + _s[lIndex]
        return lSB + rSB
