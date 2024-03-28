class Solution:
  def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
      # Initialize two lists to store intervals before and after the newInterval
      l, r = [], []

      # Iterate through each interval in the intervals list
      for interval in intervals:
          # If the current interval ends before the start of the newInterval, add it to the left list
          if interval[1] < newInterval[0]:
              l.append(interval)
          # If the current interval starts after the end of the newInterval, add it to the right list
          elif interval[0] > newInterval[1]:
              r.append(interval)
          # If there is an overlap between the current interval and the newInterval, merge them
          else:
              # Update the newInterval to cover both the current interval and itself
              newInterval = [min(newInterval[0], interval[0]), max(newInterval[1], interval[1])]

      # Combine the left list, newInterval, and right list to form the result
      return l + [newInterval] + r
