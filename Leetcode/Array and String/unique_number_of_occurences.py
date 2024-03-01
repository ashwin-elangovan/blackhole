# Given an array of integers 'arr', the task is to return true if the number of occurrences of each value in the array is unique, or false otherwise.

# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2, and 3 has 1. No two values have the same number of occurrences.

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = collections.Counter(arr)  # Create a counter to count occurrences of each value in the array.
        # Compare the number of unique values in the counter (Keys) with the number of unique occurrence counts (Values) using 'set'.
        return len(c) == len(set(c.values()))
