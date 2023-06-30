def selection_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # Find the minimum element in the unsorted part of the array
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Swap the minimum element with the current element
        arr[i], arr[min_index] = arr[min_index], arr[i]

arr = [4, 2, 7, 1, 9, 5]
selection_sort(arr)
print("Sorted array:", arr)

'''
Time Complexity:
The time complexity of Selection Sort is O(n^2) in the average and worst cases, where n is the number of elements in the array. It involves two nested loops that iterate over the array, resulting in a quadratic time complexity.

Space Complexity:
The space complexity of Selection Sort is O(1) because it only uses a constant amount of extra space to store variables like i, j, and min_index.
'''