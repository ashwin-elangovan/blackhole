# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:
      # Strategy: Vertical area and then horizontal area

      # stack = [] # pair: (index, height)
      # max_area = 0
      # for curr_idx, current_height in enumerate(heights):
      #     start = curr_idx
      #     while stack and stack[-1][1] > current_height:
      #         idx, h = stack.pop()
      #         max_area = max(max_area, h*(curr_idx-idx))
      #         start = idx

      #     stack.append((start, current_height))

      # for start_idx, height in stack:
      #     max_area = max(max_area, height*(len(heights)-start_idx))

      # return max_area

      height = heights
      # We loop from 0 -> n+1 because we are considering a height array with a zero at the end.
      # We add a zero at the end because we want to always ensure a loop condition in which the current considered height is less than the height's stored in the stack.
      # This also handles horizontal heights [1,1,1,1,1]
      height.append(0)
      # For condition,  w = (i-1) - stack[-1] 0 to -1 cases.
      stack = [-1]
      ans = 0
      print(height)
      for i in range(len(height)):
          while height[i] < height[stack[-1]]:
              h = height[stack.pop()]
              # i-1 is the right boundary (previous larger element) and stack[-1] is the left boundary. at most left boundary goes till the while condition breaks
              print(i-1, stack[-1], height[i])
              w = (i-1) - stack[-1]
              ans = max(ans, h * w)
          stack.append(i)
      return ans






