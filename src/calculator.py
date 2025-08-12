"""
Simple Calculator Module

A basic calculator with arithmetic operations for demonstration purposes.
This module is used in the Git Advanced Session to demonstrate:
- Basic Python code structure
- Testing with pytest
- Pre-commit hooks
- Merge conflicts and rebasing scenarios
"""

import math
from typing import Union
import logging
Number = Union[int, float]


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def add(a: Number, b: Number) -> Number:
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
        
    Examples:
        >>> add(2, 3)
        5
        >>> add(2.5, 1.5)
        4.0
    """
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Both arguments must be numbers (int or float)")
        
        logger.info(f"Adding {a} and {b}")
        return a + b
    except Exception as e:
        logger.error(f"Error in add function: {e}")
        raise


def subtract(a: Number, b: Number) -> Number:
    """
    Subtract second number from first number.
    
    Args:
        a: First number (minuend)
        b: Second number (subtrahend)
        
    Returns:
        Difference of a and b
        
    Examples:
        >>> subtract(5, 3)
        2
        >>> subtract(10.5, 2.5)
        8.0
    """
    return a - b


def multiply(a: Number, b: Number) -> Number:
    """
    Multiply two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Product of a and b
        
    Examples:
        >>> multiply(4, 5)
        20
        >>> multiply(2.5, 4)
        10.0
    """
    return a * b


def divide(a: Number, b: Number) -> Number:
    """
    Divide first number by second number.
    
    Args:
        a: Dividend
        b: Divisor
        
    Returns:
        Quotient of a and b
        
    Raises:
        ZeroDivisionError: When attempting to divide by zero
        
    Examples:
        >>> divide(10, 2)
        5.0
        >>> divide(7, 2)
        3.5
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


def power(base: Number, exponent: Number) -> Number:
    """
    Raise base to the power of exponent.
    
    Args:
        base: The base number
        exponent: The exponent
        
    Returns:
        base raised to the power of exponent
        
    Examples:
        >>> power(2, 3)
        8
        >>> power(4, 0.5)
        2.0
    """
    return base ** exponent


def square_root(number: Number) -> float:
    """
    Calculate the square root of a number.
    
    Args:
        number: The number to find square root of
        
    Returns:
        Square root of the number
        
    Raises:
        ValueError: When number is negative
        
    Examples:
        >>> square_root(9)
        3.0
        >>> square_root(2)
        1.4142135623730951
    """
    if number < 0:
        raise ValueError("Cannot calculate square root of negative number")
    return math.sqrt(number)


def factorial(n: int) -> int:
    """
    Calculate the factorial of a non-negative integer.
    
    Args:
        n: Non-negative integer
        
    Returns:
        Factorial of n
        
    Raises:
        ValueError: When n is negative
        TypeError: When n is not an integer
        
    Examples:
        >>> factorial(5)
        120
        >>> factorial(0)
        1
    """
    if not isinstance(n, int):
        raise TypeError("Factorial is only defined for integers")
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def percentage(part: Number, whole: Number) -> float:
    """
    Calculate what percentage 'part' is of 'whole'.
    
    Args:
        part: The part value
        whole: The whole value
        
    Returns:
        Percentage as a float
        
    Raises:
        ZeroDivisionError: When whole is zero
        
    Examples:
        >>> percentage(25, 100)
        25.0
        >>> percentage(3, 4)
        75.0
    """
    if whole == 0:
        raise ZeroDivisionError("Cannot calculate percentage with zero as whole")
    return (part / whole) * 100
