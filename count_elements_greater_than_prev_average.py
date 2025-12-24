#!/bin/python3
#
# Complete the 'countResponseTimeRegressions' function below.
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY responseTimes as parameter.

def countResponseTimeRegressions(arr):
    if not arr:
        return 0
    
    count = 0
    running_sum = arr[0] # Start with the first element
    
    # Start loop from the second element (index 1)
    for i in range(1, len(arr)):
        # Previous average = running_sum / i
        if arr[i] > (running_sum / i):
            count += 1
        
        # Update running sum for the next iteration
        running_sum += arr[i]
        
    return count

arr = [10, 20, 15, 25, 30]
print(countResponseTimeRegressions(arr))

#soltuion 2:
def count_elements(n, arr):
    # If there's only one element or none, 
    # there are no previous elements to average.
    if n <= 1:
        return 0
    
    count = 0
    running_sum = arr[0]
    
    # We start at 1 (the 2nd element) and go up to n-1
    for i in range(1, n):
        # Check if current element > average of all previous elements
        # Using (running_sum / i) because 'i' also represents 
        # the count of elements seen so far.
        if arr[i] > (running_sum / i):
            count += 1
        
        # Add current element to sum for the next iteration's average
        running_sum += arr[i]
        
    return count