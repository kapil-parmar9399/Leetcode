class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = []

        for i in nums1:
            new.append(i)

        for i in nums2:
            new.append(i)

        new.sort()

        n = len(new)

        if n % 2 == 1:
            return new[n // 2]
        else:
            return (new[n // 2 - 1] + new[n // 2]) / 2