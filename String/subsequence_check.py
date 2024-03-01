# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

# Example 1:

# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:

# Input: s = "axc", t = "ahbgdc"
# Output: false

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Check if the length of 's' is greater than the length of 't'.
        # If so, 's' cannot be a subsequence of 't', so return False.
        if len(s) > len(t):
            return False
        
        # If 's' is an empty string, it is trivially a subsequence of any string 't'.
        if len(s) == 0:
            return True
        
        p1 = 0  # Initialize pointer 'p1' for string 's'.
        
        # Loop through each character 'p2' in string 't'.
        for p2 in range(len(t)):
            # Check if 'p1' is within the bounds of 's' and if the characters at 'p1' in 's' and 'p2' in 't' are equal.
            if p1 < len(s) and s[p1] == t[p2]:
                p1 += 1  # Increment pointer 'p1'.
        
        # Check if pointer 'p1' has reached the end of string 's'.
        # If so, 's' is a subsequence of 't'; otherwise, it is not.
        return p1 == len(s)
