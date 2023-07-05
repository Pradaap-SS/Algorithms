def naive_pattern_match(text, pattern):
    n = len(text)
    m = len(pattern)
    
    for i in range(n - m + 1):
        j = 0
        while j < m:
            if text[i + j] != pattern[j]:
                break
            j += 1
        if j == m:
            return i
    
    return -1

text = "Hello, world!"
pattern = "world"
index = naive_pattern_match(text, pattern)
print("Pattern found at index:", index)

'''
Time Complexity: The worst-case time complexity of the Naive algorithm is O((n - m + 1) * m), where n is the length of the text and m is the length of the pattern.

Space Complexity: The space complexity is O(1) since it only requires a constant amount of extra space.
'''