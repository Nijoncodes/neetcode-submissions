class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
     # Get length of array from two for loops
     for i in range(len(nums)): # O(n2) Time complexity 
        for j in range(i + 1,len(nums)): # j is index postion 1
            added = nums[i] + nums[j]
            if added == target:
                return [i,j]
        
        