class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        spaceFlag = False
        continueFlag = True
        index = len(s) - 1
        length = 0
        while continueFlag:
            if index == -1:
                continueFlag = False
            elif s[index] == " ":
                index -= 1
                if spaceFlag:
                    break
            else:
                index -= 1
                length += 1
                spaceFlag = True
        return length
