class Solution:
    def absDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        smallest=0
        largest=0
        for i in range(k):
            smallest+=nums[i]

        for j in range(len(nums)-k ,len(nums)) :
            largest+=nums[j]


        diff=abs(largest-smallest)

        return diff    
