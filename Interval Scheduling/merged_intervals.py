class Solution:

  def merge(self, intervals: List[List[int]]) -> List[List[int]]:
    # Sort intervals based on their start points
    intervals.sort(key=lambda x: x[0])

    merged_intervals = []
    # Merge intervals
    merged_interval = intervals[0]
    for start, end in intervals[1:]:
      if start > merged_interval[1]:
        # If start of next interval is greater than end of current merged interval,
        # add current merged interval to the result and start a new merged interval
        merged_intervals.append(merged_interval)
        merged_interval = [start, end]
      else:
        # Otherwise, merge the intervals
        merged_interval[1] = max(merged_interval[1], end)

    # Add the last merged interval
    merged_intervals.append(merged_interval)

    return merged_intervals
