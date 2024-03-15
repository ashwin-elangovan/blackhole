class HeapItem:

  def __init__(self, word: str, count: int) -> None:
    # Initialize HeapItem with word and its count
    self.word = word
    self.count = count

  # Define comparison method for HeapItem objects
  def __lt__(self, to_compare) -> bool:
    # If counts are equal, prioritize lexicographically smaller word
    if self.count == to_compare.count:
      return self.word > to_compare.word
    # Otherwise, prioritize higher count
    return self.count < to_compare.count


class Solution:

  def topKFrequent(self, words: List[str], k: int) -> List[str]:
    # Count occurrences of each word
    word_counts = collections.Counter(words)
    # Initialize heap
    heap = []
    # Iterate over word counts
    for word, count in word_counts.items():
      # Create HeapItem object
      item = HeapItem(word, count)
      # If heap size is less than k, push item to heap
      if len(heap) < k:
        heapq.heappush(heap, item)
      else:
        # If current item has higher count or lexicographically smaller word, replace root of heap
        if heap[0] < item:
          heapq.heappop(heap)
          heapq.heappush(heap, item)
    # Initialize result list
    res = []
    # Pop top k elements from heap and append to result
    while k:
      cur = heapq.heappop(heap)
      res.append(cur.word)
      k -= 1
    # Reverse the result list
    return res[::-1]
