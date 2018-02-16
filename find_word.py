def find_word_idx(word, arr):

    if word == arr[0]:
        return 0

    return 1 + find_word_idx(word, arr[1:])

print find_word_idx('fish', ['hello', 'world', 'one', 'fish']) == 3