def generateSums(i, curSum):
  """
  Generate all possible sums of elements in the array starting from index i
  and store them in the set sums.
  """
  if i == len(nums):
    sums.add(curSum)  # Add the current sum to the set of sums
    return
  # Recursively generate sums including and excluding the current element
  generateSums(i + 1, curSum)  # Exclude current element
  generateSums(i + 1, curSum + nums[i])  # Include current element


# Initialize an empty set to store the generated sums
sums = set()

nums = [5, 4, 3]

# Generate all possible sums of elements in the first half of the nums array
generateSums(0, 0)

print(sums)
