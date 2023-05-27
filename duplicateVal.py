def duplicate(nums):
    
    hashmaps = set()
    
    for i in nums:
        if i in hashmaps:
            return True
        
        hashmaps.add(i)
    return False

print(duplicate([1,2,3,1]))

def containDuplicate(nums):
    
    s = set(nums)
    l1 = len(nums)
    l2 = len(s)
    
    if l1 != l2:
        print("Has duplicate values")
    else:
        print("No duplicate values")
containDuplicate([1,2,3,1])
containDuplicate([1,3,5,7])
containDuplicate([2,4,6,8,6])
    