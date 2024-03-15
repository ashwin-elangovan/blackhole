class Solution:
  def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
      # Convert banned words to a set for faster lookup
      banned = set(banned)

      # Get all the words from the paragraph, convert them to lowercase, and store them in a list
      words = re.findall(r'\w+', paragraph.lower())

      # Count the occurrences of each word in the paragraph, excluding banned words
      words_ctr = Counter(word for word in words if word not in banned)

      # Create a min-heap to store word counts, where the count is negated to make it behave like a max-heap
      heap = []
      for key, val in words_ctr.items():
          heapq.heappush(heap, (-val, key))

      # Pop the most common word from the heap (since it's a max-heap with counts negated)
      final_val = heapq.heappop(heap)

      # Return the most common word (the second element of the tuple)
      return final_val[1]

