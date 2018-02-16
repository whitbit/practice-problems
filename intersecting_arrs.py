from collections import Counter

def intersect(nums1, nums2):
    # build counts dict for each arr
    c1, c2 = Counter(nums1), Counter(nums2)

    # convert matching dicts keys and counts back to list
    print list((c1&c2).elements())

intersect([1, 2, 2, 1], [2, 2, 1])