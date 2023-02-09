class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bX = bin(x)[2:]
        bY = bin(y)[2:]
        bX = "0" * (len(bY) - len(bX)) + bX
        bY = "0" * (len(bX) - len(bY)) + bY
        dCount = 0
        for idx in range(len(bX)):
            if bX[idx] != bY[idx]:
                dCount += 1
        return dCount
