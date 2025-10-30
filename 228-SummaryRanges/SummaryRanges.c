/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
char** summaryRanges(int* nums, int numsSize, int* returnSize) {
    if (numsSize == 0) {
        *returnSize = 0;
        return NULL;
    }
    char** results = malloc(numsSize * sizeof(char*));
    int resultSize = 0;
    int left_num = nums[0];
    int right_num = nums[0];
    int prev_num = nums[0];
    for (int x = 1; x < numsSize; x++) {
        if (prev_num + 1 == nums[x]) {
            right_num = nums[x];
        }
        else {
            char buffer[50];
            if (left_num >= right_num) {
                sprintf(buffer, "%d", left_num);
            }
            else {
                sprintf(buffer, "%d->%d", left_num, right_num);
            }
            results[resultSize] = malloc(strlen(buffer) + 1);
            strcpy(results[resultSize], buffer);
            resultSize += 1;
            left_num = nums[x];
        }
        prev_num = nums[x];
    }
    char buffer[50];
    if (left_num >= right_num) {
        sprintf(buffer, "%d", left_num);
    }
    else {
        sprintf(buffer, "%d->%d", left_num, right_num);
    }
    results[resultSize] = malloc(strlen(buffer) + 1);
    strcpy(results[resultSize], buffer);
    resultSize += 1;
    *returnSize = resultSize;
    return results;
}