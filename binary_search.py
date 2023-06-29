def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid + 1  # Found the target at index mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found


arr = [1, 2, 4, 5, 7, 9]
target = 7
index = binary_search(arr, target)
if index != -1:
    print("Target found at index:", index)
else:
    print("Target not found")


''' Time Complexity:
The time complexity of binary search is O(log n), where n is the number of elements in the sorted array. In each iteration, the search space is halved, resulting in a logarithmic time complexity. It is efficient for large arrays compared to linear search.

Space Complexity:
The space complexity of binary search is O(1) because it does not require any extra space that grows with the input size. It only uses a fixed amount of space to store the variables low, high, and mid.

'''