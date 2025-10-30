class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if len(nums) == 0:
            return []
        results = []
        left_num = nums[0]
        right_num = nums[0]
        prev_num = nums[0]
        for num in nums[1:]:
            if prev_num + 1 == num:
                right_num = num
            else:
                if left_num >= right_num:
                    results.append(str(left_num))
                else:
                    results.append(str(left_num) + "->" + str(right_num))
                left_num = num
            prev_num = num
        if left_num >= right_num:
            results.append(str(left_num))
        else:
            results.append(str(left_num) + "->" + str(right_num))
        return results