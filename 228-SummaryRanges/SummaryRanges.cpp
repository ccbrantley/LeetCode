class Solution {
public:
    vector<string> summaryRanges(vector<int>& nums) {
        if (nums.size() == 0) {
            return {};
        }
        vector<string> results;
        int left_num = nums[0];
        int right_num = nums[0];
        int prev_num = nums[0];
        for (int x = 1; x < nums.size(); x++) {
            if (prev_num + 1 == nums[x]) {
                right_num = nums[x];
            }
            else {
                if (left_num >= right_num) {
                    results.push_back(to_string(left_num));
                }
                else {
                    results.push_back(to_string(left_num) + "->" + to_string(right_num));
                }
                left_num = nums[x];
            }
            prev_num = nums[x];
        }
        if (left_num >= right_num) {
            results.push_back(to_string(left_num));
        }
        else {
            results.push_back(to_string(left_num) + "->" + to_string(right_num));
        }
        return results;
    }
};
