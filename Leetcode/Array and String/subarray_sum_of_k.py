# Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

# A subarray is a contiguous non-empty sequence of elements within an array.

 

# Example 1:

# Input: nums = [1,1,1], k = 2
# Output: 2
# Example 2:

# Input: nums = [1,2,3], k = 3
# Output: 2

# Logic video: https://www.youtube.com/watch?v=HbbYPQc-Oo4

# k = 7

# [3 4 7 2 -3 1 4 2]

# 3 7 14 16 13 14 18 20

# While in 14, (14-7) = 7, since we have 7 in index 1 already, without considering that we will 7 in index 3 which is a subarray 



from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # Create a dictionary to store the count of sums encountered so far
        sum_dict = defaultdict(lambda: 0)

        # Initialize variables to keep track of the current sum and the result
        current_sum = 0
        result = 0

        # Iterate through the elements in the input array
        for current_val in nums:
            # Add the current value to the running sum
            current_sum += current_val

            # If the current sum is equal to the target sum 'k', increment the result
            if current_sum == k:
                result += 1

            # Check if there exists a subarray with a sum of (current_sum - k)
            # If such a sum exists, it means there is a subarray that sums up to 'k'
            # Increment the result by the count of subarrays with the sum (current_sum - k)
            if (current_sum - k) in sum_dict:
                result += sum_dict[current_sum - k]
            
            # Update the dictionary to keep track of the count of the current sum
            sum_dict[current_sum] += 1
        
        # Return the final result, which represents the total number of subarrays with sum 'k'
        return result
