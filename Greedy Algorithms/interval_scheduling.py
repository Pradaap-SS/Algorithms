'''
Interval Scheduling:
Interval Scheduling is a greedy algorithm that selects the maximum number of non-overlapping intervals 
from a given set of intervals with their start and end times.
'''

def interval_scheduling(intervals):
    n = len(intervals)
    selected_intervals = []
    
    # Sort intervals by end time
    sorted_intervals = sorted(intervals, key=lambda x: x[1])
    
    # Select the first interval
    selected_intervals.append(sorted_intervals[0])
    last_end = sorted_intervals[0][1]
    
    # Iterate through the remaining intervals
    for i in range(1, n):
        if sorted_intervals[i][0] >= last_end:
            selected_intervals.append(sorted_intervals[i])
            last_end = sorted_intervals[i][1]
    
    return selected_intervals

# Example usage:
intervals = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 8), (5, 9), (6, 10), (8, 11)]
selected_intervals = interval_scheduling(intervals)
print(selected_intervals)


'''
Time Complexity: The time complexity of this algorithm is O(n log n), where n is the number of intervals. 
Sorting the intervals by end time takes O(n log n) time.

Space Complexity: The space complexity is O(n) because the algorithm uses additional space to store the selected 
intervals.'''