# You are given an integer array 'height' of length 'n'.
# There are 'n' vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# The goal is to find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:
  
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by the array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
  
# Input: height = [1,1]
# Output: 1
class Solution:
    def maxArea(self, height: List[int]) -> int:

      # BRUTE FORCE
      # res = 0
      # for l in range(len(height)):
      #     for r in range(l+1, len(height)):
      #         area = (r-l) * min(height[l], height[r])
      #         res = max(area, res)

      # return res

      
      # Initialize the variable 'res' to store the maximum area.
      res = 0
      
      # Initialize two pointers 'l' and 'r' representing the left and right ends of the container.
      l, r = 0, len(height) - 1
      
      # Loop until the left pointer 'l' is less than the right pointer 'r'.
      while l < r:
          # Calculate the area between the two pointers using the width (r - l) and the minimum height of the two heights.
          area = (r - l) * min(height[l], height[r])
          
          # Update 'res' with the maximum of the current area and the existing 'res'.
          res = max(area, res)
      
          # Move the pointers based on the condition of the heights at 'l' and 'r'.
          if height[l] < height[r]:
              l += 1  # Move the left pointer to the right.
          else:
              r -= 1  # Move the right pointer to the left.
      
      # After the loop, the 'res' variable contains the maximum area found.
      # Return the 'res' variable as the final result.
      return res
