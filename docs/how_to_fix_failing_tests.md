# 🔧 How to Fix the Failing Tests - Complete Guide

## Overview
This guide explains how to fix each type of failing test in `test_calculator.py`. The file contains both **PASSING** and **FAILING** tests for demonstration purposes.

---

## 🎯 How to Run Different Test Categories

### Run Only Passing Tests
```bash
pytest tests/test_calculator.py -k "PASS" -v
```

### Run Only Failing Tests  
```bash
pytest tests/test_calculator.py -k "FAIL" -v
```

### Run All Tests (see both pass and fail)
```bash
pytest tests/test_calculator.py -v
```

---

## 🚨 Types of Failures and How to Fix Them

### 1. **Assertion Errors - Wrong Expected Values**

#### ❌ **Failing Test:**
```python
def test_add_wrong_expectation_FAIL(self):
    assert add(2, 3) == 6  # WRONG: 2+3=5, not 6
```

#### ✅ **How to Fix:**
```python
def test_add_correct_expectation_FIXED(self):
    assert add(2, 3) == 5  # CORRECT: 2+3=5
```

**Key Learning:** Always verify your expected results manually or with a calculator.

---

### 2. **Exception Type Errors**

#### ❌ **Failing Test:**
```python
def test_divide_by_zero_wrong_exception_FAIL(self):
    with pytest.raises(ValueError):  # WRONG exception type
        divide(10, 0)
```

#### ✅ **How to Fix:**
```python
def test_divide_by_zero_correct_exception_FIXED(self):
    with pytest.raises(ZeroDivisionError):  # CORRECT exception type
        divide(10, 0)
```

**Key Learning:** Check what exception your function actually raises by reading the code or running it manually.

---

### 3. **Floating Point Precision Issues**

#### ❌ **Failing Test:**
```python
def test_multiply_float_precision_FAIL(self):
    result = multiply(0.1, 0.2)
    assert result == 0.02  # FAILS due to floating point precision
```

#### ✅ **How to Fix:**
```python
def test_multiply_float_precision_FIXED(self):
    result = multiply(0.1, 0.2)
    assert result == pytest.approx(0.02)  # Use pytest.approx for floats
```

**Key Learning:** Never use `==` for floating point comparisons. Use `pytest.approx()` or check absolute difference.

---

### 4. **Parametrized Test Failures**

#### ❌ **Failing Test:**
```python
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),      # ✅ Correct
    (10, 15, 26),   # ❌ WRONG: 10+15=25, not 26
    (0, 5, 6),      # ❌ WRONG: 0+5=5, not 6
])
def test_add_parametrized_FAIL(self, a, b, expected):
    assert add(a, b) == expected
```

#### ✅ **How to Fix:**
```python
@pytest.mark.parametrize("a,b,expected", [
    (2, 3, 5),      # ✅ Correct
    (10, 15, 25),   # ✅ FIXED: 10+15=25
    (0, 5, 5),      # ✅ FIXED: 0+5=5
])
def test_add_parametrized_FIXED(self, a, b, expected):
    assert add(a, b) == expected
```

**Key Learning:** Check each parameter set individually. One wrong value fails the entire parametrized test.

---

### 5. **Exception Message Matching Errors**

#### ❌ **Failing Test:**
```python
def test_square_root_negative_wrong_message_FAIL(self):
    with pytest.raises(ValueError, match="Invalid input"):  # WRONG message
        square_root(-1)
```

#### ✅ **How to Fix:**
```python
def test_square_root_negative_correct_message_FIXED(self):
    with pytest.raises(ValueError, match="Cannot calculate square root of negative number"):
        square_root(-1)
```

**Key Learning:** Check the actual error message in your source code. The `match` parameter must match the actual message.

---

### 6. **Missing Exception Handling**

#### ❌ **Failing Test:**
```python
def test_divide_missing_exception_handling_FAIL(self):
    result = divide(10, 0)  # This raises ZeroDivisionError!
    assert result == 0      # This line never executes
```

#### ✅ **How to Fix:**
```python
def test_divide_with_proper_exception_handling_FIXED(self):
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)  # Properly expect the exception
```

**Key Learning:** If your function raises an exception, you must handle it with `pytest.raises()`.

---

### 7. **Fixture Data Errors**

#### ❌ **Failing Test:**
```python
@pytest.fixture
def calculator_test_data_FAIL():
    return {
        'wrong_calculations': [(2, 3, 6), (5, 5, 11)]  # Wrong expected values
    }

def test_with_incorrect_fixture_FAIL(self, calculator_test_data_FAIL):
    for a, b, expected in calculator_test_data_FAIL['wrong_calculations']:
        assert add(a, b) == expected  # FAILS because fixture has wrong data
```

