class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        total=0
        
        for i in range(k):
            total+=nums[i]
        ans=total/k
            


        for i in range(k,len(nums)):
            total=total-nums[i-k]
            total=total+nums[i] 

            avg=total/k

            if avg> ans:
                ans=avg

        return ans            