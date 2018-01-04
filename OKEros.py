my_rectangle = {
    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 1,

    # width and height
    'width': 6,
    'height': 3,
}

my_rectangle2 = {
    # coordinates of bottom-left corner
    'left_x': 2,
    'bottom_y': 1,

    # width and height
    'width': 4,
    'height': 3,
}

def find_range_overlap(point1, length1, point2, length2):
    """
    Find overlap of x and y on a 1-D line.

    """
    highest_start_point = max(point1, point2)
    lowest_end_point = min(point1 + length1, point2 + length2)

    if highest_start_point >= lowest_end_point:
        return (None, None)

    overlap_length = lowest_end_point - highest_start_point

    return (highest_start_point, overlap_length)
    

def find_rectangular_overlap(rect1, rect2):
    """
    >>> find_rectangular_overlap(my_rectangle, my_rectangle2) == { 'left_x': 2, 'bottom_y': 1, 'width': 4, 'height': 3}
    True

    """

    x_overlap_point, x_overlap_width = find_range_overlap(
        rect1['left_x'], rect1['width'], rect2['left_x'], rect2['width'])
    y_overlap_point, y_overlap_height = find_range_overlap(
        rect1['bottom_y'], rect1['height'], rect2['bottom_y'], rect2['height'])

    if not x_overlap_width or not y_overlap_height: 
        return {
            'left_x': None,
            'bottom_y': None,
            'width': None,
            'height': None
        }

    return {
        'left_x': x_overlap_point,
        'bottom_y': y_overlap_point,
        'width': x_overlap_width,
        'height': y_overlap_height
    }


if __name__ == '__main__':
    import doctest
    doctest.testmod()