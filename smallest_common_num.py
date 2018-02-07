def find_smallest_common_num(arr1, arr2, arr3):

    common_num = -1

    for i in range(len(arr1)):
        for j in range(len(arr2)):
            if arr1[i] == arr2[j]:
                for k in range(len(arr3)):
                    if arr1[i] == arr3[k]:
                        common_num = arr1[i]

    return common_num

arr1 = [5, 7, 10, 25, 30, 63, 64]
arr2 = [-1, 4, 5, 6, 7, 8, 50]
arr3 = [1, 6, 10, 14]

print find_smallest_common_num(arr1, arr2, arr3)