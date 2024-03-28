class Solution:

  def smallestDistancePair(self, nums: List[int], k: int) -> int:
    # Sort the input array to use binary search
    nums.sort()
    n = len(nums)

    # Set the initial search space
    l, r = 0, nums[-1] - nums[
      0]  # 0 and the distance between max and min as search space

    # Function to determine if enough pairs exist with a given distance
    def enough(current_distance):
      slow, fast = 0, 0
      number_of_pairs = 0
      # Loop through the array to find pairs with distance less than or equal to the current distance
      while slow < n or fast < n:
        while fast < n and nums[fast] - nums[slow] <= current_distance:
          fast += 1
        # Calculate the number of pairs within the given distance
        number_of_pairs += fast - slow - 1
        slow += 1
      return number_of_pairs >= k
      # If the number of pairs is greater than or equal to k, reduce 'r' to get the minimum value

    # Binary search to find the smallest distance pair
    while l < r:
      mid = l + (r - l) // 2
      if enough(mid):
        r = mid
      else:
        l = mid + 1
    return l
