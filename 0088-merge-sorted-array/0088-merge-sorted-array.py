class Solution:
    def merge(self, nums1, m, nums2, n):
        list= []

        for i in range(m):
            list.append(nums1[i])

        for i in range(n):
            list.append(nums2[i])

        list.sort()

        for i in range(m + n):
            nums1[i] = list[i]