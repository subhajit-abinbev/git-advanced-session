"""
Test suite for calculator module - WITH BOTH PASSING AND FAILING TESTS

This test file demonstrates various pytest concepts:
- Basic test functions (PASS and FAIL scenarios)
- Test fixtures
- Parametrized tests
- Exception testing
- Test organization with classes
- Different types of test failures for learning

IMPORTANT: This file contains INTENTIONAL FAILURES for demonstration purposes!
To run only passing tests: pytest -k "PASS"
To run only failing tests: pytest -k "FAIL"
"""

import pytest
import math
from src.calculator import (
    add, subtract, multiply, divide, power, 
    square_root, factorial, percentage
)


class TestBasicArithmetic:
    """Test class demonstrating basic arithmetic operations - PASSING TESTS."""
    
    def test_add_positive_numbers_PASS(self):
        """✅ PASSING: Test adding positive numbers."""
        assert add(2, 3) == 5
        assert add(10, 15) == 25
        assert add(0, 5) == 5
    
    def test_add_negative_numbers_PASS(self):
        """✅ PASSING: Test adding negative numbers."""
        assert add(-2, -3) == -5
        assert add(-10, 5) == -5
        assert add(10, -5) == 5
    
    def test_add_floats_PASS(self):
        """✅ PASSING: Test adding floating point numbers."""
        result = add(2.5, 3.7)
        assert abs(result - 6.2) < 0.0001  # Handle floating point precision
        assert add(0.1, 0.2) == pytest.approx(0.3)  # pytest.approx for floats
    
    def test_subtract_basic_PASS(self):
        """✅ PASSING: Test basic subtraction."""
        assert subtract(10, 3) == 7
        assert subtract(5, 5) == 0
        assert subtract(0, 5) == -5
    
    def test_multiply_basic_PASS(self):
        """✅ PASSING: Test basic multiplication."""
        assert multiply(3, 4) == 12
        assert multiply(-2, 5) == -10
        assert multiply(0, 100) == 0
    
    def test_multiply_by_zero_PASS(self):
        """✅ PASSING: Test multiplication by zero."""
        assert multiply(100, 0) == 0
        assert multiply(0, 0) == 0


class TestBasicArithmeticFailing:
    """Test class with FAILING tests - these demonstrate different failure types."""
    
    def test_add_wrong_expectation_FAIL(self):
        """❌ FAILING: Wrong expected result - Assertion Error."""
        # This will fail because 2 + 3 = 5, not 6
        assert add(2, 3) == 6  # INTENTIONAL FAILURE: Wrong expectation
    
    def test_subtract_wrong_math_FAIL(self):
        """❌ FAILING: Wrong math expectation - Assertion Error."""
        # This will fail because 10 - 3 = 7, not 8
        assert subtract(10, 3) == 8  # INTENTIONAL FAILURE: Wrong math
    
    def test_multiply_float_precision_FAIL(self):
        """❌ FAILING: Float precision issue - Assertion Error."""
        # This might fail due to floating point precision
        result = multiply(0.1, 0.2)
        assert result == 0.02  # INTENTIONAL FAILURE: Should use pytest.approx


