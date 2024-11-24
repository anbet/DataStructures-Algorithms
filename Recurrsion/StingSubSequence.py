# Populate substing with all the possible combination of alphabets in the string
# Example string=abc
# substring: a, ab, ac, b, bc, c, cb, ''

def get_subsequences(word):
    # base condition
    if len(word) == 0:
        return ''

    first = word[0]
    rest = get_subsequences(word[1:])

    result = ''
    # Recurring condition
    for substr in rest.split(','):
        result += ',' + first + substr
        result += ',' + substr

    result = result[1:]

    return result

substr = get_subsequences("abc")
print(substr)