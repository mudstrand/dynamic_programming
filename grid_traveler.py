# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


memo = {}

def grid_traveler(m, n, memo):
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    if m == 1 and n == 1:
        return 1
    if m == 0 or n == 0:
        return 0
    memo[key] = grid_traveler(m - 1, n, memo) + grid_traveler(m, n - 1, memo)
    return memo[key]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(grid_traveler(1, 1, memo))
    memo.clear()
    print(grid_traveler(2, 3, memo))
    memo.clear()
    print(grid_traveler(3, 2, memo))
    memo.clear()
    print(grid_traveler(3, 3, memo))
    memo.clear()
    print(grid_traveler(18, 18, memo))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
