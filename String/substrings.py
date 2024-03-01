def substrings(s):
  str_arr = []
  # First loop for starting index
  for i in range(len(s)):
    substr = ""
    # Second loop is generating sub-String
    for j in range(i, len(s)):
      substr += s[j]
      str_arr.append(substr)
  return str_arr


substrings("hello")