class TestDivision:
    """Test class for division operations and error handling - PASSING TESTS."""
    
    def test_divide_basic_PASS(self):
        """✅ PASSING: Test basic division."""
        assert divide(10, 2) == 5.0
        assert divide(15, 3) == 5.0
        assert divide(7, 2) == 3.5
    
    def test_divide_by_zero_raises_exception_PASS(self):
        """✅ PASSING: Test that division by zero raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError):
            divide(10, 0)
        
        # Alternative syntax with message checking
        with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
            divide(5, 0)
    
    def test_divide_negative_numbers_PASS(self):
        """✅ PASSING: Test division with negative numbers."""
        assert divide(-10, 2) == -5.0
        assert divide(10, -2) == -5.0
        assert divide(-10, -2) == 5.0


class TestDivisionFailing:
    """Test class for division - FAILING TESTS to demonstrate error scenarios."""
    
    def test_divide_by_zero_wrong_exception_FAIL(self):
        """❌ FAILING: Expecting wrong exception type."""
        # This will fail because divide by zero raises ZeroDivisionError, not ValueError
        with pytest.raises(ValueError):  # INTENTIONAL FAILURE: Wrong exception type
            divide(10, 0)
    
    def test_divide_wrong_result_FAIL(self):
        """❌ FAILING: Wrong expected result."""
        # This will fail because 10 / 2 = 5.0, not 4.0
        assert divide(10, 2) == 4.0  # INTENTIONAL FAILURE: Wrong expectation
    
    def test_divide_missing_exception_handling_FAIL(self):
        """❌ FAILING: Not handling expected exception."""
        # This will fail because we expect an exception but don't handle it
        result = divide(10, 0)  # INTENTIONAL FAILURE: This will raise ZeroDivisionError
        assert result == 0  # This line won't be reached


@pytest.mark.parametrize("base,exponent,expected", [
    (2, 3, 8),      # ✅ PASSING
    (5, 0, 1),      # ✅ PASSING  
    (4, 0.5, 2.0),  # ✅ PASSING
    (10, 2, 100),   # ✅ PASSING
    (-2, 3, -8),    # ✅ PASSING
    (0, 5, 0),      # ✅ PASSING
])
def test_power_parametrized_PASS(base, exponent, expected):
    """✅ PASSING: Parametrized test for power function."""
    result = power(base, exponent)
    assert result == pytest.approx(expected)


@pytest.mark.parametrize("base,exponent,expected", [
    (2, 3, 9),      # ❌ FAILING: 2^3 = 8, not 9
    (5, 0, 0),      # ❌ FAILING: 5^0 = 1, not 0
    (4, 0.5, 3.0),  # ❌ FAILING: 4^0.5 = 2.0, not 3.0
])
def test_power_parametrized_FAIL(base, exponent, expected):
    """❌ FAILING: Parametrized test with wrong expectations."""
    result = power(base, exponent)
    assert result == pytest.approx(expected)  # INTENTIONAL FAILURES


class TestSquareRoot:
    """Test class for square root function - PASSING TESTS."""
    
    def test_square_root_perfect_squares_PASS(self):
        """✅ PASSING: Test square root of perfect squares."""
        assert square_root(9) == 3.0
        assert square_root(16) == 4.0
        assert square_root(25) == 5.0
        assert square_root(0) == 0.0
    
    def test_square_root_non_perfect_squares_PASS(self):
        """✅ PASSING: Test square root of non-perfect squares."""
        assert square_root(2) == pytest.approx(1.4142135623730951)
        assert square_root(10) == pytest.approx(3.1622776601683795)
    
    def test_square_root_negative_raises_error_PASS(self):
        """✅ PASSING: Test that square root of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
            square_root(-1)
        
        with pytest.raises(ValueError):
            square_root(-10)


class TestSquareRootFailing:
    """Test class for square root function - FAILING TESTS."""
    
    def test_square_root_wrong_result_FAIL(self):
        """❌ FAILING: Wrong expected result."""
        # This will fail because sqrt(9) = 3.0, not 4.0
        assert square_root(9) == 4.0  # INTENTIONAL FAILURE
    
    def test_square_root_negative_wrong_exception_FAIL(self):
        """❌ FAILING: Wrong exception message."""
        # This will fail because the error message doesn't match
        with pytest.raises(ValueError, match="Invalid input"):  # INTENTIONAL FAILURE
            square_root(-1)


class TestFactorial:
    """Test class for factorial function - PASSING TESTS."""
    
    @pytest.mark.parametrize("n,expected", [
        (0, 1),
        (1, 1),
        (5, 120),
        (10, 3628800),
    ])
    def test_factorial_valid_inputs_PASS(self, n, expected):
        """✅ PASSING: Test factorial with valid inputs."""
        assert factorial(n) == expected
    
    def test_factorial_negative_raises_error_PASS(self):
        """✅ PASSING: Test that factorial of negative number raises ValueError."""
        with pytest.raises(ValueError, match="Factorial is not defined for negative numbers"):
            factorial(-1)
    
    def test_factorial_non_integer_raises_error_PASS(self):
        """✅ PASSING: Test that factorial of non-integer raises TypeError."""
        with pytest.raises(TypeError, match="Factorial is only defined for integers"):
            factorial(5.5)
        
        with pytest.raises(TypeError):
            factorial("5")


class TestFactorialFailing:
    """Test class for factorial function - FAILING TESTS."""
    
    @pytest.mark.parametrize("n,expected", [
        (5, 100),      # ❌ FAILING: 5! = 120, not 100
        (3, 5),        # ❌ FAILING: 3! = 6, not 5
        (4, 25),       # ❌ FAILING: 4! = 24, not 25
    ])
    def test_factorial_wrong_expectations_FAIL(self, n, expected):
        """❌ FAILING: Test factorial with wrong expected values."""
        assert factorial(n) == expected  # INTENTIONAL FAILURES
    
    def test_factorial_negative_wrong_exception_FAIL(self):
        """❌ FAILING: Expecting wrong exception type."""
        # This will fail because factorial(-1) raises ValueError, not TypeError
        with pytest.raises(TypeError):  # INTENTIONAL FAILURE: Wrong exception type
            factorial(-1)


