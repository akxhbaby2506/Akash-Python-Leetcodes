#def maxArea(height):
#    
#    result = 0
#    
#    for left in range(len(height)):
#        for right in range(left+1,len(height)):
#            
#            area = (right-left) * min(height[left],height[right])
#            result = max(result,area)
#    return result
#
#print(maxArea([1,8,6,2,5,4,8,3,7]))
#This above problem takes more time to execute - O(n^2)
#Below takes lesser time
def maxyyArea(height):
    
    result = 0
    left = 0
    right = len(height)-1
    
    while(left<right):
        area = (right-left)*min(height[left],height[right])
        result = max(result,area)
        
        if (height[left]<height[right]):
            left = left + 1
        else:
            right = right - 1
            
    return result
            
print(maxyyArea([1,8,6,2,5,4,8,3,7]))
