"""
Test suite for data_processor module

This test file demonstrates pytest concepts for data processing:
- Testing with pandas DataFrames
- Fixture usage for test data
- Mocking file operations
- Testing data validation
- Exception handling for data operations
"""

import pytest
import pandas as pd
import numpy as np
import json
import tempfile
import os
from pathlib import Path
from unittest.mock import patch, mock_open

from src.data_processor import (
    load_csv_data, clean_data, filter_by_column, calculate_statistics,
    group_by_column, save_to_json, load_from_json, create_sample_data,
    validate_data_types
)


# Fixtures for test data
@pytest.fixture
def sample_dataframe():
    """Fixture providing a sample DataFrame for testing."""
    data = {
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'age': [25, 30, 35, 28, 32],
        'department': ['Engineering', 'Sales', 'Engineering', 'Marketing', 'Sales'],
        'salary': [75000, 65000, 85000, 60000, 70000],
        'years_experience': [3, 5, 8, 2, 6]
    }
    return pd.DataFrame(data)


@pytest.fixture
def dirty_dataframe():
    """Fixture providing a DataFrame with missing values and duplicates."""
    data = {
        'name': ['Alice', 'Bob', None, 'Bob', 'Eve', 'Alice'],
        'age': [25, 30, 35, 30, None, 25],
        'score': [85.5, 90.0, 78.5, 90.0, 88.0, 85.5]
    }
    return pd.DataFrame(data)


@pytest.fixture
def numeric_dataframe():
    """Fixture providing a DataFrame with numeric data for statistics."""
    np.random.seed(42)
    data = {
        'values': [10, 20, 30, 40, 50],
        'scores': [85.5, 90.0, 78.5, 92.0, 88.0],
        'category': ['A', 'B', 'A', 'B', 'A']
    }
    return pd.DataFrame(data)


@pytest.fixture
def temp_csv_file():
    """Fixture creating a temporary CSV file for testing."""
    data = "name,age,city\nAlice,25,NYC\nBob,30,LA\nCharlie,35,Chicago"
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.csv', delete=False) as f:
        f.write(data)
        temp_file = f.name
    
    yield temp_file
    
    # Cleanup
    os.unlink(temp_file)


@pytest.fixture
def temp_json_file():
    """Fixture creating a temporary JSON file for testing."""
    data = {"test": "data", "numbers": [1, 2, 3]}
    
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
        json.dump(data, f)
        temp_file = f.name
    
    yield temp_file
    
    # Cleanup
    os.unlink(temp_file)


class TestLoadCSVData:
    """Test class for CSV loading functionality."""
    
    def test_load_csv_success(self, temp_csv_file):
        """Test successful CSV loading."""
        df = load_csv_data(temp_csv_file)
        
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 3
        assert list(df.columns) == ['name', 'age', 'city']
        assert df.iloc[0]['name'] == 'Alice'
    
    def test_load_csv_file_not_found(self):
        """Test loading non-existent CSV file."""
        with pytest.raises(FileNotFoundError, match="File not found"):
            load_csv_data("nonexistent_file.csv")
    
    @patch('src.data_processor.Path.exists')
    @patch('pandas.read_csv')
    def test_load_csv_empty_file(self, mock_read_csv, mock_exists):
        """Test loading empty CSV file using mock."""
        mock_exists.return_value = True  # File exists
        mock_read_csv.side_effect = pd.errors.EmptyDataError("No data")
        
        with pytest.raises(pd.errors.EmptyDataError):
            load_csv_data("empty_file.csv")


class TestCleanData:
    """Test class for data cleaning functionality."""
    
    def test_clean_data_removes_nulls(self, dirty_dataframe):
        """Test that clean_data removes rows with null values."""
        original_length = len(dirty_dataframe)
        cleaned = clean_data(dirty_dataframe)
        
        assert len(cleaned) < original_length
        assert not cleaned.isnull().any().any()  # No null values remain
    
    def test_clean_data_removes_duplicates(self, dirty_dataframe):
        """Test that clean_data removes duplicate rows."""
        cleaned = clean_data(dirty_dataframe)
        
        # Check that there are no duplicate rows
        assert not cleaned.duplicated().any()
    
    def test_clean_data_resets_index(self, dirty_dataframe):
        """Test that clean_data resets the index."""
        cleaned = clean_data(dirty_dataframe)
        
        # Index should start from 0 and be sequential
        expected_index = list(range(len(cleaned)))
        assert list(cleaned.index) == expected_index
    
    def test_clean_data_empty_dataframe(self):
        """Test cleaning an empty DataFrame."""
        empty_df = pd.DataFrame()
        cleaned = clean_data(empty_df)
        
        assert len(cleaned) == 0
        assert isinstance(cleaned, pd.DataFrame)