class TestPercentage:
    """Test class for percentage calculation - PASSING TESTS."""
    
    def test_percentage_basic_PASS(self):
        """✅ PASSING: Test basic percentage calculations."""
        assert percentage(25, 100) == 25.0
        assert percentage(1, 4) == 25.0
        assert percentage(3, 4) == 75.0
        assert percentage(100, 100) == 100.0
    
    def test_percentage_with_floats_PASS(self):
        """✅ PASSING: Test percentage with floating point numbers."""
        assert percentage(2.5, 10) == 25.0
        assert percentage(7.5, 15) == 50.0
    
    def test_percentage_zero_whole_raises_error_PASS(self):
        """✅ PASSING: Test that percentage with zero whole raises ZeroDivisionError."""
        with pytest.raises(ZeroDivisionError, match="Cannot calculate percentage with zero as whole"):
            percentage(50, 0)


class TestPercentageFailing:
    """Test class for percentage calculation - FAILING TESTS."""
    
    def test_percentage_wrong_calculation_FAIL(self):
        """❌ FAILING: Wrong percentage calculation."""
        # This will fail because 25/100 = 25%, not 30%
        assert percentage(25, 100) == 30.0  # INTENTIONAL FAILURE
    
    def test_percentage_zero_whole_wrong_exception_FAIL(self):
        """❌ FAILING: Expecting wrong exception type."""
        # This will fail because percentage with zero raises ZeroDivisionError, not ValueError
        with pytest.raises(ValueError):  # INTENTIONAL FAILURE: Wrong exception type
            percentage(50, 0)


# Fixtures for more complex testing scenarios
@pytest.fixture
def calculator_test_data_PASS():
    """✅ PASSING: Fixture providing correct test data."""
    return {
        'positive_numbers': [1, 2, 3, 5, 10],
        'negative_numbers': [-1, -2, -5, -10],
        'zero': 0,
        'floats': [1.5, 2.7, 3.14, 100.001],
        'large_numbers': [1000, 10000, 100000]
    }


@pytest.fixture
def calculator_test_data_FAIL():
    """❌ FAILING: Fixture with incorrect test data for demonstration."""
    return {
        'positive_numbers': [1, 2, 3, 5, 10],
        'wrong_calculations': [(2, 3, 6), (5, 5, 11), (1, 1, 3)]  # INTENTIONAL FAILURES
    }


@pytest.fixture
def sample_calculations():
    """Fixture providing sample calculation results."""
    return {
        'additions': [(1, 2, 3), (5, 10, 15), (-5, 5, 0)],
        'multiplications': [(2, 3, 6), (0, 100, 0), (-2, 4, -8)]
    }


def test_calculator_with_fixture_data_PASS(calculator_test_data_PASS):
    """✅ PASSING: Test using correct fixture data."""
    # Test that adding zero doesn't change values
    for num in calculator_test_data_PASS['positive_numbers']:
        assert add(num, 0) == num
        assert multiply(num, 1) == num


def test_calculator_with_fixture_data_FAIL(calculator_test_data_FAIL):
    """❌ FAILING: Test using fixture with wrong data."""
    for a, b, expected in calculator_test_data_FAIL['wrong_calculations']:
        assert add(a, b) == expected  # INTENTIONAL FAILURES


def test_multiple_operations_chain_PASS():
    """✅ PASSING: Test chaining multiple operations."""
    # Test: (2 + 3) * 4 - 1 = 19
    result = subtract(multiply(add(2, 3), 4), 1)
    assert result == 19
    
    # Test: 10 / 2 + 3 * 2 = 11
    result = add(divide(10, 2), multiply(3, 2))
    assert result == 11.0


def test_multiple_operations_chain_FAIL():
    """❌ FAILING: Test chaining with wrong expectation."""
    # Test: (2 + 3) * 4 - 1 = 19, but we expect 20
    result = subtract(multiply(add(2, 3), 4), 1)
    assert result == 20  # INTENTIONAL FAILURE: Should be 19


@pytest.mark.slow
def test_large_factorial_PASS():
    """✅ PASSING: Test factorial with larger numbers (marked as slow)."""
    # This test is marked as 'slow' - can be skipped with: pytest -m "not slow"
    result = factorial(15)
    assert result == 1307674368000


@pytest.mark.slow
def test_large_factorial_FAIL():
    """❌ FAILING: Test factorial with wrong expectation (marked as slow)."""
    result = factorial(10)
    assert result == 3000000  # INTENTIONAL FAILURE: 10! = 3628800, not 3000000


