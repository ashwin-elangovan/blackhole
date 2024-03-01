# Given a string 's' and an integer 'k', return the maximum number of vowel letters in any substring of 's' with length 'k'.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Example 1:
# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.

# Example 2:
# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.

# Example 3:
# Input: s = "leetcode", k = 3
# Output: 2
# Explanation: "lee", "eet" and "ode" contain 2 vowels.

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0              # Initialize the variable 'count' to keep track of the vowel count in the current substring.
        ans = 0                # Initialize the variable 'ans' to store the maximum vowel count found.
        vowels = "aeiou"       # Define the string of vowel letters.

        for i, c in enumerate(s):
            if i >= k:
                # If the character at index i-k (i.e., the first character in the current window) is a vowel, decrement 'count'.
                if s[i - k] in vowels:
                    count -= 1
            # If the current character is a vowel, increment 'count'. This is the base case. Write this first.
            if c in vowels:
                count += 1
            # Update 'ans' with the maximum of 'ans' and 'count'.
            ans = max(ans, count)
        
        return ans  # Return the maximum number of vowel letters in any substring of 's' with length 'k'.
