from typing import List
from collections import defaultdict


class Solution:

  def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
    # Base case: If there's only one node, return it as the root of the tree
    if n == 1:
      return [0]

    # Create an adjacency list to represent the graph
    adj = defaultdict(set)

    # Populate the adjacency list with the given edges
    for start, end in edges:
      adj[start].add(end)
      adj[end].add(start)

    # Initialize a list to store leaf nodes
    leaves = []

    # Find all leaf nodes (nodes with only one neighbor)
    for node in range(n):
      if len(adj[node]) == 1:
        leaves.append(node)

    # Repeat the process until there are only 1 or 2 nodes left
    while n > 2:
      new_leaves = []  # Temporary list to store new leaf nodes
      for leaf in leaves:
        nei = adj[leaf].pop()  # Get the only neighbor of the leaf
        adj[nei].remove(leaf)  # Remove the leaf from the neighbor's neighbors
        if len(adj[nei]) == 1:  # If the neighbor becomes a leaf after removal
          new_leaves.append(nei)  # Add it to the new leaves list
      n -= len(
        leaves
      )  # Decrement the number of nodes by the number of removed leaves
      leaves = new_leaves[:]  # Update the list of leaves for the next iteration
    return leaves  # Return the remaining nodes, which are the roots of the minimum height trees
