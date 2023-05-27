def twoSum(l,target):
    
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if(l[i]+l[j])==target:
                return [i,j]
            
print(twoSum([2,7,11,13],13))