# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def count_construct(target, word_bank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return 1
    total_count = 0;
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):len(target)]
            number_of_ways_for_rest = count_construct(suffix, word_bank, memo)
            total_count = total_count + number_of_ways_for_rest

    memo[target] = total_count
    return total_count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(count_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
    print(count_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(count_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(count_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
    print(count_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                          ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
