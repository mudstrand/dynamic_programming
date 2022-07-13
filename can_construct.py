# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def can_construct(target, word_bank, memo=None):
    if memo is None:
        memo = {}
    if target in memo:
        return memo[target]
    if target == '':
        return True
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word):len(target)]
            if can_construct(suffix, word_bank, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(can_construct('abcdef', ['ab', 'abc', 'cd', 'def', 'abcd']))
    print(can_construct('skateboard', ['bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
    print(can_construct('enterapotentpot', ['a', 'p', 'ent', 'enter', 'ot', 'o', 't']))
    print(can_construct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef',
                        ['e', 'ee', 'eee', 'eeee', 'eeeee', 'eeeeee']))
