from collections import deque

def find_max_sliding_window(arr, window_size):

    window = deque()

    for i in range(window_size):
        while window and arr[i] >= arr[window[-1]]:
            window.pop()
        window.append(i)
    # print arr[window[0]]

    for i in range(window_size, len(arr)):
        while window and arr[i] >= arr[window[-1]]:
            window.pop()
        if window and (window[0] <= i - window_size):
            i = 5
            window[0] = 5
            window.popleft()
        window.append(i)

        print arr[window[0]]

find_max_sliding_window([-4, 2, -5, 1, -1, 6], 3)