'''
Longest Common Subsequence (LCS):
The Longest Common Subsequence problem involves finding the longest subsequence common to two sequences (strings). 
A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing 
the order of the remaining elements. The dynamic programming approach for the LCS problem involves building a table 
that stores the length of the LCS for each pair of prefixes from the two sequences.
'''

def longest_common_subsequence(text1, text2):
    m = len(text1)
    n = len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

text1 = "ABCBDAB"
text2 = "BDCAB"
lcs_length = longest_common_subsequence(text1, text2)
print("Length of LCS:", lcs_length)

'''Length of LCS: 4'''


'''
Time Complexity: The time complexity of the LCS algorithm using dynamic programming is O(m * n) since it 
iterates over m rows and n columns of the DP table.

Space Complexity: The space complexity is O(m * n) since it requires a 2D array of size (m+1) * (n+1) to 
store the computed values.
'''