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

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        # Sort the intervals based on their start times
        intervals.sort(key=lambda x: x.start)

        # Initialize a min-heap to keep track of the end times of ongoing intervals
        min_heap = []

        # Add the end time of the first interval to the min-heap
        heapq.heappush(min_heap, intervals[0].end)

        # Iterate through the sorted intervals
        for interval in intervals[1:]:
            # If the start time of the current interval is greater than or equal to the end time of the earliest ending interval
            # in the min-heap, pop the earliest ending interval from the min-heap
            if interval.start >= min_heap[0]:
                heapq.heappop(min_heap)

            # Add the end time of the current interval to the min-heap
            heapq.heappush(min_heap, interval.end)

        # The size of the min-heap represents the minimum number of meeting rooms required
        return len(min_heap)

# Example input
intervals = [Interval(0, 30), Interval(5, 10), Interval(15, 20)]
solution = Solution()
print(solution.minMeetingRooms(intervals))  # Output: 2