# Test for edge cases and boundary conditions
class TestEdgeCases:
    """Test edge cases and boundary conditions - PASSING TESTS."""
    
    def test_very_small_numbers_PASS(self):
        """✅ PASSING: Test operations with very small numbers."""
        small = 1e-10
        assert add(small, small) == 2e-10
        assert multiply(small, 2) == 2e-10
    
    def test_very_large_numbers_PASS(self):
        """✅ PASSING: Test operations with very large numbers."""
        large = 1e10
        assert add(large, large) == 2e10
        assert multiply(large, 2) == 2e10
    
    def test_zero_operations_PASS(self):
        """✅ PASSING: Test various operations with zero."""
        assert add(0, 0) == 0
        assert subtract(0, 0) == 0
        assert multiply(0, 1000) == 0
        assert power(0, 5) == 0


class TestEdgeCasesFailing:
    """Test edge cases - FAILING TESTS."""
    
    def test_zero_operations_wrong_expectation_FAIL(self):
        """❌ FAILING: Test zero operations with wrong expectations."""
        assert add(0, 0) == 1  # INTENTIONAL FAILURE: 0 + 0 = 0, not 1
        assert multiply(0, 1000) == 1000  # INTENTIONAL FAILURE: 0 * 1000 = 0, not 1000


# Demonstration of pytest markers
@pytest.mark.integration
def test_calculator_integration_PASS():
    """✅ PASSING: Integration test combining multiple calculator functions."""
    # Calculate: sqrt(16) + 2^3 - 10/2 + 3! = 4 + 8 - 5 + 6 = 13
    result = add(
        add(square_root(16), power(2, 3)),
        add(-divide(10, 2), factorial(3))
    )
    assert result == 13.0


@pytest.mark.integration
def test_calculator_integration_FAIL():
    """❌ FAILING: Integration test with wrong expectation."""
    # Calculate: sqrt(16) + 2^3 - 10/2 + 3! = 4 + 8 - 5 + 6 = 13, but we expect 15
    result = add(
        add(square_root(16), power(2, 3)),
        add(-divide(10, 2), factorial(3))
    )
    assert result == 15.0  # INTENTIONAL FAILURE: Should be 13.0


# Skip test example
@pytest.mark.skip(reason="Example of skipped test")
def test_not_implemented_feature():
    """This test is skipped - useful for features not yet implemented."""
    pass


# Conditional skip
@pytest.mark.skipif(not hasattr(math, 'isclose'), reason="math.isclose not available")
def test_with_math_isclose_PASS():
    """✅ PASSING: Test that uses math.isclose if available."""
    result = divide(1, 3)
    expected = 1/3
    assert math.isclose(result, expected)


# Additional failing test scenarios
class TestCommonMistakes:
    """Common testing mistakes that lead to failures."""
    
    def test_floating_point_precision_FAIL(self):
        """❌ FAILING: Direct floating point comparison without tolerance."""
        result = divide(1, 3)
        expected = 0.3333333333333333
        assert result == expected  # INTENTIONAL FAILURE: Floating point precision issue
    
    def test_wrong_function_call_FAIL(self):
        """❌ FAILING: Calling function with wrong parameters."""
        # This will fail because we're calling add with 3 parameters instead of 2
        try:
            result = add(1, 2, 3)  # INTENTIONAL FAILURE: Too many arguments
            assert result == 6
        except TypeError:
            # If we catch the TypeError, the test should fail because our logic is wrong
            assert False, "Function call failed due to wrong number of arguments"
    
    def test_assertion_without_function_call_FAIL(self):
        """❌ FAILING: Hardcoded assertion that doesn't test the function."""
        # This test doesn't actually test our function
        x = 5
        y = 3
        expected = 8
        actual = 9  # Hardcoded wrong value instead of calling add(x, y)
        assert actual == expected  # INTENTIONAL FAILURE: 9 != 8


if __name__ == "__main__":
    # Examples of how to run specific test groups:
    
    # Run only passing tests
    print("To run only PASSING tests: pytest -k 'PASS' -v")
    
    # Run only failing tests  
    print("To run only FAILING tests: pytest -k 'FAIL' -v")
    
    # Run all tests
    print("To run ALL tests: pytest tests/test_calculator.py -v")
    
    # Run by test class
    print("To run specific class: pytest tests/test_calculator.py::TestBasicArithmetic -v")
    
    # Default: run passing tests only for demo
    pytest.main([__file__, "-k", "PASS", "-v"])
