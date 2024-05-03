class Solution:

  def dailyTemperatures(self, T):
    # Get the length of the input list T
    t_len = len(T)

    # Initialize an array to store the result
    final_arr = [0] * t_len

    # Initialize an empty stack to store indices of temperatures
    temp = []

    # Iterate through each temperature and its index
    for idx, value in enumerate(T):
      # While the stack is not empty and the current temperature is higher than the temperature at the top of the stack
      while temp and T[temp[-1]] < value:
        # Pop the index of the temperature from the stack
        prev_idx = temp.pop()
        # Calculate the number of days until the temperature rises above the previous temperature
        final_arr[prev_idx] = idx - prev_idx
      # Append the current index to the stack
      temp.append(idx)

    # Return the array containing the number of days until the temperature rises above each temperature
    return final_arr
