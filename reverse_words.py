# def reverse_string(s):
    
#     for i in range(len(s)/2):
#         temp = s[i]
#         s[i] = s[i-1]
#         s[i-1] = temp

#     return s
def rev_str(s, start, end):
    s = list(s)

    if s == None or len(s) < 2:
        return

    while(start < end):
        temp = s[start]
        s[start] = s[end]
        s[end] = temp

        start += 1
        end -= 1

    return s

def rev_sentence(sentence):
    reversed_s = rev_str(sentence, 0, len(sentence)-2)

    # iterate through items
    # when we hit a space
    # stop and reverse

    start = 0
    end = 0

    while True:
        try:
            while(reversed_s[start] == ' '):
                start += 1
                # print start
        except IndexError:
            continue
        
        end = start + 1
        
        try:
            while reversed_s[end] != ' ':
                end += 1
        except IndexError:
            continue

        rev_str(reversed_s, start, end-1)
        print reversed_s

        start = end
    print reversed_s

    return reversed_s

print rev_sentence('hello world!')