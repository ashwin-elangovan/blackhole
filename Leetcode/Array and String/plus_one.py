# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

# Increment the large integer by one and return the resulting array of digits.


class Solution:
  def plusOne(self, digits: List[int]) -> List[int]:
      if len(digits) == 1 and digits[0] == 9:
          return [1,0]

      if digits[-1] != 9:
          digits[-1] += 1
      else:
          digits[-1] = 0
          digits[:-1] = self.plusOne(digits[:-1])

      return digits


Different solution:
    
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        for index, value in enumerate(digits): # Loop the digits
            num = num*10 + digits[index] # Add the digits
        return [int(i) for i in str(num+1)] # Do a +1 and separate them into an array
