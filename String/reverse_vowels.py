# Given a string s, reverse only all the vowels in the string and return it.

# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

# Example 1:

# Input: s = "hello"
# Output: "holle"
# Example 2:

# Input: s = "leetcode"
# Output: "leotcede"
class Solution:
    def reverseVowels(self, s: str) -> str:
        p1 = 0
        p2 = len(s) - 1
        vowels = list('aeiouAEIOU')
        str1 = list(s)
        while p1 < p2:
            if str1[p1] in vowels and str1[p2] in vowels:
                str1[p1], str1[p2] = str1[p2], str1[p1]
                p1 += 1
                p2 -= 1
            if str1[p1] not in vowels:
                p1 += 1
            if str1[p2] not in vowels:
                p2 -= 1
        
        return ''.join(str1)

# Alternate solution
# def reverseVowels(self, s):
#     # Find all vowels (case-insensitive) in the input string 's' using regex and store them in the 'vowels' list.
#     vowels = re.findall('(?i)[aeiou]', s)

#     # Replace each vowel in the input string 's' with the corresponding vowel from the 'vowels' list, in reverse order.
#     return re.sub('(?i)[aeiou]', lambda m: vowels.pop(), s)
