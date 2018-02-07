from collections import deque

def find_max_sliding_window(arr, window_size):
    maxes = []

    window = deque()

    for i in range(window_size):
        while window and arr[i] >= arr[window[-1]]:
            window.pop()
        window.append(i)
    maxes.append(arr[window[0]])

    for i in range(window_size, len(arr)):
        while window and arr[i] >= arr[window[-1]]:
            window.pop()
        if window and (window[0] <= i - window_size):
            i = 5
            window[0] = 5
            window.popleft()
        window.append(i)

        maxes.append(arr[window[0]])
    
    return maxes

print find_max_sliding_window([-4, 2, -5, 1, -1, 6], 3)


def find_max_sliding_window_brute_force(arr, window_size):

    maxes = []

    for i in range(len(arr) - window_size+1):
        maxes.append(max(arr[i:i+window_size]))

    return maxes

print find_max_sliding_window_brute_force([-4, 2, -5, 1, -1, 6], 3)

