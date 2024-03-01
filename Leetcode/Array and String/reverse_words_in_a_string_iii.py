# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"

# Ruby
# s.split.reverse.join(" ").reverse
# or
# s.split.map(&:reverse).join(" ")

# Python

' '.join(s.split()[::-1])[::-1]

# [::-1] - Reverses word and letters
# s.split()[::-1] - ['contest', 'LeetCode', 'take', "Let's"]
# ' '.join(s.split()[::-1])[::-1] - "s'teL ekat edoCteeL tsetnoc"
