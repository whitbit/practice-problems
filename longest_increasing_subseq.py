def LIS(arr):
    j, i, t = 0, 1, [1] * len(arr)  # initialize ints j, i and array t
    
    while i < len(arr):  # loop while i is within the sequence's bounds
        if arr[j] < arr[i]:
            t[i] = max(t[i], t[j] + 1)  # exact same logic Tushar wrote at the end of video
        j = j + 1  # at each iteration, increment j
        
        if j == i:
            j, i = 0, i + 1  # if j meets i, set j to 0 and increment i
            
    return max(t)﻿