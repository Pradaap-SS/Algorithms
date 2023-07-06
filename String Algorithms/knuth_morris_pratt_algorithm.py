def compute_lps_array(pattern):
    m = len(pattern)
    lps = [0] * m
    
    i = 0
    j = 1
    
    while j < m:
        if pattern[i] == pattern[j]:
            i += 1
            lps[j] = i
            j += 1
        else:
            if i != 0:
                i = lps[i - 1]
            else:
                lps[j] = 0
                j += 1
    
    return lps

def kmp_pattern_match(text, pattern):
    n = len(text)
    m = len(pattern)
    lps = compute_lps_array(pattern)
    
    i = 0
    j = 0
    
    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == m:
                return i - j
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return -1

text = "Hello, world!"
pattern = "world"
index = kmp_pattern_match(text, pattern)
print("Pattern found at index:", index)


'''
Time Complexity: The time complexity of the KMP algorithm is O(n + m), where n is the length of the text and m is the length of the pattern. The algorithm preprocesses the pattern to compute the Longest Proper Prefix which is also a Suffix (LPS) array in O(m) time, and then performs a single pass over the text to find matches.

Space Complexity: The space complexity of the KMP algorithm is O(m) since it requires additional space for the LPS array.
'''