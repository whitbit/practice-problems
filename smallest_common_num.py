arr1 = [6, 7, 10, 25, 30, 63, 64]
arr2 = [-1, 4, 5, 6, 7, 8, 50]
arr3 = [1, 6, 10, 14]

def find_smallest_common_num_bf(arr1, arr2, arr3):
    # O(n^3) time complexity
    # O(1) space complexity
    common_num = -1

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                for k in range(len(arr3)):
                    if arr1[i] == arr3[k]:
                        common_num = arr1[i]

    return common_num


def find_smallest_common_num(arr1, arr2, arr3):
    # O(n) time complexity
    # O(1) space complexity

    i = 0
    j = 0
    k = 0

    while(i < len(arr1)
         and j < len(arr2)
         and k < len(arr3)):

        if arr1[i] == arr2[j] == arr3[k]:
            return arr1[i]

        else:
            if arr1[i] < arr2[j] and arr1[i] < arr3[k]:
                i += 1
            elif arr2[j] < arr1[i] and arr2[j] < arr3[k]:
                j += 1
            else:
                k += 1
    return -1

print find_smallest_common_num(arr1, arr2, arr3)