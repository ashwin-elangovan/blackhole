# Implement strStr()
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle)+1): # Index - Beginning of haystack to the point (end - length of needle)
            if haystack[i:i+len(needle)] == needle: # Check if haystack range value == needle
                return i
        return -1