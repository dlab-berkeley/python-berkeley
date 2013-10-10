"""Function annotations demo using MyPy (http://www.mypy-lang.org/)

This code will run under either MyPy or vanilla Python 3, but MyPy can give
a clearer error when we call the function with the wrong type of input.
"""
import typing

def fib(n: int) -> None:
    a, b = 0, 1 
    while a < n:
        print(a)
        a, b = b, a+b

fib(1000)
#fib('1000')
