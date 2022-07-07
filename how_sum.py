# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def how_sum(target_sum, numbers, memo=None):
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for num in numbers:
        remainder = target_sum - num
        result = how_sum(remainder, numbers, memo)
        if result is not None:
            memo[target_sum] = result.append(num)
            return result
    memo[target_sum] = None
    return None


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(how_sum(7, [2, 3]))
    print(how_sum(7, [5, 3, 4, 7]))
    print(how_sum(7, [2, 4]))
    print(how_sum(8, [2, 3, 5]))
    print(how_sum(300, [7, 14]))
    print(how_sum(308, [6, 14, 20]))
