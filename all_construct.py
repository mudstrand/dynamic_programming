# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def all_construct(target, word_bank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return [[]]

    result = []

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):len(target)]
            suffix_ways = all_construct(suffix, word_bank, memo)
            target_ways = []
            for suffix_way in suffix_ways:
                target_way = [word] + suffix_way
                target_ways.append(target_way)
            result = result + target_ways
    memo[target] = result
    return result


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(all_construct('purple', ['purp', 'p', 'ur', 'le', 'purpl']) )
    print(all_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd', 'ef', 'c']))
    print(all_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(all_construct('aaaaaaaaaaaaaaaaaaaaaaaaaz',
                        ['a', 'aa', 'aaa', 'aaaa', 'aaaaa', 'aaaaaa']))
