# There are n cities numbered from 0 to n - 1 and n - 1 roads such that there is only one way to travel between two different cities (this network form a tree). Last year, The ministry of transport decided to orient the roads in one direction because they are too narrow.

# Roads are represented by connections where connections[i] = [ai, bi] represents a road from city ai to city bi.

# This year, there will be a big event in the capital (city 0), and many people want to travel to this city.

# Your task consists of reorienting some roads such that each city can visit the city 0. Return the minimum number of edges changed.

# It's guaranteed that each city can reach city 0 after reorder.

# Input: n = 6, connections = [[0,1],[1,3],[2,3],[4,0],[4,5]]
# Output: 3
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
# Example 2:


# Input: n = 5, connections = [[1,0],[1,2],[3,2],[3,4]]
# Output: 2
# Explanation: Change the direction of edges show in red such that each node can reach the node 0 (capital).
# Example 3:

# Input: n = 3, connections = [[1,0],[2,0]]
# Output: 0
for u, v in connections
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]) -> int:
        self.res = 0  # Initialize the result counter
        roads = set()  # Store the roads that need reordering as a set
        graph = defaultdict(list)  # Create an adjacency list to represent the graph

        # Iterate through the connections and build the graph and set of roads
        for u, v in connections:
            roads.add((u, v))  # Add the road (u, v) to the set
            graph[v].append(u)  # Add v as a neighbor of u
            graph[u].append(v)  # Add u as a neighbor of v

        # Depth-First Search (DFS) function to traverse the graph
        def dfs(u, parent):
            self.res += (parent, u) in roads  # Check if the road needs reordering and update the result
            for v in graph[u]:  # Iterate through neighboring cities
                if v == parent:
                    continue  # Skip revisiting the parent city
                dfs(v, u)  # Recursively call DFS on neighboring cities

        dfs(0, -1)  # Start the DFS traversal from city 0 with -1 as its parent
        return self.res  # Return the total count of roads that need reordering
