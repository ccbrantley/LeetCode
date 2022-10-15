class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        indexOne = 0
        indexTwo = 0
        mergeCount = 0
        while indexTwo < n:
            if indexOne < m + mergeCount:
                if nums1[indexOne] < nums2[indexTwo]:
                    indexOne += 1
                elif nums1[indexOne] >= nums2[indexTwo]:
                    tempEltOne = nums1[indexOne]
                    tempEltTwo = nums1[indexOne + 1]
                    print(nums1)
                    for index in range(indexOne + 1, m + mergeCount + 1):
                        tempEltTwo = nums1[index]
                        nums1[index] = tempEltOne
                        tempEltOne = tempEltTwo
                    nums1[indexOne] = nums2[indexTwo]
                    indexOne += 1
                    indexTwo += 1
                    mergeCount += 1
                    print(nums1)
            else:
                nums1[indexOne] = nums2[indexTwo]
                mergeCount += 1
                indexOne += 1
                indexTwo += 1