class TestFilterByColumn:
    """Test class for column filtering functionality."""
    
    def test_filter_by_column_success(self, sample_dataframe):
        """Test successful filtering by column value."""
        result = filter_by_column(sample_dataframe, 'department', 'Engineering')
        
        assert len(result) == 2  # Alice and Charlie
        assert all(result['department'] == 'Engineering')
        assert 'Alice' in result['name'].values
        assert 'Charlie' in result['name'].values
    
    def test_filter_by_column_no_matches(self, sample_dataframe):
        """Test filtering with value that doesn't exist."""
        result = filter_by_column(sample_dataframe, 'department', 'Nonexistent')
        
        assert len(result) == 0
        assert isinstance(result, pd.DataFrame)
    
    def test_filter_by_column_invalid_column(self, sample_dataframe):
        """Test filtering by non-existent column."""
        with pytest.raises(KeyError, match="Column 'invalid_column' not found"):
            filter_by_column(sample_dataframe, 'invalid_column', 'value')
    
    @pytest.mark.parametrize("column,value,expected_count", [
        ('department', 'Sales', 2),
        ('department', 'Engineering', 2),
        ('department', 'Marketing', 1),
        ('age', 30, 1),
    ])
    def test_filter_by_column_parametrized(self, sample_dataframe, column, value, expected_count):
        """Parametrized test for different filter scenarios."""
        result = filter_by_column(sample_dataframe, column, value)
        assert len(result) == expected_count


class TestCalculateStatistics:
    """Test class for statistics calculation."""
    
    def test_calculate_statistics_success(self, numeric_dataframe):
        """Test successful statistics calculation."""
        stats = calculate_statistics(numeric_dataframe, 'values')
        
        assert isinstance(stats, dict)
        assert 'mean' in stats
        assert 'median' in stats
        assert 'std' in stats
        assert 'min' in stats
        assert 'max' in stats
        assert 'count' in stats
        
        # Check specific values
        assert stats['mean'] == 30.0
        assert stats['median'] == 30.0
        assert stats['min'] == 10.0
        assert stats['max'] == 50.0
        assert stats['count'] == 5
    
    def test_calculate_statistics_invalid_column(self, numeric_dataframe):
        """Test statistics calculation for non-existent column."""
        with pytest.raises(KeyError, match="Column 'invalid' not found"):
            calculate_statistics(numeric_dataframe, 'invalid')
    
    def test_calculate_statistics_non_numeric_column(self, numeric_dataframe):
        """Test statistics calculation for non-numeric column."""
        with pytest.raises(ValueError, match="Column 'category' is not numeric"):
            calculate_statistics(numeric_dataframe, 'category')


class TestGroupByColumn:
    """Test class for grouping operations."""
    
    def test_group_by_column_mean(self, sample_dataframe):
        """Test grouping with mean aggregation."""
        result = group_by_column(sample_dataframe, 'department', 'salary', 'mean')
        
        assert isinstance(result, pd.DataFrame)
        assert len(result) == 3  # Three departments
        assert 'department' in result.columns
        assert 'salary' in result.columns
    
    def test_group_by_column_sum(self, sample_dataframe):
        """Test grouping with sum aggregation."""
        result = group_by_column(sample_dataframe, 'department', 'years_experience', 'sum')
        
        engineering_sum = result[result['department'] == 'Engineering']['years_experience'].iloc[0]
        assert engineering_sum == 11  # Alice(3) + Charlie(8)
    
    def test_group_by_column_invalid_operation(self, sample_dataframe):
        """Test grouping with invalid operation."""
        with pytest.raises(ValueError, match="Operation 'invalid' not supported"):
            group_by_column(sample_dataframe, 'department', 'salary', 'invalid')
    
    def test_group_by_column_invalid_columns(self, sample_dataframe):
        """Test grouping with invalid column names."""
        with pytest.raises(KeyError, match="Group column 'invalid' not found"):
            group_by_column(sample_dataframe, 'invalid', 'salary', 'mean')
        
        with pytest.raises(KeyError, match="Aggregation column 'invalid' not found"):
            group_by_column(sample_dataframe, 'department', 'invalid', 'mean')


