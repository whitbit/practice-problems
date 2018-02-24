
def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """
    # Your code here!
    def helper(needle, haystack, index):
        print "Looking for %s in %s at index %d" % (needle, haystack, index)
        if index >= len(haystack):
            print " Not found!  Returning none"
            return None
        
        if needle == haystack[index]:
            print " Found! Returning %d" % index
            return index
        
        print " Not found YET, recursing."
        return helper(needle, haystack, index + 1)
    
    return helper(needle, haystack, 0)



def recursive_index(needle, haystack):
    """Given list (haystack), return index (0-based) of needle in the list.

    Return None if needle is not in haystack.

    Do this with recursion. You MAY NOT USE A `for` OR `while` LOOP.
    """
    # Your code here!
    if len(haystack) < 1:
        return None
    
    if needle == haystack[0]:
        return 0
    
    index = recursive_index(needle, haystack[1:])
    
    
    if index is not None:
        return index + 1
    
    