def heap_sort(arr):
    n = len(arr)
    
    # Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap root (max element) with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap

def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    # Find the largest element among the root and its children
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap root with the largest element
        heapify(arr, n, largest)  # Recursively heapify the affected subtree

arr = [4, 2, 7, 1, 9, 5]
heap_sort(arr)
print("Sorted array:", arr)

'''
Time Complexity:
The time complexity of Heap Sort is O(n log n) in all cases, where n is the number of elements in the array. Building the heap takes O(n) time, and each heapify operation takes O(log n) time. Since heapify is performed for each element, the overall time complexity is O(n log n).

Space Complexity:
The space complexity of Heap Sort is O(1) because it only uses a constant amount of extra space for variables like n, i, largest, left, and right. The sorting is performed in place, without requiring additional memory proportional to the input size.
'''