class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        elif numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]
        else:
            triangle = [[1], [1, 1]]
            for row in range(3, numRows + 1):
                if row == 1:
                    triangle.append([1])
                elif row == 2:
                    triangle.append([1, 1])
                else:
                    newRow = [1]
                    values = triangle[-1]
                    for index in range(len(values) - 1):
                        newRow.append(values[index] + values[index + 1])
                    newRow.append(1)
                    triangle.append(newRow)
        return triangle
