def groupAnagrams(strs):
    ans = {}

    for words in strs:
        key = ''.join(sorted(words))
        if key in ans:
            ans[key].append(words)
        else:
            ans[key] = [words]

    return ans.values()
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
