# Given a string s, return the number of palindromic substrings in it.

# A string is a palindrome when it reads the same backward as forward.

# A substring is a contiguous sequence of characters within the string.

 

# Example 1:

# Input: s = "abc"
# Output: 3
# Explanation: Three palindromic strings: "a", "b", "c".
# Example 2:

# Input: s = "aaa"
# Output: 6
# Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".

class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0

        # Iterate through each character 'i' in the string.
        for i in range(len(s)):
            # There can be 2 types of palindromes, odd and even.

            # Odd case:
            result += self.compute_substr(s, i, i)
            
            # Even case:
            result += self.compute_substr(s, i, i+1)
        
        # After looping through all possible centers, the 'result' contains the longest palindromic substring.
        return result

    def compute_substr(self, s, l, r):
        res = 0
        # Initialize pointers 'l' and 'r' to the same index 'i'.
        while l >= 0 and r < len(s) and s[l] == s[r]:
            res += 1
            l -= 1
            r += 1
        return res