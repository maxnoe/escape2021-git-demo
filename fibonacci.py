from functools import cache


@cache
def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fib_gen(n):
    for i in range(n):
        yield fibonacci(n)

if __name__ == "__main__":
    print(fibonacci(35))
