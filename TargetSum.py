class Solution:
    def twoSum(self, nums, target):
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if target == nums[i]+nums[j]:
                    print([i,j])
                    print(nums[i],",",nums[j])
                
s = Solution()
s.twoSum([2,5,7,8],9)
