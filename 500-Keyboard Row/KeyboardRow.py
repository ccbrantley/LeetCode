class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        rowDict = {
            'q' : 1,
            'w' : 1,
            'e' : 1,
            'r' : 1,
            't' : 1,
            'y' : 1,
            'u' : 1,
            'i' : 1,
            'o' : 1,
            'p' : 1,
            'a' : 2,
            's' : 2,
            'd' : 2,
            'f' : 2,
            'g' : 2,
            'h' : 2,
            'j' : 2,
            'k' : 2,
            'l' : 2,
            'z' : 3,
            'x' : 3,
            'c' : 3,
            'v' : 3,
            'b' : 3,
            'n' : 3,
            'm' : 3,
        }
        oneRowList = []
        for word in words:
            rowValue = rowDict.get(word[0].lower())
            for letter in word:
                if (rowDict.get(letter.lower()) != rowValue):
                    rowValue = -1
                    break
            if (rowValue > 0):
                oneRowList.append(word)
        return oneRowList
