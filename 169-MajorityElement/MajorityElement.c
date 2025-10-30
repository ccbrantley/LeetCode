int majorityElement(int* nums, int numsSize) {
    int cur_major = nums[0], cur_count = 1;
    for (int x = 1; x < numsSize; x++){
        if (nums[x] == cur_major) {
            cur_count +=1;
        }
        else {
            cur_count -=1;
            if (cur_count < 1) {
                cur_major = nums[x];
                cur_count = 1;
            }
        }
    }
    return cur_major;
}