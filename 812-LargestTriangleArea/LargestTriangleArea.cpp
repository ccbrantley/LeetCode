class Solution {
public:
    double largestTriangleArea(vector<vector<int>>& points) {
        double max_area = -1;
        for (const auto& p1 : points) {
            double x1 = p1[0], y1 = p1[1];
            for (const auto& p2 : points) {
                double x2 = p2[0], y2 = p2[1];
                for (const auto& p3 : points) {
                    double x3 = p3[0], y3 = p3[1];
                    double cur_area = fabs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0;
                    if (max_area < cur_area) {
                        max_area = cur_area;
                    }
                }
            }

        }
        return max_area;
    }
};