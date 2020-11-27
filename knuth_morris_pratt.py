def circl_shift(word, shift):
    return word[-shift:] + word[:-shift]


def prefix_suffix(string):
    if not string:
        return 0
    arr = [0] * (len(string) + 1)
    for i in range(2, len(arr)):
        arr[i] = arr[i - 1]
        while string[i - 1] != string[arr[i]] and arr[i] > 0:
            arr[i] = arr[arr[i]]
        if string[i - 1] == string[arr[i]]:
            arr[i] += 1
    max_suffix_prefix = arr[-1]
    max_match = max(arr)
    max_match_index = arr.index(max_match)
    return max_suffix_prefix, max_match, max_match_index


def knuth_morris_pratt(string, pattern):
    if not string and not pattern:
        return 0
    elif not string or not pattern:
        return -1
    new_string = string + '$' + pattern + pattern
    _, max_match, max_match_index = prefix_suffix(new_string)
    max_match_index -= len(string) + 1
    shift = max_match_index - len(string)
    if circl_shift(string, shift) == pattern:
        return shift
    else:
        return -1

if __name__ == '__main__':
    s = 'aaabaaa'
    p = 'aabaaaa'
    print('Test #1 is','Ok' if knuth_morris_pratt(s, p) == 6 else 'Fail')
    s = 'aaabaa'
    p = 'aabaaaa'
    print('Test #2 is','Ok' if knuth_morris_pratt(s, p) == -1 else 'Fail')
    s = 'abcde'
    p = 'eabcd'
    print('Test #3 is','Ok' if knuth_morris_pratt(s, p) == 1 else 'Fail')
    s = 'abcde'
    p = 'abcda'
    print('Test #4 is','Ok' if knuth_morris_pratt(s, p) == -1 else 'Fail')
    s = 'abcdefgh'
    p = 'fghabcde'
    print('Test #5 is','Ok' if knuth_morris_pratt(s, p) == 3 else 'Fail')

