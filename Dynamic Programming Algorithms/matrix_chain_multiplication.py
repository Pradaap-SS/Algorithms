'''
Matrix Chain Multiplication:
The Matrix Chain Multiplication problem involves finding the most efficient way to multiply a given sequence of matrices. 
The goal is to minimize the number of scalar multiplications required. The dynamic programming approach for the 
Matrix Chain Multiplication problem involves building a table that stores the optimal costs for multiplying different 
matrix subsequences.
'''

def matrix_chain_multiplication(dims):
    n = len(dims)
    dp = [[0] * n for _ in range(n)]
    
    for chain_len in range(2, n):
        for i in range(1, n - chain_len + 1):
            j = i + chain_len - 1
            dp[i][j] = float('inf')
            
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + dims[i - 1] * dims[k] * dims[j]
                dp[i][j] = min(dp[i][j], cost)
    
    return dp[1][n - 1]

dimensions = [10, 30, 5, 60]
min_cost = matrix_chain_multiplication(dimensions)
print("Minimum cost of matrix multiplication:", min_cost)


'''Minimum cost of matrix multiplication: 4500'''

'''
Time Complexity: The time complexity of the Matrix Chain Multiplication algorithm using dynamic programming is O(n^3) 
since it iterates over the chains of different lengths in nested loops.

Space Complexity: The space complexity is O(n^2) since it requires a 2D array of size n * n to store the computed values.
'''