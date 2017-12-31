def merge_ranges(meeting_times):

    """
    Takes a list of meeting time ranges and retursn a list of condensed ranges.
    Solution should be efficient even if we don't have a nice upper bound.

    >>> merge_ranges([(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)])
    [(0, 1), (3, 8), (9, 12)]

    >>> merge_ranges([(1, 3), (2, 4)])
    [(1, 4)]

    """
    sorted_times = sorted(meeting_times)

    merged_meetings = [sorted_times[0]]

    for current_meeting_start, current_meeting_end in sorted_times[1:]:
        last_merged_meeting_start, last_merged_meeting_end = merged_meetings[-1]

        if (current_meeting_start <= last_merged_meeting_end):
            merged_meetings[-1] = (last_merged_meeting_start, 
                                  max(last_merged_meeting_end, current_meeting_end))

        else:
            merged_meetings.append((current_meeting_start, current_meeting_end))

    return merged_meetings

if __name__ == '__main__':
    import doctest
    doctest.testmod()

