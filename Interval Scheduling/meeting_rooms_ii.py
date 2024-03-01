# Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), find the minimum number of conference rooms required.

# Example 1:
# Input:
# [[0, 30],[5, 10],[15, 20]]
# Output:
#  2

# Example 2:
# Input:
#  [[7,10],[2,4]]
# Output:
#  1

# def interval_partitioning(intervals):
#   intervals.sort(key= lambda x: x[1]) # Sort by end times
#   rooms = []

#   for interval in intervals:
#     allocated = False
#     start, end = interval
#     for room in rooms:
#       if start >= room[-1][1]:
#         room.append([interval])
#         allocated = True
#         break

#     if not allocated:
#         rooms.append([interval])

#   return len(rooms)
import heapq


def interval_partitioning(intervals):
  heap = []

  for start, end in sorted(intervals):
    while heap and heap[0] <= start:
      heapq.heappop(heap)
    heapq.heappush(heap, end)

  return len(heap)


res = interval_partitioning([[0, 30], [5, 10], [15, 20]])
print(res)