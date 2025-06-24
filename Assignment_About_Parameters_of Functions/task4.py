# DP approach for Fibonacci, getting time complexity of o(n)
def nth_fin_dp(nth: int, memo: dict[int, int] | None = None) -> int:
    if memo is None:
        memo = {}

    if nth in memo:
        return memo[nth]

    if nth < 0:
        raise ValueError("cannot be negative!")
    if nth ==0:
        return 0
    if nth == 1:
        return 1
    # memorize
    memo[nth] = nth_fin_dp(nth - 1, memo) + nth_fin_dp(nth - 2, memo)
    return memo[nth]

# simple but expensive, since time complexity is o(n^2)
def nth_fibonacci(nth: int) -> int:
    if nth < 0:
        raise ValueError("cannot be negative!")
    if nth ==0:
        return 0
    if nth == 1:
        return 1
    return nth_fibonacci(nth - 1) + nth_fibonacci(nth - 2)

def factorial(num: int) -> int:
    if num < 0:
        raise ValueError("cannot be negative!")
    if num in (0, 1):
        return 1
    return num * factorial(num - 1)

def main():
    number = 5
    result = factorial(number)
    nth = 6
    result_nth_factorial = nth_fibonacci(nth)
    print(f"Factorial of {number} is {result}. "
          f"The {nth}th Fibonacci number is {result_nth_factorial}.")

    # test DP Fibonacci
    # print(f"DP Fibonacci is {nth_fin_dp(nth)}")
if __name__ == "__main__":
    main()