class TestJSONOperations:
    """Test class for JSON save/load operations."""
    
    def test_save_to_json(self):
        """Test saving data to JSON file."""
        test_data = {"key": "value", "numbers": [1, 2, 3]}
        
        with tempfile.NamedTemporaryFile(mode='w', suffix='.json', delete=False) as f:
            temp_file = f.name
        
        try:
            save_to_json(test_data, temp_file)
            
            # Verify file was created and contains correct data
            with open(temp_file, 'r') as f:
                loaded_data = json.load(f)
            
            assert loaded_data == test_data
        finally:
            os.unlink(temp_file)
    
    def test_load_from_json_success(self, temp_json_file):
        """Test successful JSON loading."""
        data = load_from_json(temp_json_file)
        
        assert isinstance(data, dict)
        assert data["test"] == "data"
        assert data["numbers"] == [1, 2, 3]
    
    def test_load_from_json_file_not_found(self):
        """Test loading non-existent JSON file."""
        with pytest.raises(FileNotFoundError, match="File not found"):
            load_from_json("nonexistent_file.json")
    
    @patch('builtins.open', mock_open(read_data='{"invalid": json}'))
    def test_load_from_json_invalid_json(self):
        """Test loading invalid JSON file using mock."""
        with patch('pathlib.Path.exists', return_value=True):
            with pytest.raises(json.JSONDecodeError):
                load_from_json("invalid.json")


class TestCreateSampleData:
    """Test class for sample data creation."""
    
    def test_create_sample_data_default(self):
        """Test creating sample data with default parameters."""
        df = create_sample_data()
        
        assert isinstance(df, pd.DataFrame)
        assert len(df) == 100
        assert 'employee_id' in df.columns
        assert 'name' in df.columns
        assert 'department' in df.columns
        assert 'salary' in df.columns
    
    def test_create_sample_data_custom_size(self):
        """Test creating sample data with custom size."""
        df = create_sample_data(50)
        
        assert len(df) == 50
        assert df['employee_id'].max() == 50
    
    def test_create_sample_data_reproducible(self):
        """Test that sample data creation is reproducible."""
        df1 = create_sample_data(10)
        df2 = create_sample_data(10)
        
        # Should be identical due to fixed random seed
        pd.testing.assert_frame_equal(df1, df2)


class TestValidateDataTypes:
    """Test class for data type validation."""
    
    def test_validate_data_types_success(self, sample_dataframe):
        """Test successful data type validation."""
        expected_types = {
            'name': 'string',
            'age': 'numeric',
            'salary': 'numeric'
        }
        
        result = validate_data_types(sample_dataframe, expected_types)
        assert result is True
    
    def test_validate_data_types_failure(self, sample_dataframe):
        """Test data type validation failure."""
        expected_types = {
            'name': 'numeric',  # This should fail
            'age': 'numeric'
        }
        
        result = validate_data_types(sample_dataframe, expected_types)
        assert result is False
    
    def test_validate_data_types_missing_column(self, sample_dataframe):
        """Test validation with missing column."""
        expected_types = {
            'nonexistent_column': 'numeric'
        }
        
        result = validate_data_types(sample_dataframe, expected_types)
        assert result is False


# Integration test combining multiple functions
@pytest.mark.integration
def test_data_processing_workflow(temp_csv_file):
    """Integration test for complete data processing workflow."""
    # Load data
    df = load_csv_data(temp_csv_file)
    
    # Clean data (though this CSV is already clean)
    cleaned_df = clean_data(df)
    
    # Filter data
    filtered_df = filter_by_column(cleaned_df, 'city', 'NYC')
    
    # Validate the workflow
    assert len(filtered_df) == 1
    assert filtered_df.iloc[0]['name'] == 'Alice'


# Performance test example
@pytest.mark.slow
def test_large_dataframe_processing():
    """Test processing of large DataFrame (marked as slow)."""
    # Create a large DataFrame
    large_df = create_sample_data(10000)
    
    # Test that operations complete successfully
    cleaned = clean_data(large_df)
    stats = calculate_statistics(cleaned, 'salary')
    
    assert len(cleaned) <= 10000  # Should be same or smaller after cleaning
    assert 'mean' in stats


if __name__ == "__main__":
    # Run tests when script is executed directly
    pytest.main([__file__])
