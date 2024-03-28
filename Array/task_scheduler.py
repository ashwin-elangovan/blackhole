from collections import Counter
import heapq


class Solution:

  def leastInterval(self, tasks: List[str], n: int) -> int:
    # Count the occurrences of each task
    ctr = Counter(tasks)

    # Initialize a heap to store tasks by their frequency
    heap = []

    # Push tasks and their negative frequencies onto the heap
    for key, val in ctr.items():
      heapq.heappush(heap, [-val, key])

    # Count the number of tasks with the most frequent frequency
    no_of_most_frequent_elements = 0
    frequency_of_the_most_frequent_element = abs(heap[0][0])

    # Pop tasks with the most frequent frequency from the heap
    while len(heap) > 0 and abs(heap[0][0]) == frequency_of_the_most_frequent_element:
      no_of_most_frequent_elements += 1
      heapq.heappop(heap)

    # Calculate the total time required
    # n represents the input n
    # (n+1) means input n plus most frequent_element
    total_time = (n + 1) * (frequency_of_the_most_frequent_element - 1) + no_of_most_frequent_elements

    # Return the maximum of the total time and the number of tasks
    return max(total_time, len(tasks))
