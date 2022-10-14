class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        lengths = [len(x) for x in strs]
        minLength = lengths[0]
        for x in range(len(lengths)):
            if lengths[x] < minLength:
                minLength = lengths[x]
        if (minLength == 0):
            return ""
        minLength = lengths.index(minLength)

            
        theWord = strs[minLength]
        strs.remove(theWord)
        prefix = ""
        endFlag = 0
        for x in range(len(theWord)):
            for word in strs:
                if (theWord[x] != word[x]):
                    endFlag = 1
                    break
            if (endFlag):
                break
            else:
                prefix += (theWord[x])
        return prefix