#### ✅ **How to Fix:**
```python
@pytest.fixture
def calculator_test_data_FIXED():
    return {
        'correct_calculations': [(2, 3, 5), (5, 5, 10)]  # Correct expected values
    }

def test_with_correct_fixture_FIXED(self, calculator_test_data_FIXED):
    for a, b, expected in calculator_test_data_FIXED['correct_calculations']:
        assert add(a, b) == expected  # PASSES with correct data
```

**Key Learning:** Verify the data in your fixtures is correct. Bad fixture data causes multiple test failures.

---

### 8. **Type Errors**

#### ❌ **Failing Test:**
```python
def test_type_error_FAIL(self):
    result = factorial("5")  # WRONG: passing string instead of int
    assert result == 120
```

#### ✅ **How to Fix:**
```python
def test_type_correct_FIXED(self):
    result = factorial(5)  # CORRECT: passing int
    assert result == 120
```

**Key Learning:** Check function signatures and ensure you pass the correct data types.

---

### 9. **Import Errors**

#### ❌ **Failing Test:**
```python
def test_import_error_FAIL(self):
    from src.non_existent_module import some_function  # Module doesn't exist
    result = some_function(5)
    assert result == 5
```

#### ✅ **How to Fix:**
```python
def test_import_correct_FIXED(self):
    from src.calculator import add  # Import existing function
    result = add(2, 3)
    assert result == 5
```

**Key Learning:** Verify that modules and functions exist before importing them.

---

### 10. **Logic Errors in Tests**

#### ❌ **Failing Test:**
```python
def test_wrong_test_logic_FAIL(self):
    x = 5
    y = 3
    expected = 8  # Hardcoded value
    actual = add(x, y)  # This returns 8
    assert actual == 9  # WRONG: comparing with wrong value
```

#### ✅ **How to Fix:**
```python
def test_correct_test_logic_FIXED(self):
    x = 5
    y = 3
    expected = 8  # Correct expected value
    actual = add(x, y)  # This returns 8
    assert actual == expected  # CORRECT: comparing with right value
```

**Key Learning:** Ensure your test logic is sound. Don't hardcode wrong values.

---

## 🛠️ Debugging Strategies

### 1. **Read the Error Message Carefully**
```
FAILED test_calculator.py::test_add_wrong_expectation_FAIL 
AssertionError: assert 5 == 6
```
This tells you: expected 6, got 5.

### 2. **Run Individual Tests**
```bash
pytest tests/test_calculator.py::test_add_wrong_expectation_FAIL -v
```

### 3. **Use Print Debugging (temporarily)**
```python
def test_debug_FAIL(self):
    result = add(2, 3)
    print(f"Result: {result}")  # Add this to see actual value
    assert result == 6  # Wrong expectation
```

### 4. **Check Function Implementation**
Look at the source code to understand what the function actually returns.

### 5. **Test Functions Manually**
```python
# In Python REPL or Jupyter notebook
from src.calculator import add
result = add(2, 3)
print(result)  # See what it actually returns
```

---

## 📊 Summary of Common Fixes

| Error Type | Fix Strategy |
|------------|-------------|
| **Wrong Expected Value** | Calculate the correct expected result |
| **Wrong Exception Type** | Check what exception the function actually raises |
| **Float Precision** | Use `pytest.approx()` for floating point comparisons |
| **Wrong Exception Message** | Check the actual error message in source code |
| **Missing Exception Handling** | Use `pytest.raises()` when function raises exceptions |
| **Bad Fixture Data** | Verify and correct the data in fixtures |
| **Type Errors** | Pass the correct data types to functions |
| **Import Errors** | Import existing modules and functions |
| **Logic Errors** | Review test logic and ensure it makes sense |

---

## 🎯 Best Practices to Avoid Failures

1. **Calculate Expected Results Manually** - Don't guess
2. **Read Function Documentation** - Understand what it returns
3. **Test Functions Interactively First** - Before writing tests
4. **Use Descriptive Test Names** - Makes debugging easier
5. **Write One Assertion Per Test** - Easier to identify failures
6. **Use `pytest.approx()` for Floats** - Always
7. **Check Exception Types and Messages** - Be precise
8. **Validate Fixture Data** - Ensure it's correct
9. **Run Tests Frequently** - Catch errors early
10. **Read Error Messages Carefully** - They tell you exactly what's wrong

---

## 🚀 Quick Demo Commands

```bash
# See all failures at once
pytest tests/test_calculator.py -k "FAIL" -v

# See specific failure type
pytest tests/test_calculator.py::TestBasicArithmeticFailing::test_add_wrong_expectation_FAIL -v

# Compare with passing version
pytest tests/test_calculator.py::TestBasicArithmetic::test_add_positive_numbers_PASS -v

# Run and show detailed output
pytest tests/test_calculator.py -k "FAIL" -v -s
```

This comprehensive guide covers all the failure scenarios in your test file and exactly how to fix each one!
