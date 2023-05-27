#This method evokes palindromes ignoring the spcl case charcters
def palindrome1(s):

    newStr = ""

    for i in s:
        if i.isalnum():
            newStr = newStr + i.lower()
    return newStr==newStr[::-1]
print(palindrome1("A man, a plan, a canal: Panama"))
#This above sol takes more time complevity
#The following code gives us a lessser ti,e complexity

def palindrome2(s):
    
    l = 0
    r = len(s)-1
    
    while l<r:
        while l<r and not alphaNum(s[l]):
            l = l+1
        while r>l and not alphaNum(s[r]):
            r = r-1
        if s[l].lower() != s[r].lower():
            return False
        l = l+1
        r = r-1
    return True
    
    
def alphaNum(c):                #ord("value") --> gives the ASCII value of the value,... This helps to return only the alpha numeric values of the function
    return ((ord("A")) <= ord(c) <= ord("Z") or
            (ord("a")) <= ord(c) <= ord("z") or
            (ord("0")) <= ord(c) <= ord("9"))
    
print(palindrome2("A man, a plan, a canal: Panama"))