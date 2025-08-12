"""
Test suite for calculator module - Simple passing tests only
"""

import pytest
from src.calculator import add, subtract, multiply, divide, square_root, factorial


def test_add():
    """Test basic addition."""
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0.1, 0.2) == pytest.approx(0.3)


def test_subtract():
    """Test basic subtraction."""
    assert subtract(10, 3) == 7
    assert subtract(5, 5) == 0
    assert subtract(-2, -3) == 1


def test_multiply():
    """Test basic multiplication."""
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 100) == 0


def test_divide():
    """Test basic division and error handling."""
    assert divide(10, 2) == 5.0
    assert divide(7, 2) == 3.5
    
    # Test division by zero raises exception
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)


def test_square_root():
    """Test square root calculation and error handling."""
    assert square_root(9) == 3.0
    assert square_root(16) == 4.0
    assert square_root(2) == pytest.approx(1.4142135623730951)
    
    # Test negative number raises exception
    with pytest.raises(ValueError):
        square_root(-1)


def test_factorial():
    """Test factorial calculation and error handling."""
    assert factorial(0) == 1
    assert factorial(5) == 120
    assert factorial(1) == 1
    
    # Test negative number raises exception
    with pytest.raises(ValueError):
        factorial(-1)
