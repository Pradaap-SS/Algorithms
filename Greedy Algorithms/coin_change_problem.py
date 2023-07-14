'''
Coin Change Problem:
The Coin Change problem involves finding the minimum number of coins needed to make a certain amount of change. 
We are given a set of coin denominations and an amount, and we need to determine the minimum number of coins required 
to make that amount.
'''

def coin_change(coins, amount):
    coins.sort(reverse=True)  # Sort coins in descending order
    
    count = 0
    for coin in coins:
        if coin <= amount:
            count += amount // coin
            amount %= coin
        if amount == 0:
            break
    
    if amount == 0:
        return count
    else:
        return -1  # If exact change cannot be made


coins = [1, 5, 10, 25]
amount = 47
print(coin_change(coins, amount))


'''
Time Complexity: The time complexity of this algorithm is O(n), where n is the number of coins. 
Sorting the coins takes O(n log n) time, but the loop that iterates through the coins has a time complexity of O(n) 
since we consider each coin only once.

Space Complexity: The space complexity is O(1) because the algorithm uses a constant amount of additional 
space to store the count and amount.
'''
