class Solution {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> counter;
        for (const auto& num : nums) {
            counter[num]++;
        }
        int max_key = -1;
        int max_value = -1;
        for (const auto& [key, value] : counter) {
            if (value > max_value) {
                max_key = key;
                max_value = value;
            }
        }
        return max_key;
    }
};