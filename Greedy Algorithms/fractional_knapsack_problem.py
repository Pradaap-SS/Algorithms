'''
Fractional Knapsack Problem:
The Fractional Knapsack problem involves maximizing the value of items that can be put into a knapsack with a 
limited weight capacity. Each item has a weight and a value, and we can take fractions of items.
'''

class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x.value / x.weight, reverse=True)  # Sort items by value/weight ratio
    
    total_value = 0.0
    for item in items:
        if capacity >= item.weight:
            total_value += item.value
            capacity -= item.weight
        else:
            fraction = capacity / item.weight
            total_value += item.value * fraction
            break
    
    return total_value


items = [Item(10, 60), Item(20, 100), Item(30, 120)]
capacity = 50
print(fractional_knapsack(items, capacity))

'''
Time Complexity: The time complexity of this algorithm is O(n log n), where n is the number of items. 
Sorting the items based on value/weight ratio takes O(n log n) time.

Space Complexity: The space complexity is O(1) because the algorithm uses a constant amount of 
additional space to store the total_value and capacity.
'''
