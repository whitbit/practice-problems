def print_recursively(lst):
    """Print items in the list, using recursion."""

    if lst:
        print lst[-1]
        print_recursively(lst[:-1])

print_recursively([1,2,3])

# def print_recursively(lst):
#     """Print items in the list, using recursion."""

#     # START SOLUTION

#     if lst:
#         print lst[0]
#         print_recursively(lst[1:])