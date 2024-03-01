Two strings are considered close if you can attain one from the other using the following operations:

Operation 1: Swap any two existing characters.
For example, abcde -> aecdb
Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
You can use the operations on either string as many times as necessary.

Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.

 

Example 1:

Input: word1 = "abc", word2 = "bca"
Output: true
Explanation: You can attain word2 from word1 in 2 operations.
Apply Operation 1: "abc" -> "acb"
Apply Operation 1: "acb" -> "bca"
Example 2:

Input: word1 = "a", word2 = "aa"
Output: false
Explanation: It is impossible to attain word2 from word1, or vice versa, in any number of operations.


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        c1 = Counter(word1)  # Count occurrences of characters in word1 using a Counter.
        c2 = Counter(word2)  # Count occurrences of characters in word2 using a Counter.

        # Check if the sets of keys (characters) in both Counters are the same,
        # and if the sorted lists of values (occurrences) are the same.
        # Here sorted is not needed when comparing keys
        
        # dict(a=1, b=2) == dict(a=2, b=1)
        # False
        
        # dict(a=1, b=2) == dict(a=1, b=2, c=0)
        # False
        
        # dict(a=1, b=2) == dict(b=2, a=1)
        # True

        # But for values they must be sorted to check if they are same.
        # Ideally, the keys should match and the count values should match so even after swapping we can restore it to the original string.
        return c1.keys() == c2.keys() and sorted(c1.values()) == sorted(c2.values())