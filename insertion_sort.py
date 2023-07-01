def insertion_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        
        # Move elements greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

arr = [4, 2, 7, 1, 9, 5]
insertion_sort(arr)
print("Sorted array:", arr)

'''
Time Complexity:
The time complexity of Insertion Sort is O(n^2) in the average and worst cases, where n is the number of elements in the array. It involves two nested loops. However, it has a best-case time complexity of O(n) when the input array is already sorted.

Space Complexity:
The space complexity of Insertion Sort is O(1) because it only uses a constant amount of extra space to store variables like i, j, key, and temporary variables for shifting elements.
'''