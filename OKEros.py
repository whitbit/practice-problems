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


def get_rectangular_intersection(rect1, rect2):
    """

    Find rectangular intersection of two given love rectangles.
    Rectangles are defined as dictionaries.

    """

def find_x_overlap(rect1, rect2):

    first_x_range = (rect1['left_x'], rect1['left_x'] + rect1['width'])
    print first_x_range

    second_x_range = (rect2['left_x'], rect2['left_x'] + rect2['width'])
    print second_x_range

    if first_x_range[1] <= second_x_range[0]:
        return 'No overlap'

    return (max(first_x_range[0], second_x_range[0]),
            min(first_x_range[1], second_x_range[1]))

print find_x_overlap(my_rectangle, my_rectangle2)

def find_x_overlap(x1, width1, x2, width2):
    highest_start_point = max(x1, x2)
    lowest_end_point
    