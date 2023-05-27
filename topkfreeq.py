from collections import Counter

def topKfreequency(nums,k):
    freeq = []
    countNum = Counter(nums)
    sortVall = set(sorted(countNum.values())[::-1][:k])
    for key in sortVall:
        print(countNum[key])
        if countNum[key] in sortVall:
            print(freeq)
            freeq.append(key)
    return freeq

topKfreequency([1,2,3,4],2)