# You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

# The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

# Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.

# Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
# Output: 20

# (Prim's)

from collections import defaultdict
import heapq
)

class Solution:

  def minCostConnectPoints(self, points: List[List[int]]) -> int:
    # Initialize adjacency list to store distances between points
    adj = defaultdict(list)

    # Set to keep track of visited points
    visit = set()

    # Variable to store total cost
    total_cost = 0

    # Build the adjacency list with distances between each pair of points
    for i in range(len(points)):
      x1, y1 = points[i]
      for j in range(i + 1, len(points)):
        x2, y2 = points[j]
        # Calculate Manhattan distance between points
        dist = abs(x1 - x2) + abs(y1 - y2)
        # Add distance and index of adjacent point to the adjacency list
        adj[i].append([dist, j])
        adj[j].append([dist, i])

    # Initialize min-heap with starting point (0, 0)
    minH = [[0, 0]]  # 0 stands for the 0th point not 0 value. cost, point_idx

    # Perform Prim's algorithm to find minimum spanning tree
    while minH:
      # Pop the minimum cost edge from min-heap
      cost, point_idx = heapq.heappop(minH)
      # If the point is already visited, skip
      if point_idx in visit:
        continue
      # Mark the point as visited
      visit.add(point_idx)
      # Add cost to total cost
      total_cost += cost
      # Explore neighbors of the current point
      for n_cost, n_point in adj[point_idx]:
        # If neighbor is not visited, add it to min-heap
        if n_point not in visit:
          heapq.heappush(minH, [n_cost, n_point])

    # Return the total minimum cost
    return total_cost
