#include <unordered_set>
class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        if (k == 0) {
            return false;
        }
        unordered_set<int> j;
        for (int i = 0; i < nums.size(); i++) {
            if (j.find(nums[i]) != j.end()) {
                return true;
            }
            else {
                if (i >= k) {
                    j.erase(nums[i - k]);
                }
            }
            j.insert(nums[i]);
        }
        return false;
    }
};