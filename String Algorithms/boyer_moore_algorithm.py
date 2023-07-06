def compute_bad_character_table(pattern):
    table = {}
    m = len(pattern)
    
    for i in range(m - 1):
        table[pattern[i]] = m - 1 - i
    
    return table

def boyer_moore_pattern_match(text, pattern):
    n = len(text)
    m = len(pattern)
    table = compute_bad_character_table(pattern)
    
    i = m - 1
    j = m - 1
    
    while i < n:
        if text[i] == pattern[j]:
            if j == 0:
                return i
            i -= 1
            j -= 1
        else:
            skip = table.get(text[i], m)
            i += m - min(j, 1 + skip)
            j = m - 1
    
    return -1

text = "Hello, world!"
pattern = "world"
index = boyer_moore_pattern_match(text, pattern)
print("Pattern found at index:", index)

'''
Time Complexity: The time complexity of the Boyer-Moore algorithm is generally considered as O(n + m), where n is the length of the text and m is the length of the pattern. However, in certain cases, it can exhibit a best-case complexity of O(n/m) when there are mismatches in the text and pattern occur far apart.

Space Complexity: The space complexity is O(m) since it requires additional space for the bad character table.
'''