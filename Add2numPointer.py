def twoSumPointer(l,target):
    
    beg = 0
    end = len(l)-1
    
    while(beg<end):
        
        currSum = l[beg]+l[end]
        
        if (currSum>target):
            end = end-1
        elif (currSum<target):
            beg = beg+1
        else:
            return [beg,end]
            
print(twoSumPointer([2,7,11,13],9))
print(twoSumPointer([2,7,11,13],24))
print(twoSumPointer([2,7,11,13],20))
print(twoSumPointer([2,7,11,13],15))