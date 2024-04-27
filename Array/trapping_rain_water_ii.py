class Solution:

  def trapRainWater(self, heightMap: List[List[int]]) -> int:
    # Get the dimensions of the height map
    row_len = len(heightMap)
    col_len = len(heightMap[0])

    # Initialize a min heap
    heap = []

    # Add the border cells to the heap
    for r_idx in range(row_len):
      for col_idx in range(col_len):
        if r_idx == 0 or r_idx == row_len - 1 or col_idx == 0 or col_idx == col_len - 1:
          heapq.heappush(heap, (heightMap[r_idx][col_idx], r_idx, col_idx))
          # Mark border cells as visited by changing their height to -1
          heightMap[r_idx][col_idx] = -1

    # Initialize variables to track current level and total trapped rainwater
    curr_level = 0
    final_res = 0

    # Process the heap
    while heap:
      curr_val, x, y = heapq.heappop(heap)
      curr_level = max(curr_val, curr_level)

      # Explore neighboring cells
      for c_x, c_y in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
        if 0 <= c_x < row_len and 0 <= c_y < col_len and heightMap[c_x][
            c_y] != -1:
          heapq.heappush(heap, (heightMap[c_x][c_y], c_x, c_y))
          # Accumulate trapped rainwater if there's a depression
          if heightMap[c_x][c_y] < curr_level:
            final_res += curr_level - heightMap[c_x][c_y]
          # Mark visited cells
          heightMap[c_x][c_y] = -1

    return final_res
