"""
Data Processing Module

A collection of data processing utilities for demonstration purposes.
This module is used in the Git Advanced Session to demonstrate:
- Data manipulation functions
- Testing with pytest
- Pre-commit hooks with pandas
- Realistic code examples
"""

import pandas as pd
import numpy as np
from typing import List, Dict, Any, Optional
import json
from pathlib import Path


def load_csv_data(file_path: str) -> pd.DataFrame:
    """
    Load data from a CSV file.
    
    Args:
        file_path: Path to the CSV file
        
    Returns:
        DataFrame containing the CSV data
        
    Raises:
        FileNotFoundError: When file doesn't exist
        pd.errors.EmptyDataError: When file is empty
    """
    if not Path(file_path).exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    return pd.read_csv(file_path)


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean a DataFrame by removing null values and duplicates.
    
    Args:
        df: Input DataFrame
        
    Returns:
        Cleaned DataFrame
    """
    # Remove rows with any null values
    cleaned = df.dropna()
    
    # Remove duplicate rows
    cleaned = cleaned.drop_duplicates()
    
    # Reset index
    cleaned = cleaned.reset_index(drop=True)
    
    return cleaned


def filter_by_column(df: pd.DataFrame, column: str, value: Any) -> pd.DataFrame:
    """
    Filter DataFrame by a specific column value.
    
    Args:
        df: Input DataFrame
        column: Column name to filter by
        value: Value to filter for
        
    Returns:
        Filtered DataFrame
        
    Raises:
        KeyError: When column doesn't exist
    """
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not found in DataFrame")
    
    return df[df[column] == value].reset_index(drop=True)


def calculate_statistics(df: pd.DataFrame, column: str) -> Dict[str, float]:
    """
    Calculate basic statistics for a numeric column.
    
    Args:
        df: Input DataFrame
        column: Column name to calculate statistics for
        
    Returns:
        Dictionary containing mean, median, std, min, max
        
    Raises:
        KeyError: When column doesn't exist
        ValueError: When column is not numeric
    """
    if column not in df.columns:
        raise KeyError(f"Column '{column}' not found in DataFrame")
    
    if not pd.api.types.is_numeric_dtype(df[column]):
        raise ValueError(f"Column '{column}' is not numeric")
    
    return {
        'mean': float(df[column].mean()),
        'median': float(df[column].median()),
        'std': float(df[column].std()),
        'min': float(df[column].min()),
        'max': float(df[column].max()),
        'count': int(df[column].count())
    }


def group_by_column(df: pd.DataFrame, group_column: str, agg_column: str, 
                   operation: str = 'mean') -> pd.DataFrame:
    """
    Group DataFrame by a column and aggregate another column.
    
    Args:
        df: Input DataFrame
        group_column: Column to group by
        agg_column: Column to aggregate
        operation: Aggregation operation ('mean', 'sum', 'count', 'min', 'max')
        
    Returns:
        Grouped and aggregated DataFrame
        
    Raises:
        KeyError: When column doesn't exist
        ValueError: When operation is not supported
    """
    if group_column not in df.columns:
        raise KeyError(f"Group column '{group_column}' not found in DataFrame")
    
    if agg_column not in df.columns:
        raise KeyError(f"Aggregation column '{agg_column}' not found in DataFrame")
    
    valid_operations = ['mean', 'sum', 'count', 'min', 'max']
    if operation not in valid_operations:
        raise ValueError(f"Operation '{operation}' not supported. Use one of: {valid_operations}")
    
    grouped = df.groupby(group_column)[agg_column]
    
    if operation == 'mean':
        result = grouped.mean()
    elif operation == 'sum':
        result = grouped.sum()
    elif operation == 'count':
        result = grouped.count()
    elif operation == 'min':
        result = grouped.min()
    elif operation == 'max':
        result = grouped.max()
    
    return result.reset_index()


def save_to_json(data: Dict[str, Any], file_path: str) -> None:
    """
    Save data to a JSON file.
    
    Args:
        data: Dictionary to save
        file_path: Path where to save the JSON file
    """
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=2)


def load_from_json(file_path: str) -> Dict[str, Any]:
    """
    Load data from a JSON file.
    
    Args:
        file_path: Path to the JSON file
        
    Returns:
        Dictionary containing the loaded data
        
    Raises:
        FileNotFoundError: When file doesn't exist
        json.JSONDecodeError: When file contains invalid JSON
    """
    if not Path(file_path).exists():
        raise FileNotFoundError(f"File not found: {file_path}")
    
    with open(file_path, 'r') as f:
        return json.load(f)


def create_sample_data(num_rows: int = 100) -> pd.DataFrame:
    """
    Create sample employee data for demonstration purposes.
    
    Args:
        num_rows: Number of rows to generate
        
    Returns:
        DataFrame with sample employee data
    """
    np.random.seed(42)  # For reproducible results
    
    departments = ['Engineering', 'Sales', 'Marketing', 'HR', 'Finance']
    locations = ['New York', 'San Francisco', 'Chicago', 'Austin', 'Seattle']
    
    data = {
        'employee_id': range(1, num_rows + 1),
        'name': [f'Employee_{i}' for i in range(1, num_rows + 1)],
        'department': np.random.choice(departments, num_rows),
        'location': np.random.choice(locations, num_rows),
        'salary': np.random.normal(75000, 15000, num_rows).round(2),
        'years_experience': np.random.randint(0, 20, num_rows),
        'performance_score': np.random.uniform(1.0, 5.0, num_rows).round(2)
    }
    
    return pd.DataFrame(data)


def validate_data_types(df: pd.DataFrame, expected_types: Dict[str, str]) -> bool:
    """
    Validate that DataFrame columns have expected data types.
    
    Args:
        df: DataFrame to validate
        expected_types: Dictionary mapping column names to expected types
        
    Returns:
        True if all columns have expected types, False otherwise
    """
    for column, expected_type in expected_types.items():
        if column not in df.columns:
            return False
        
        actual_type = str(df[column].dtype)
        
        # Simple type matching (can be enhanced)
        if expected_type == 'numeric' and not pd.api.types.is_numeric_dtype(df[column]):
            return False
        elif expected_type == 'string' and actual_type != 'object':
            return False
        elif expected_type not in actual_type and expected_type != 'numeric' and expected_type != 'string':
            return False
    
    return True
