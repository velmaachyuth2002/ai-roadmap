from time import perf_counter


naive_calls = 0
memo_calls = 0


# 1. Naive Fibonacci O(2^n)
def fib_naive(n):
    global naive_calls
    naive_calls += 1

    if n <= 1:
        return n

    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n, memo=None):
    global memo_calls
    memo_calls += 1

    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)

    return memo[n]



def fib_tab(n):
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]



def climb_stairs(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


naive_calls = 0

start = perf_counter()
print("fib_naive(30):", fib_naive(30))
end = perf_counter()

print("Naive calls:", naive_calls)
print("Naive time:", end - start)



memo_calls = 0

start = perf_counter()
print("fib_memo(30):", fib_memo(30))
end = perf_counter()

print("Memo calls:", memo_calls)
print("Memo time:", end - start)



print("fib_tab(10):", fib_tab(10))

print("climb_stairs(5):", climb_stairs(5))
print("climb_stairs(1):", climb_stairs(1))
print("climb_stairs(2):", climb_stairs(2))



print(fib_tab(5000))       