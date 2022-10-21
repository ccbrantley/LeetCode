class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        else:
            newRow = [1, 1]
            for x in range(rowIndex - 1):
                row = newRow
                newRow = [1]
                for index in range(len(row) - 1):
                    newRow.append(row[index] + row[index + 1])
                newRow.append(1)
            return newRow
                
                
