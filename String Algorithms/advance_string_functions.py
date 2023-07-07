'''
Longest Palindromic Substring:
Given a string, find the longest substring that is a palindrome. 
A palindrome is a string that reads the same forwards and backwards.'''

def longest_palindromic_substring(s):
    if not s:
        return ""

    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    longest = ""
    for i in range(len(s)):
        # For odd-length palindromes
        palindrome_odd = expand_around_center(s, i, i)
        if len(palindrome_odd) > len(longest):
            longest = palindrome_odd

        # For even-length palindromes
        palindrome_even = expand_around_center(s, i, i + 1)
        if len(palindrome_even) > len(longest):
            longest = palindrome_even

    return longest

'''
String Compression:
Implement a method to perform basic string compression using the counts of repeated characters. 
For example, the string "aabcccccaaa" would become "a2b1c5a3". 
If the compressed string is not smaller than the original string, return the original string.'''

def compress_string(s):
    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + str(count))
            count = 1

    compressed.append(s[-1] + str(count))
    compressed_string = "".join(compressed)

    return compressed_string if len(compressed_string) < len(s) else s

''' 
Valid Parentheses:
Given a string containing only the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid. An input string is valid if:

Open brackets are closed by the same type of brackets.
Open brackets are closed in the correct order.
An empty string is also considered valid.'''

def is_valid_parentheses(s):
    stack = []
    brackets = {"(": ")", "{": "}", "[": "]"}

    for char in s:
        if char in brackets:
            stack.append(char)
        elif char in brackets.values():
            if not stack or brackets[stack.pop()] != char:
                return False

    return not stack

'''
Word Break:
Given a non-empty string s and a dictionary containing a list of non-empty words, 
determine if s can be segmented into a space-separated sequence of one or more dictionary words.
'''
def word_break(s, word_dict):
    n = len(s)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_dict:
                dp[i] = True
                break

    return dp[n]


'''
Regular Expression Matching:
Implement regular expression matching with support for '.' (matches any single character) and '*' 
(matches zero or more of the preceding element). The matching should cover the entire input string, 
not partial matching.
'''

def is_match(s, p):
    if not p:
        return not s

    first_match = bool(s) and p[0] in {s[0], "."}

    if len(p) >= 2 and p[1] == "*":
        return (is_match(s, p[2:]) or
                first_match and is_match(s[1:], p))
    else:
        return first_match and is_match(s[1:], p[1:])