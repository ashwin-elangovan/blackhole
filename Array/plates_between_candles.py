import bisect

class Solution:
  def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
      # Initialize prefix list to keep track of the number of plates until each point
      prefix = [0] 

      # Initialize a list to store the indices of candles
      candles = []

      # Iterate through the string to populate the prefix list and find candle indices
      for i, ch in enumerate(s): 
          if ch == '|':  # If a candle is found
              candles.append(i)
          if ch == '|':  # If a candle is found, maintain the same number of plates until this point
              prefix.append(prefix[-1])
          else:  # If a plate is found, increment the number of plates until this point
              prefix.append(prefix[-1] + 1)

      # Initialize a list to store the results for each query
      ans = []

      # Iterate through the queries
      for x, y in queries: 
          # Find the index of the leftmost candle greater than or equal to x
          lo = bisect.bisect_left(candles, x)

          # Find the index of the rightmost candle less than or equal to y
          hi = bisect.bisect_right(candles, y) - 1

          # If valid candle indices are found
          if 0 <= hi and lo < len(candles) and lo <= hi: 
              # Calculate the number of plates between candles x and y using prefix values
              ans.append(prefix[candles[hi]+1] - prefix[candles[lo]+1])
          else:  # If no valid candles are found within the range
              ans.append(0)

      return ans 
