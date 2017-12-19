def find_rotation_pt(words):

    first_word = words[0]
    flr_idx = 0
    ceiling_idx = len(words) - 1

    if words[ceiling_idx] > first_word:
        return 0

    while flr_idx < ceiling_idx:
        guess_idx = flr_idx + ((ceiling_idx-flr_idx)//2)

        if words[guess_idx] >= first_word:
            flr_idx = guess_idx
        else:
            ceiling_idx = guess_idx

        if flr_idx + 1 == ceiling_idx:
            return ceiling_idx

    return 0