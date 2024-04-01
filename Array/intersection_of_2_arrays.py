# Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.

from collections import Counter

class Solution:
  def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
      return set(nums1) & set(nums2)



class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create a Counter object to count the occurrences of elements in nums1
        count = Counter(nums1)

        # Initialize an empty list to store the result of intersection
        res = []

        # Iterate through each element in nums2
        for num in nums2:
            # Check if the current element is present in the Counter (nums1)
            # If its count is greater than 0, it means it's an intersection
            if count[num] > 0:
                # Add the current element to the result list
                res.append(num)
                # Decrement the count in the Counter to account for this intersection
                count[num] -= 1
        
        # Return the final result list containing the intersections
        return res

# We can also simply use
# nums1 - Counter({1: 2, 2: 2})
# nums2 - Counter({2: 2})
# nums1 & nums2 - Counter({2: 2})
# list(elements()) will return the values like above [value*no of count]
# return list((Counter(nums1) & Counter(nums2)).elements())
