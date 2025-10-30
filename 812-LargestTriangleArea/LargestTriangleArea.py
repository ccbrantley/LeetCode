class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max_area = -1
        for x in points:
            x1, y1 = x[0], x[1]
            for y in points:
                x2, y2 = y[0], y[1]
                for z in points:
                    x3, y3 = z[0], z[1]
                    area = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
                    if area > max_area:
                        max_area = area
        return max_area