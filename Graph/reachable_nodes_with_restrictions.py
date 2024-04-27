from collections import defaultdict


class Solution:

  def reachableNodes(self, n: int, edges: List[List[int]],
                     restricted: List[int]) -> int:
    # Convert the list of restricted nodes into a set for faster lookup
    restricted = set(restricted)

    # Initialize an adjacency list to represent the graph
    adj = defaultdict(list)

    # Initialize an empty set to keep track of visited nodes
    visited = set()

    # Populate the adjacency list
    for start, end in edges:
      # Skip edges connected to visited or restricted nodes
      if start in visited or end in visited:
        continue
      # Add edges to the adjacency list
      adj[start].append(end)
      adj[end].append(start)

    # Initialize a queue with the starting node
    queue = [0]

    # Perform BFS to explore reachable nodes
    while queue:
      # Pop a node from the queue
      curr_node = queue.pop()
      # Skip if the current node is already visited or restricted
      if curr_node in visited or curr_node in restricted:
        continue

      # Mark the current node as visited
      visited.add(curr_node)

      # Explore neighbors of the current node
      for nei in adj[curr_node]:
        # Add unvisited neighbors to the queue
        if nei not in visited:
          queue.append(nei)

    # Return the number of visited nodes
    return len(visited)
