'''
Reverse a String:
Write a function that takes a string as input and returns the string reversed.

Time Complexity: O(n), where n is the length of the string.
Space Complexity: O(n), as a new string of length n is created.

In Python, strings can be sliced using the [::-1] notation, which means to start from the end of the string 
and move backwards with a step of -1. This effectively reverses the order of characters in the string.


The input string s is passed to the function.
The slicing operation s[::-1] is performed on the string. 
It starts from the first character (implicitly, as the start index is not specified), 
moves to the last character (implicitly, as the end index is not specified), and steps backward by -1.
The resulting reversed string is returned as the output.
'''

def reverse_string(s):
    return s[::-1]

'''
Check Anagrams:
Write a function that takes two strings as input and returns True 
if they are anagrams (contain the same characters), False otherwise.

Time Complexity: O(n log n), where n is the length of the longest string. This is due to the sorting operation.
Space Complexity: O(n), as the sorted strings are created.
The function uses the sorted() function to sort the characters in both s1 and s2. 
Sorting the characters ensures that if two strings are anagrams, their sorted versions will be identical.
'''

def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

'''
Count Occurrences:
Write a function that takes a string and a target character as input and returns the count of occurrences of the target character in the string.

Time Complexity: O(n), where n is the length of the string.
Space Complexity: O(1), as only a single integer variable is used.
'''

def count_occurrences(s, target):
    count = 0
    for char in s:
        if char == target:
            count += 1
    return count

'''
Longest Substring without Repeating Characters:
Given a string, find the length of the longest substring without repeating characters.

Time Complexity: O(n), where n is the length of the string.
Space Complexity: O(min(n, m)), where m is the size of the character set. 
In the worst case, the entire string could be unique, requiring O(n) space.
'''

def length_of_longest_substring(s):
    seen = {}
    start = 0
    max_length = 0
    for end in range(len(s)):
        if s[end] in seen:
            start = max(start, seen[s[end]] + 1)
        seen[s[end]] = end
        max_length = max(max_length, end - start + 1)
    return max_length
