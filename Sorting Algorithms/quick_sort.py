def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # Choose the pivot element
    smaller, equal, larger = [], [], []
    
    for num in arr:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)
    
    return quick_sort(smaller) + equal + quick_sort(larger)

arr = [4, 2, 7, 1, 9, 5]
sorted_arr = quick_sort(arr)
print("Sorted array:", sorted_arr)


'''
Time Complexity:
The time complexity of Quick Sort depends on the choice of the pivot element and the partitioning of the array. In the average and best cases, it has a time complexity of O(n log n), where n is the number of elements in the array. However, in the worst case (when the pivot is always the smallest or largest element), it has a time complexity of O(n^2). The average case time complexity is commonly encountered in practice.

Space Complexity:
The space complexity of Quick Sort is O(n) due to the recursive calls and the space required for the smaller, equal, and larger lists. In the worst case, it can require O(n) extra space for the call stack. However, with optimizations like tail recursion elimination or using an iterative approach, the space complexity can be reduced to O(log n).
'''