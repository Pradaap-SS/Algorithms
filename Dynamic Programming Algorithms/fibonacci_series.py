'''
Fibonacci Sequence:
The Fibonacci sequence is a sequence of numbers in which each number is the sum of the two preceding ones. 
The Fibonacci sequence can be defined as F(n) = F(n-1) + F(n-2), with F(0) = 0 and F(1) = 1 as the base cases. 
The dynamic programming approach for computing the Fibonacci sequence involves storing the previously computed values 
to avoid redundant calculations.
'''

def fibonacci(n):
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]

n = 6
fib = fibonacci(n)
print("Fibonacci of", n, ":", fib)

'''
Time Complexity: The time complexity of the Fibonacci algorithm using dynamic programming is O(n) since it 
computes the Fibonacci sequence in a bottom-up manner.

Space Complexity: The space complexity is O(n) since it requires an additional array of size n+1 to store 
the computed values.
'''