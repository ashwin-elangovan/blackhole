class Solution:

  def trap(self, height: List[int]) -> int:
    left = 0  # Initialize left pointer
    right = len(height) - 1  # Initialize right pointer

    max_left, max_right = 0, 0  # Initialize max_left and max_right variables

    final_val = 0  # Initialize final_val variable to store the trapped rainwater volume

    # Loop until left pointer is less than or equal to right pointer
    while left <= right:
      # Print current pointers and maximum heights for debugging
      # print(left, right, max_left, max_right)

      # Check if the maximum height on the left side is less than or equal to the maximum height on the right side
      if max_left <= max_right:
        # Calculate the trapped rainwater level between max_left and current height[left]
        temp = max_left - height[left]

        # Add the trapped rainwater level to the final_val if it is positive
        if temp > 0:
          final_val += temp

        # Update max_left to the maximum of current max_left and height[left]
        max_left = max(max_left, height[left])

        # Move the left pointer to the next position
        left += 1
      else:
        # Calculate the trapped rainwater level between max_right and current height[right]
        temp = max_right - height[right]

        # Add the trapped rainwater level to the final_val if it is positive
        if temp > 0:
          final_val += temp

        # Update max_right to the maximum of current max_right and height[right]
        max_right = max(max_right, height[right])

        # Move the right pointer to the previous position
        right -= 1

    return final_val  # Return the total trapped rainwater volume
