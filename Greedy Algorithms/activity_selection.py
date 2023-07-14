'''Activity Selection:
Activity Selection is a greedy algorithm that selects the maximum number of non-overlapping activities 
that can be performed from a given set of activities with their start and finish times.
'''

def activity_selection(start, finish):
    n = len(start)
    activities = []
    
    # Sort activities by finish time
    sorted_activities = sorted(zip(start, finish), key=lambda x: x[1])
    
    # Select the first activity
    activities.append(sorted_activities[0])
    last_finish = sorted_activities[0][1]
    
    # Iterate through the remaining activities
    for i in range(1, n):
        if sorted_activities[i][0] >= last_finish:
            activities.append(sorted_activities[i])
            last_finish = sorted_activities[i][1]
    
    return activities

start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]
activities = activity_selection(start, finish)
print(activities)

'''
Time Complexity: The time complexity of this algorithm is O(n log n), where n is the number of activities. 
Sorting the activities by finish time takes O(n log n) time.

Space Complexity: The space complexity is O(n) because the algorithm uses additional space to store the selected 
activities.
'''
