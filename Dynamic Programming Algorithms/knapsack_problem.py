'''
Knapsack Problem:
The Knapsack problem is a classic optimization problem where we have a set of items, each with a weight and value, 
and a knapsack with a maximum weight capacity. The goal is to maximize the total value of items in the knapsack without 
exceeding its weight capacity. The dynamic programming approach for the Knapsack problem involves building a table that
stores the maximum value achievable for each combination of items and capacities.
'''

def knapsack(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(values[i - 1] + dp[i - 1][j - weights[i - 1]], dp[i - 1][j])
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][capacity]

weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 7
max_value = knapsack(weights, values, capacity)
print("Maximum value:", max_value)

'''Maximum value: 10'''

'''
Time Complexity: The time complexity of the Knapsack algorithm using dynamic programming is O(n * capacity) since 
it iterates over n items and each iteration considers all capacities up to the given capacity.

Space Complexity: The space complexity is O(n * capacity) since it requires a 2D array of size (n+1) * (capacity+1) 
to store the computed values.
'''