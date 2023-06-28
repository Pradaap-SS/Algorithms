def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # Return the index of the target if found
    return -1  # Return -1 if the target is not found

# Example 
my_list = [4, 7, 2, 9, 1, 5]
target_number = 9

result = linear_search(my_list, target_number)
if result != -1:
    print("Target found at index:", result)
else:
    print("Target not found in the list.")