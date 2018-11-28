import sys

def fibonacci(n):
    """ this will take in (n) and return that number in the fibonacci chain
    """
    prev_1 = 1
    prev_2 = 0
    fib = 1

    if type(n) is not int or n < 0:
        raise TypeError('Your input needs to be a positive number please')

    if n == 0 or n == 1:
        return n

    for idx in range(2, n + 1):
        fib = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = fib

    return fib

def fibonacci_recursion(n):
    """ this will take in (n) and return the fibonacci sequence recursively
    """

    if type(n) is not int or n < 0:
        raise TypeError('Your input needs to be a positive number please')

    if n == 1 or n == 0:
        return n

    return fibonacci_recursion(n - 2) + fibonacci_recursion(n - 1)

def lucas(n):
    """ this will use the lucas methond and return a loop using (n) as the argument
    """
    prev_1 = 1
    prev_2 = 2
    lucas = 1

    if type(n) is not int or n < 0:
        raise TypeError('Your input needs to be a positive number please')

    if n == 0:
        return 2

    if n == 1:
        return 1

    for idx in range(2, n + 1):
        lucas = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = lucas

    return lucas

def lucas_recursion(n):
    """ this will take in (n) and return the lucas sequence recursively
    """

    if type(n) is not int or n < 0:
        raise TypeError('Your input needs to be a positive number please')

    if n == 0:
        return 2

    if n == 1:
        return 1

    return lucas_recursion(n - 1) + lucas_recursion(n - 2)

def sum_series(n, prev_2=0, prev_1=1):
    """ sum_series will do either fibonacci or lucas based on the arguments
        that are provided. If you use only (n), you will get fibonacci. If you use both,
        you will get lucas. Fancy.
    """

    sum_series_number = 0

    if type(n) is not int or n < 0:
        raise TypeError('Your input needs to be a positive number please')

    if n == 0:
        return prev_2

    if n == 1:
        return prev_1

    for idx in range(2, n + 1):
        sum_series_number = prev_1 + prev_2
        prev_2 = prev_1
        prev_1 = sum_series_number

    return sum_series_number

def sum_series_recursion(n, prev_2=0, prev_1=1):
    """ sum_series_recursion will do either fibonacci or lucas recursively based on the arguments
        that are provided. If you use only (n), you will get fibonacci. If you use both,
        you will get lucas. Fancy.
    """

    if type(n) is not int or n < 0:
        raise TypeError('Your input needs to be a positive number please')

    if n == 0:
        return prev_2

    if n == 1:
        return prev_1

    return sum_series_recursion(n - 1, prev_2, prev_1) + sum_series_recursion(n - 2, prev_2, prev_1)

def main_application_start():
    print('''
    This module defines functions that implement mathematical series.

    See below for the instructions to run the application. You will choose from a few different options.
    Type "quit" to exit.

    If your data is entered incorrectly, you will receive a type error.

    fibonacci(n): this will take in (n) and return that number in the fibonacci chain.

    fibonacci_recursion(n): this will take in (n) and return the fibonacci sequence using recurion.

    lucas(n): this returns a lucas number using a loop where (n) is the number you wish to receive.

    lucas_recursion(n): returns lucas sequence number at n using recursion.

    sum_series(n[, prev_2, prev_1]): returns a number from sequence of either
        fibonacci or lucas.

        The second and third arguments are optional and are used to determine the first
        two numbers of returned sequence.

    sum_series_recursion(n[, prev_2, prev_1]): same as above. this version uses recursion
    ''')

    while True:
        user_input = input('->')

        if user_input == 'quit()':
            print('Application exiting.')
            sys.exit()

        try:
            print(eval(user_input))
        except:
            print('There is a problem with your input.')

if __name__ == "__main__":
    main_application_start()
    sys.exit()
