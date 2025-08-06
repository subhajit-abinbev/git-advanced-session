# Pytest Tutorial Guide for Git Advanced Session

## Overview
This document explains the pytest concepts demonstrated in the test files. Use this as a reference during your Git training session when explaining testing concepts.

## 🧪 Test File Structure

### `tests/test_calculator.py` - 35 test functions
Demonstrates basic pytest concepts with simple mathematical operations.

### `tests/test_data_processor.py` - 34 test functions  
Demonstrates advanced pytest concepts with pandas DataFrame operations.

---

## 📚 Pytest Concepts Demonstrated

### 1. **Basic Test Functions**
```python
def test_add_positive_numbers():
    """Test adding positive numbers."""
    assert add(2, 3) == 5
    assert add(10, 15) == 25
```
**Key Points:**
- Functions starting with `test_` are automatically discovered
- Use `assert` statements for verifications
- Descriptive function names and docstrings

### 2. **Test Classes for Organization**
```python
class TestBasicArithmetic:
    """Test class demonstrating basic arithmetic operations."""
    
    def test_add_positive_numbers(self):
        assert add(2, 3) == 5
```
**Key Points:**
- Classes starting with `Test` group related tests
- Use `self` parameter in class methods
- Helps organize tests logically

### 3. **Exception Testing**
```python
def test_divide_by_zero_raises_exception(self):
    """Test that division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)
    
    # With message checking
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero"):
        divide(5, 0)
```
**Key Points:**
- `pytest.raises()` context manager catches expected exceptions
- `match` parameter validates error messages
- Essential for testing error conditions

### 4. **Parametrized Tests**
```python
@pytest.mark.parametrize("base,exponent,expected", [
    (2, 3, 8),
    (5, 0, 1),
    (4, 0.5, 2.0),
])
def test_power_parametrized(base, exponent, expected):
    result = power(base, exponent)
    assert result == pytest.approx(expected)
```
**Key Points:**
- Run same test with different input/output combinations
- Reduces code duplication
- First parameter is argument names, second is test data tuples

### 5. **Fixtures for Test Data**
```python
@pytest.fixture
def sample_dataframe():
    """Fixture providing a sample DataFrame for testing."""
    data = {
        'name': ['Alice', 'Bob', 'Charlie'],
        'age': [25, 30, 35]
    }
    return pd.DataFrame(data)

def test_filter_data(sample_dataframe):
    """Test using fixture data."""
    result = filter_by_column(sample_dataframe, 'name', 'Alice')
    assert len(result) == 1
```
**Key Points:**
- `@pytest.fixture` decorator creates reusable test data
- Fixtures are passed as function parameters
- Setup code runs before each test, cleanup after

### 6. **Floating Point Comparisons**
```python
def test_add_floats(self):
    """Test adding floating point numbers."""
    result = add(2.5, 3.7)
    assert result == pytest.approx(6.2)  # Handles precision issues
    assert add(0.1, 0.2) == pytest.approx(0.3)
```
**Key Points:**
- `pytest.approx()` handles floating point precision issues
- Avoids common floating point comparison problems
- Default tolerance is reasonable for most cases

### 7. **Mocking External Dependencies**
```python
@patch('src.data_processor.Path.exists')
@patch('pandas.read_csv')
def test_load_csv_empty_file(self, mock_read_csv, mock_exists):
    """Test loading empty CSV file using mock."""
    mock_exists.return_value = True
    mock_read_csv.side_effect = pd.errors.EmptyDataError("No data")
    
    with pytest.raises(pd.errors.EmptyDataError):
        load_csv_data("empty_file.csv")
```
**Key Points:**
- `@patch` decorator replaces external dependencies
- `side_effect` can raise exceptions
- `return_value` sets mock return values
- Test behavior without external dependencies

