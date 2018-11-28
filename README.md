# 02 - Modules and Testing

The Fibonacci Series is a numeric series starting with the integers 0 and 1. In this series, the next integer is determined by summing the previous two. This gives us:

0, 1, 1, 2, 3, 5, 8, 13, ...
The Lucas Numbers are a related series of integers that start with the values 2 and 1 rather than 0 and 1. The resulting series looks like this:

2, 1, 3, 4, 7, 11, 18, 29, ...

# Feature Tasks

Create a function called fibonacci. The function should have one parameter n. The function should return the nth value in the fibonacci series. You may implement the function using recursion or iteration. If you are feeling particularly frisky, do both as separate functions.

Calling this function with no optional parameters will produce numbers from the fibonacci series. Calling it with the optional arguments 2 and 1 will produce values from the lucas numbers. Other values for the optional parameters will produce other series. Again, you may use recursion or iteration, or both. Again, ensure that your function has a well-formed docstring.

# Testing

All tests are written in PyTest - To run the tests make sure that pipenv is running ("pipenv shell"), and then install pytest ("pipenv install pytest"). Once that is finished, you may run the tests by simply typing "pytest" in the terminal.

# Credits

Sources used include:
- WikiPedia for the fibonacci sequence
- http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibtable.html for the numbers used in testing,
- and last but not least, https://www.sanfoundry.com/python-program-find-fibonacci-series-recursion/ for the right direction in recursion.


***Author: [Daniel Frey](https://github.com/fncreative)

