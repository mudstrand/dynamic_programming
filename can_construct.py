# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import copy


def can_construct(target_sum, numberlist, memo=None):
    if memo is None:
        memo = {}
    if target_sum in memo:
        return memo[target_sum]
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    shortest_combination = None
    for num in numberlist:
        remainder = target_sum - num
        remainder_combination = can_construct(remainder, numberlist, memo)
        if remainder_combination is not None:
            remainder_combination_copy = copy.deepcopy(remainder_combination)
            remainder_combination_copy.append(num)
            combination = remainder_combination_copy
            if (shortest_combination is None) or (len(combination) < len(shortest_combination)):
                shortest_combination = combination

    memo[target_sum] = shortest_combination
    return shortest_combination


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print(can_construct(7, [5, 3, 4, 7]))
    # print(can_construct(8, [2, 3, 5]))
    print(can_construct(8, [1, 4, 5]))
    print(can_construct(100, [1, 2, 5, 25]))
    # print(can_construct(308, [6, 14, 20]))
