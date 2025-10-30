double largestTriangleArea(int** points, int pointsSize, int* pointsColSize) {
    double max_area = -1;
    for (int p1 = 0; p1 < pointsSize; p1++) {
        double x1 = points[p1][0], y1 = points[p1][1];
        for (int p2 = 0; p2 < pointsSize; p2++) {
            double x2 = points[p2][0], y2 = points[p2][1];
            for (int p3 = 0; p3 < pointsSize; p3++) {
                double x3 = points[p3][0], y3 = points[p3][1];
                double cur_area = fabs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0;
                if (cur_area > max_area) {
                    max_area = cur_area;
                }
            }
        }
    }
    return max_area;
}