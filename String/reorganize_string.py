from collections import Counter
import heapq


class Solution:

  def reorganizeString(self, s: str) -> str:
    # Count the frequency of each character in the string
    freq_map = Counter(s)

    # Initialize a heap to store characters based on their frequency
    heap = []

    # Push characters and their negative frequencies into the heap
    for key, count in freq_map.items():
      heapq.heappush(heap, (-count, key))

    # Initialize a list to store the rearranged string
    res = []

    # While there are at least two elements in the heap
    while len(heap) > 1:
      # Pop the two characters with the highest frequencies
      freq1, char1 = heapq.heappop(heap)
      freq2, char2 = heapq.heappop(heap)

      # Append the characters alternately to the result list
      res.extend([char1, char2])

      # If the frequency of char1 is greater than 1, push it back to the heap with decremented frequency
      if abs(freq1) > 1:
        heapq.heappush(heap, (freq1 + 1, char1))

      # If the frequency of char2 is greater than 1, push it back to the heap with decremented frequency
      if abs(freq2) > 1:
        heapq.heappush(heap, (freq2 + 1, char2))

    # If there is one character left in the heap (odd number of characters)
    if heap:
      # Pop the character and its frequency from the heap
      freq, char = heapq.heappop(heap)
      # If the frequency of the character is greater than 1, it cannot be rearranged adjacent to itself
      if abs(freq) > 1:
        return ""
      # Append the character to the result list
      res.append(char)

    # Join the characters in the result list to form the rearranged string
    return "".join(res)
