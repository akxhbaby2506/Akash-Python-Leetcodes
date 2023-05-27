# Longest Substring without repetition
"""
def subStr(s):
    s = set(s)
    return len(s)

print(subStr("abcabcbb"))
"""

def substring(s):
    
    charSet = set()
    l = 0
    result = 0
    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l = l + 1

        charSet.add(s[r])
        result = max(result,r-l+1)
        
    return result

print(substring("abcabcbb"))

# The below one is of leetcodes code
# def lengthOfLongestSubstring(s):
#     charSet = set()
#     l = 0
#     res = 0
    
#     for r in range(len(s)):
#         while s[r] in charSet:
#             charSet.remove(s[l])
#             l += 1
#         charSet.add(s[r])
#         res = max(res, r - l + 1)
#     return res
# print(lengthOfLongestSubstring("aaabbbccc"))
