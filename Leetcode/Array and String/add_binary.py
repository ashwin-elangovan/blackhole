class Solution:
    def addBinary(a: str, b: str) -> str:
        carry = 0
        final_val = ""
        aIndex = len(a)-1 # Using indexes so reducing by 1
        bIndex = len(b)-1

        while aIndex >= 0 or bIndex >= 0 or carry: # Coming from last digit
            if aIndex >= 0:
                carry += int(a[aIndex]) # Adding the a digit to carry

            if bIndex >= 0:
                carry += int(b[bIndex]) # Adding the a digit to carry

            # Now carry can have 0/1/2/3 values
            final_val = str(carry%2) + final_val # "prepending" processed values in sum. Final val will have 0/1 values.
            carry //= 2

            aIndex -= 1
            bIndex -= 1

        return final_val

# class Solution:
  # def addBinary(self, a: str, b: str) -> str:
  #     return bin(int(a , 2) + int(b,2))[2:]
        