### 8. **Custom Test Markers**
```python
@pytest.mark.slow
def test_large_factorial():
    """Test factorial with larger numbers (marked as slow)."""
    result = factorial(15)
    assert result == 1307674368000

@pytest.mark.integration
def test_calculator_integration():
    """Integration test combining multiple calculator functions."""
    # Complex test combining multiple functions
```
**Key Points:**
- Custom markers categorize tests
- Run with: `pytest -m "not slow"` (skip slow tests)
- Useful for separating unit/integration/slow tests

### 9. **Skip and Conditional Skip**
```python
@pytest.mark.skip(reason="Example of skipped test")
def test_not_implemented_feature():
    """This test is skipped - useful for features not yet implemented."""
    pass

@pytest.mark.skipif(not hasattr(math, 'isclose'), reason="math.isclose not available")
def test_with_math_isclose():
    """Test that uses math.isclose if available."""
    # Test only runs if condition is met
```
**Key Points:**
- `@pytest.mark.skip` always skips test
- `@pytest.mark.skipif` conditionally skips
- Useful for platform-specific or optional features

### 10. **Temporary Files and Cleanup**
```python
@pytest.fixture
def temp_csv_file():
    """Fixture creating a temporary CSV file for testing."""
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write("name,age\nAlice,25\nBob,30")
        temp_file = f.name
    
    yield temp_file  # Provide file to test
    
    # Cleanup after test
    os.unlink(temp_file)
```
**Key Points:**
- `yield` in fixtures provides setup/teardown
- Code before `yield` runs before test
- Code after `yield` runs after test (cleanup)

---

## 🏃‍♂️ Running Tests

### Basic Commands
```bash
# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_calculator.py

# Run specific test function
pytest tests/test_calculator.py::test_add_positive_numbers

# Run tests matching pattern
pytest -k "test_add"

# Run tests with specific marker
pytest -m "not slow"

# Run tests and show coverage
pytest --cov=src

# Run tests and generate HTML report
pytest --cov=src --cov-report=html
```

### Configuration (pytest.ini)
```ini
[tool:pytest]
testpaths = tests
addopts = -v --tb=short --color=yes
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
```

---

## 🎯 Teaching Points for Your Session

### 1. **Start Simple**
- Begin with basic assert statements
- Show how tests discover automatically
- Demonstrate test failure vs. success

### 2. **Show Test Organization**
- Explain test file naming conventions
- Demonstrate test classes for grouping
- Show how docstrings help documentation

### 3. **Demonstrate TDD Workflow**
- Write failing test first
- Implement minimum code to pass
- Refactor and improve

### 4. **Explain Testing Best Practices**
- One assertion per test (generally)
- Descriptive test names
- Arrange-Act-Assert pattern
- Test edge cases and error conditions

### 5. **Show Integration with Git**
- Tests run automatically in pre-commit hooks
- CI/CD integration possibilities
- How test failures prevent bad commits

---

## 🚀 Demo Script for Your Session

### Phase 1: Basic Testing (10 minutes)
```bash
# Show simple test
pytest tests/test_calculator.py::TestBasicArithmetic::test_add_positive_numbers -v

# Show test failure by breaking code
# Edit calculator.py to return wrong value, show test fails

# Show test discovery
pytest --collect-only
```

### Phase 2: Advanced Features (10 minutes)
```bash
# Show parametrized tests
pytest tests/test_calculator.py::test_power_parametrized -v

# Show exception testing
pytest tests/test_calculator.py::TestDivision::test_divide_by_zero_raises_exception -v

# Show markers
pytest -m slow -v
pytest -m "not slow" -v
```

### Phase 3: Real-world Testing (10 minutes)
```bash
# Show fixtures and mocking
pytest tests/test_data_processor.py::TestLoadCSVData -v

# Show integration tests
pytest -m integration -v

# Show coverage
pytest --cov=src --cov-report=term-missing
```

---

This comprehensive test suite demonstrates pytest concepts from basic to advanced, providing a solid foundation for explaining testing concepts during your Git training session!
