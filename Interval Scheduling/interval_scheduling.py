def interval_scheduling(intervals):
  sorted_intervals = sorted(intervals, key=lambda x: x[1])

  count = 0

  prev_end = -1

  for start, end in sorted_intervals:
    if start >= prev_end:
      count += 1
      prev_end = end

  return count


intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]
print(interval_scheduling(intervals))