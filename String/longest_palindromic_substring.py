# Given a string 's', return the longest palindromic substring in 's'.

# Example 1:
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:
# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""   # Initialize an empty string 'result' to store the longest palindromic substring.
        res_len = 0    # Initialize a variable 'res_len' to store the length of the longest palindromic substring found.

        # Iterate through each character 'i' in the string.
        for i in range(len(s)):
            # There can be 2 types of palindromes, odd and even.
            
            # Odd case:
            l, r = i, i   # Initialize pointers 'l' and 'r' to the same index 'i'.
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    l_end = l
                    r_end = r
                    res_len = r - l + 1
                result = s[l_end:r_end + 1]
                l -= 1
                r += 1

            # Even case:
            l, r = i, i + 1   # Initialize pointers 'l' and 'r' to adjacent indices around 'i'.
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > res_len:
                    l_end = l
                    r_end = r
                    res_len = r - l + 1
                result = s[l_end:r_end + 1]
                l -= 1
                r += 1
        
        # After looping through all possible centers, the 'result' contains the longest palindromic substring.
        return result

# Sandwiched version

class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        res_len = 0
        l_end, r_end = 0, 0

        for i in range(len(s)):
            # There can be 2 types of palindromes, odd and even
            # Odd case
            l,r = i,i
            result, res_len, l_end, r_end = self.compute_substr(l, r, l_end, r_end, s, result, res_len)
            # Even case
            l,r = i,i+1
            result, res_len, l_end, r_end = self.compute_substr(l, r, l_end, r_end, s, result, res_len)
        return result
    
    def compute_substr(self, l, r, l_end, r_end, s, result, res_len):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if(r-l+1 > res_len):
                l_end = l
                r_end = r
                res_len = r-l+1
            result = s[l_end:r_end+1]
            l -= 1
            r += 1
        return result, res_len, l_end, r_end
                

