from typing import List
from collections import defaultdict, deque


class Solution:

  def ladderLength(self, beginWord: str, endWord: str,
                   wordList: List[str]) -> int:
    # If the endWord is not present in the wordList, it's impossible to transform beginWord to endWord
    if endWord not in wordList:
      return 0

    # Create a defaultdict to store adjacent words with the same pattern
    adj = defaultdict(list)
    # Include the beginWord in the wordList to consider it as a potential transformation
    wordList.append(beginWord)

    # Populate the adjacency list with words having the same pattern
    for word in wordList:
      for idx in range(len(word)):
        pattern = word[:idx] + "*" + word[
          idx + 1:]  # Create a pattern by replacing one character with '*'
        adj[pattern].append(word)

    # Initialize a queue with the beginWord and a set to keep track of visited words
    queue = deque([beginWord])
    visited = set()
    depth = 1  # Initialize the depth (number of transformations) to 1

    # BFS traversal to find the shortest transformation sequence
    while queue:
      # Process all words at the current level
      for _ in range(len(queue)):
        curr_node = queue.popleft()

        # If the current word equals the endWord, return the depth (number of transformations)
        if curr_node == endWord:
          return depth

        # Skip if the current word has been visited before
        if curr_node in visited:
          continue

        # Mark the current word as visited
        visited.add(curr_node)

        # Generate all possible patterns by replacing one character with '*'
        for idx in range(len(curr_node)):
          pattern = curr_node[:idx] + "*" + curr_node[idx + 1:]
          # Explore all adjacent words with the same pattern
          for nei in adj[pattern]:
            # Add unvisited adjacent words to the queue
            if nei not in visited:
              queue.append(nei)

      # Increment the depth for the next level of BFS traversal
      depth += 1

    # If the endWord is not reachable from the beginWord, return 0
    return 0
