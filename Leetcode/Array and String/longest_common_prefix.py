# Problem Statement: Longest Common Prefix

# Write a Python class Solution that implements a method longestCommonPrefix, which takes a list of strings strs as input and returns the longest common prefix among them.

# Method Signature:

# Input:

# strs (1 <= len(strs) <= 200): A list of strings where each string consists of lowercase English letters.

# Output:

# Returns a string, representing the longest common prefix among the given strings.
# If there is no common prefix, an empty string ("") is returned.
# Example:

# python
# Copy code
# solution = Solution()

# # Example 1
# input_strs_1 = ["flower", "flow", "flight"]
# output_1 = solution.longestCommonPrefix(input_strs_1)
# # Output: "fl"

# # Example 2
# input_strs_2 = ["dog", "racecar", "car"]
# output_2 = solution.longestCommonPrefix(input_strs_2)
# # Output: ""

# # Example 3
# input_strs_3 = ["apple", "ape", "apricot"]
# output_3 = solution.longestCommonPrefix(input_strs_3)
# # Output: "ap"
# Explanation:

# In Example 1, the longest common prefix is "fl".
# In Example 2, there is no common prefix, so an empty string is returned.
# In Example 3, the longest common prefix is "ap".

from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        smallest_string = min(strs, key=len) # Get the smallest string in the list
        for i, ch in enumerate(smallest_string): # i is the index value and ch is the index character of smallest string
            for other in strs: # loop among oter strings
                if other[i] != ch: # If value is diff
                    return smallest_string[:i] # Return the substring
        return smallest_string
        