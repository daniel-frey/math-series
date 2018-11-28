from pytest import raises
from series import fibonacci
from series import fibonacci_recursion
from series import lucas
from series import lucas_recursion
from series import sum_series
from series import sum_series_recursion
import series

def test_fib_n():
    """ this will test fibonacci (n)
    """
    actual = 6
    expected = 8
    assert series.fibonacci(actual) == expected
    assert series.fibonacci_recursion(actual) == expected

def test_fib_at_zero():
    """ this will test fibonacci at 0
    """
    actual = 0
    expected = 0
    assert series.fibonacci(actual) == expected
    assert series.fibonacci_recursion(actual) == expected

def test_fib_at_one():
    """ this will test fibonacci at 1
    """
    actual = 1
    expected = 1
    assert series.fibonacci(actual) == expected
    assert series.fibonacci_recursion(actual) == expected

def test_fib_large_number():
    """ this will test a larger fibonacci number
    """
    actual = 24
    expected = 46368
    assert series.fibonacci(actual) == expected
    assert series.fibonacci_recursion(actual) == expected

def test_fib_invalid_input():
    """ this will test for the incorrect input
    """
    actual = {}

    with raises(TypeError):
        series.fibonacci(actual)
        series.fibonacci_recursion(actual)

    actual = -12

    with raises(TypeError):
        series.fibonacci(actual)
        series.fibonacci_recursion(actual)

def test_lucas_at_n():
    """ test for lucas number at sequence number n
    """
    actual = 6
    expected = 18
    assert series.lucas(actual) == expected
    assert series.lucas_recursion(actual) == expected

def test_lucas_zero():
    """ test for lucas number at sequence number 0
    """
    actual = 0
    expected = 2
    assert series.lucas(actual) == expected
    assert series.lucas_recursion(actual) == expected

def test_lucas_invalid_input():
    """ test for invalid type and invalid input (negative int)
    """
    actual = []

    with raises(TypeError):
        series.fibonacci(actual)
        series.fibonacci_recursion(actual)

    actual = -12

    with raises(TypeError):
        series.fibonacci(actual)
        series.fibonacci_recursion(actual)

def test_lucas_large_number():
    """ test for lucas number at a large sequence number
    """
    actual = 20
    expected = 15127
    assert series.lucas(actual) == expected
    assert series.lucas_recursion(actual) == expected

def test_sum_series_at_n():
    """ test for fibonacci or lucas sequence number at n.
    """
    actual = 6
    expected_fib = 8
    expected_lucas = 18
    assert series.sum_series(actual) == expected_fib
    assert series.sum_series(actual, 2, 1) == expected_lucas
    assert series.sum_series_recursion(actual) == expected_fib
    assert series.sum_series_recursion(actual, 2, 1) == expected_lucas

def test_sum_series_zero():
    """ test for fibonacci or lucas sequence number at 0.
    """
    actual = 0
    expected_fib = 0
    expected_lucas = 2
    assert series.sum_series(actual) == expected_fib
    assert series.sum_series_recursion(actual) == expected_fib
    assert series.sum_series(actual, 2, 1) == expected_lucas
    assert series.sum_series_recursion(actual, 2, 1) == expected_lucas

def test_sum_series_large_number():
    """ test for lucas or fibo at a large number
    """
    actual = 24
    expected_fib = 46368
    expected_lucas = 103682
    assert series.sum_series(actual) == expected_fib
    assert series.sum_series_recursion(actual) == expected_fib
    assert series.sum_series(actual, 2, 1) == expected_lucas
    assert series.sum_series_recursion(actual, 2, 1) == expected_lucas

def test_sum_series_incorrect_input():
    """ test sum series function for invalid type and invalid input
    """
    actual = []

    with raises(TypeError):
        series.sum_series(actual)
        series.sum_series_recursion(actual)
        series.sum_series(actual, 2, 1)
        series.sum_series_recursion(actual, 2, 1)

    actual = -12

    with raises(TypeError):
        series.sum_series(actual)
        series.sum_series_recursion(actual)
        series.sum_series(actual, 2, 1)
        series.sum_series_recursion(actual, 2, 1)
