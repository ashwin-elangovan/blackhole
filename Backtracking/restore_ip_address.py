class Solution:

  def restoreIpAddresses(self, s: str) -> List[str]:
    res = []  # List to store the valid IP addresses

    # If the length of the string is greater than 12 (maximum length for an IP address), return an empty list
    if len(s) > 12:
      return res

    # Backtracking function to generate all possible valid IP addresses
    def backtrack(idx, dots, curr_str):
      # If we have placed 4 dots and reached the end of the string, append the current IP address to the result list
      if dots == 4:
        if idx == len(s):
          res.append(
            curr_str[:-1]
          )  # Remove the last dot and append the IP address to the result list
        return

      # If we have placed more than 4 dots, or if we have exhausted the string, return
      if dots > 4 or idx == len(s):
        return

      # Iterate over the next 1 to 3 characters in the string to form a segment of the IP address
      for j in range(idx, min(idx + 3, len(s))):
        # Check if the current segment is a valid number (less than 256) and doesn't have leading zeros (except for zero itself)
        if int(s[idx:j + 1]) < 256 and (idx == j or s[idx] != '0'):
          # Recursively backtrack with the next index, incremented dots count, and updated current string
          backtrack(j + 1, dots + 1, curr_str + s[idx:j + 1] + '.')

    # Start backtracking from index 0, with 0 dots placed initially, and an empty current string
    backtrack(0, 0, "")
    return res
