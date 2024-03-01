# Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), determine if a person could attend all meetings.
# Example 1:
# Input:
# [[0,30],[5,10],[15,20]]
# Output:
#  false

# Example 2:
# Input:
#  [[7,10],[2,4]]
# Output:
#  true


def canAttendMeetings(intervals):
  if not intervals:
    return True

  intervals.sort(key=lambda x: x[0])  # Sort meetings based on start times

  for i in range(1, len(intervals)):
    if intervals[i][0] < intervals[i - 1][1]:  # Check for overlap
      return False

  return True


# Example usage:
intervals1 = [[0, 30], [5, 10], [15, 20]]
print(canAttendMeetings(intervals1))  # Output: False

intervals2 = [[7, 10], [2, 4]]
print(canAttendMeetings(intervals2))  # Output: True
