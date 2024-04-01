import heapq


class Solution:

  def shortestPath(self, n: int, edges: List[List[int]],
                   src: int) -> Dict[int, int]:
    # Build an adjacency list
    graph = defaultdict(list)

    for source, dst, weight in edges:
      graph[source].append([dst, weight])

    nodes = [[0, src]]  # weight and destination
    heapq.heapify(nodes)
    final_list = {}

    while nodes:
      weight1, dst1 = heapq.heappop(nodes)
      if dst1 in final_list:
        continue

      final_list[dst1] = weight1

      for n_dst, n_weight in graph[dst1]:
        if n_dst not in final_list: 
          heapq.heappush(nodes, [weight1 + n_weight, n_dst])

    for i in range(n):
      if i not in final_list:
        final_list[i] = -1

    return final_list


n = 5
edges = [[0, 1, 10], [0, 2, 3], [1, 3, 2], [2, 1, 4], [2, 3, 8], [2, 4, 2],
         [3, 4, 5]]
src = 0