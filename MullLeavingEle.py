def mulltiplyLeavingEle(nums):
    
    res = [1]*len(nums)
    
    prefix = 1   
    for i in range(0,len(nums)):
        res[i] = prefix           #[1,1,2,6]
        prefix = prefix*nums[i]
        print("prefix: ",prefix)      
        
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        res[i] = res[i]*postfix   #[24,12,4,1]
        postfix = postfix*nums[i]
        print("postfix",postfix)
        
    return res

print(mulltiplyLeavingEle([1,2,3,4]))