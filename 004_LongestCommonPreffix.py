'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"'''

def longestCommonPrefix(strs) -> str:

        prefix = strs[0]

        for i in range(1,len(strs)):
            if strs[i].islower():
                    while not strs[i].startswith(prefix):
                        prefix = prefix[:-1]
                        if not prefix:
                            return ""
        return prefix

print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
