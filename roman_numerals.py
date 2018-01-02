translate = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100
}

def translate_rn(s):

    total = 0

    for i in range(len(s)):
        num = translate[s[i]]

        try:
            next_num = translate[s[i+1]]
            
            if num > next_num or num == next_num:
                total += num
            elif num < next_num:
                total -= num
        except IndexError:
            total += num

    return total

print translate_rn('LXXXVI')
