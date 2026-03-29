from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
    
        max_sum = total_sum = nums[0]
        
        for i in range(1,len(nums)):
            
            total_sum = max(nums[i],total_sum+nums[i])
            max_sum = max(max_sum,total_sum) 
            
            
        return max_sum
            
sol = Solution()
num = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(num)
            