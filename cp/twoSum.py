# Our functiion mainly takes two parameters: a list of integers and a target that we want to check
#in the outer loop, we loop from the first item to the last
    ##range(len(nums)) ===> i=0,i=1,i=2,i=3
    ##range(i+1,len(nums)) ===> j=1,j=2,j=3 (inner loop)
#range(): generates a sequence of numbers starting from 0 (by default), 
# and increments by 1 (also by default), until it reaches a specified upper bound (stop).
#we check the first element with the remaining elements ...

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if(nums[i] + nums[j] == target):
                    return [i,j]
         

