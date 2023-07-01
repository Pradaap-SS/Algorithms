def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursive calls to sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Merge the sorted halves
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Append the remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

arr = [4, 2, 7, 1, 9, 5]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)


'''
Time Complexity:
The time complexity of Merge Sort is O(n log n) in all cases, where n is the number of elements in the array. It divides the array into halves recursively and merges them back in sorted order. The divide step takes O(log n) time, and the merge step takes O(n) time. Therefore, the overall time complexity is O(n log n).

Space Complexity:
The space complexity of Merge Sort is O(n) because it creates temporary arrays during the merge step to store the sorted elements. The space required is proportional to the size of the input array.
'''