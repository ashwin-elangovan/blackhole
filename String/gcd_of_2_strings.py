
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

# Python O(n) sol. based on gcd.
# Example explanation:

# input: "ABCABC", "ABC"

# gcdOfString( "ABCABC", "ABC" )　　　　　# gcd( 6, 3 ) = 3

# -> gcdOfString( "ABC", "ABC" )

# -> match, return "ABC" as greatest common divisor of string

# input: "ABABAB", "AB"

# gcdOfString( "ABABAB, "AB" ) 　　　　　# gcd( 6, 2 ) = 2

# -> gcdOfString( "AB", "AB" )

# -> match, return "AB" as greatest common divisor of string

# input: "LEET", "CODE"

# gcdOfString( "LEET, "CODE" ) 　　　　　　# "LEETCODE" =/= "CODELEET"

# -> reject, "LEET" and "CODE" have no common factor string.

# Idea: Get GCD of the length of 2 strings and use that to slice and return.

from math import gcd

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if ( str1 + str2 ) != ( str2 + str1 ):
            # if str1 and str2 has no common factor, then reject			
            return ''
			
        elif str1 == str2:
            # if str1 and str2 are perfect match, then we find greatest common divisor of strings		
            return str1
        else:
            # if str1 =\= str2, then str1[:length_by_gcd] is the answer
            length_by_gcd = gcd(len(str1), len(str2))
            return str1[:length_by_gcd]