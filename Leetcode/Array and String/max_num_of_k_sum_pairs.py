# You are given an integer array 'nums' and an integer 'k'.
# In one operation, you can pick two numbers from the array whose sum equals 'k' and remove them from the array.
# Return the maximum number of operations you can perform on the array.

# Example 1:
# Input: nums = [1,2,3,4], k = 5
# Output: 2

# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.

# Example 2:
# Input: nums = [3,1,3,4,3], k = 6
# Output: 1

# Explanation: Starting with nums = [3,1,3,4,3]:
# - Remove the first two 3's, then nums = [1,4,3]
# There are no more pairs that sum up to 6, hence a total of 1 operation.

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # Create a Counter object 'c' to count the occurrences of each number in 'nums'.
        c = Counter(nums)
        
        result = 0  # Initialize a variable 'result' to store the maximum number of operations.
        s = set()   # Initialize a set 's' to keep track of visited numbers.
        
        # Iterate through each value 'val' in 'nums'.
        for val in nums:
            # Check if 'val' is not in the set 's' and if the complementary value (k - val) exists in the Counter 'c'.
            if val not in s and (k - val) in c:
                # If 'val' and (k - val) are the same, add half of their occurrences to 'result' (since each pair is removed).
                if val == k - val:
                    result += c[val] // 2
                else:
                    # Otherwise, add the minimum of the occurrences of 'val' and (k - val) to 'result'.
                    result += min(c[val], c[k - val])

                # Add 'val' and (k - val) to the set 's' to mark them as visited.
                s.add(val)
                s.add(k - val)
        
        # Return the final 'result' representing the maximum number of operations that can be performed.
        return result
