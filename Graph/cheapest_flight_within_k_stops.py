import heapq
import collections
from typing import List


class Solution:

  def findCheapestPrice(self, n: int, flights: List[List[int]], src: int,
                        dst: int, k: int) -> int:
    # Initialize a defaultdict to represent the graph
    graph = collections.defaultdict(dict)

    # Build the graph from the flights data
    for s, d, w in flights:
      graph[s][d] = w

    # Initialize a priority queue with the starting node, source, and remaining stops
    pq = [(0, src, k + 1)]  # (cost, node, stops_left)

    # Initialize a list to keep track of visited nodes
    vis = [0] * n

    # Perform Dijkstra's algorithm with limited stops (k stops allowed)
    while pq:
      # Pop the node with the smallest cost so far from the priority queue
      w, x, k = heapq.heappop(pq)

      # If the popped node is the destination, return the cost
      if x == dst:
        return w

      # If the node has been visited the maximum allowed times, skip it
      if vis[x] >= k:
        continue

      # Mark the node as visited
      vis[x] = k

      # Iterate over the neighbors of the current node
      for y, dw in graph[x].items():
        # Add the neighbor to the priority queue with updated cost and remaining stops
        heapq.heappush(pq, (w + dw, y, k - 1))

    # If destination cannot be reached within the allowed stops, return -1
    return -1
