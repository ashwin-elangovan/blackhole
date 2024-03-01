# In this problem, there is an undirected graph with n nodes. There is also an edges array. Where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

# You need to return the number of connected components in that graph.


# Example

# Example 1
# Input:

# 3
# [[0,1], [0,2]]
# Output:
# 1

# Example 2
# Input:
# 6
# [[0,1], [1,2], [2, 3], [4, 5]]
# Output:
# 2

from typing import (
    List,
)

class Solution:
    """
    @param n: the number of vertices
    @param edges: the edges of undirected graph
    @return: the number of connected components
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        rank = [1]*n

        def find(node):
            res = node
            while parent[res] != res:
                res = parent[res]
            return res

        def union(node1, node2):
            origin1, origin2 = find(node1), find(node2)
            print(origin1, origin2)
            if origin1 == origin2:
                return 0
            if rank[origin1] >= rank[origin2]:
                parent[origin2] = origin1
                rank[origin1] += rank[origin2]
            else:
                parent[origin1] = origin2
                rank[origin2] += rank[origin1]
            return 1

        total_components = n
        for x, y in edges:
            total_components -= union(x, y)

        print(parent)

        return total_components
