# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

memo = {}

def fib(n, memo):
    if n in memo:
        return memo[n]
    if n < 2:
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(fib(50, memo))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
