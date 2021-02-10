# Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

# Example

# For s = "abacabad", the output should be
# firstNotRepeatingCharacter(s) = 'c'.

# There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

# For s = "abacabaabacaba", the output should be
# firstNotRepeatingCharacter(s) = '_'.

# There are no characters in this string that do not repeat.

# Input/Output

# [execution time limit] 4 seconds (py3)

# [input] string s

# A string that contains only lowercase English letters.

# Guaranteed constraints:
# 1 ≤ s.length ≤ 105.

# [output] char

# The first non-repeating character in s, or '_' if there are no characters that do not repeat.

def first_not_repeating_character(s):
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
        return '_'
    
    
# from collections import Counter
# def firstNotRepeatingCharacter(s):
#     list_s = [char for char in s]
#     contador = Counter(list_s)
    
#     for key, value in contador.items():
#         if value == 1:
#             return str(key)
#     return '_'
    

