from functools import cache


@cache
def fibonacci(n):
    '''
    Calculate the nth fibonacci number using recursion
    and memoization.
    '''
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def fib_gen(n):
    '''
    A generator yielding the first n fibonacci numbers
    '''
    for i in range(n):
        yield fibonacci(i)


if __name__ == "__main__":
    for n in fib_gen(20):
        print(n)    
