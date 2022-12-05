class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        columnValue = ord(columnTitle[-1]) - 64
        columnTitle = columnTitle[0:-1]
        place = 1
        while columnTitle != "":
            value = (ord(columnTitle[-1]) - 64) * (26 ** place)
            columnTitle = columnTitle[0:-1]
            columnValue += value
            place += 1
        return columnValue
