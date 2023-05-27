#Re-revise this... I am not understanding this clearly
def temperatures(temps):
    
    stack = []
    res = [0]*len(temps)
    
    for i,t in enumerate(temps):
        while stack and t>stack[-1][0]:
            stackT , stackInd = stack.pop()
            res[stackInd] = i - stackInd
        stack.append((t,i))
    return res

print(temperatures([73,74,75,71,69,72,76,73]))