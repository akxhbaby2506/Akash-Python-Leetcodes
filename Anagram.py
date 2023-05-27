def isAnagram(s,t):
    # code with least run time
    if (len(s)!=len(t)):
        return False

    letters = "abcdefghijklmnopqrstuvwxyz"
    for letter in letters:
        if (s.count(letter) != t.count(letter)):
            return False
    else:
            return True
print(isAnagram("anagram","ramaang"))
print(isAnagram("car","rat"))

#code-2
# if(sorted(s) != sorted(t)):
#     return False

#code-3
# 