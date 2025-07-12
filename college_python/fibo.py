def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=' ')
        a, b = b, a + b

n = int(input("Enter the number of Fibonacci terms: "))
fibonacci(n)


def is_perfect_square(x):
    s = int(x**0.5)
    return s * s == x

def is_fibonacci(n):
    # A number is Fibonacci if and only if
    # 5*n^2 + 4 OR 5*n^2 - 4 is a perfect square
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

num = int(input("Enter a number: "))

if is_fibonacci(num):
    print("Yes, it's a Fibonacci number!")
else:
    print("Nope, not a Fibonacci number.")


'''
Positional Arguments – Values are passed based on their position in the function call.
→ def func(a, b): ... → func(10, 20)

Keyword Arguments – Values are passed using parameter names explicitly.
→ func(a=10, b=20)

Default Arguments – If no value is passed, default values are used.
→ def func(a=5): ... → func() uses 5

Variable-length Arguments (*args) – Accepts multiple positional arguments as a tuple.
→ def func(*args): ...

Variable-length Keyword Arguments (**kwargs) – Accepts multiple keyword arguments as a dictionary.
→ def func(**kwargs): ...

Positional-only Arguments (/) – Arguments before / must be passed by position (Python 3.8+).
→ def func(a, b, /, c): ...

Keyword-only Arguments (*) – Arguments after * must be passed as keyword arguments.
→ def func(*, a, b): ...

Unpacking Arguments (*, **) – Expands a list or dict into function arguments.
→ func(*[1, 2]) or func(**{'a': 1, 'b': 2})
'''