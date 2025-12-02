# Importing required types for docstring documentation
from typing import Union, Dict, List
# Required library for view the most frequent value
from collections import Counter

def analyze_list(
    numbers: List[Union[int, float]]
    ) -> Dict[str, Union[int, float]]:
    """
    Calculate statistical measures for a list of numbers.
    
    Args:
        numbers: List of integers or floating-point numbers.
        
    Returns:
        Dictionary containing:
        - 'mean': Average value of the numbers
        - 'median': Middle value when numbers are sorted
        - 'mode': Mmost frequent value (if multiple, returns smallest)
        - 'range': Difference between maximum and minium values 

    Raises:
        TypeError: If any element in the list is not int or float

    Examples:
        >>> analyze_list([1, 2, 3, 4, 5, 5, 5])
        {'mean': 3.571..., 'median': 4, 'mode': 5, 'range': 4}
        
        >>> analyze_list([1, 2, 2, 3, 3, 4])
        {'mean': 2.5, 'median': 2.5, 'mode': 2, 'range': 3}
    """
    
    # Handle empty list
    if not numbers:
        return {}

    # Validate all elements are numeric
    valid_types = (float, int)
    for i, value in enumerate(numbers):
        if not isinstance(value, valid_types):
            raise TypeError(
                f"Element at index {i} has type {type(value).__name__}."
                f"Only int and float are allowed."
                )
    
    # Sort for median calculation
    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    # Calculate mean
    mean = sum(sorted_numbers) / n

    if n % 2 == 1: # Odd length
        median = sorted_numbers[n // 2]
    else: # Even length
        mid_right = n // 2
        mid_left = mid_right - 1
        median = (sorted_numbers[mid_left] + sorted_numbers[mid_right]) / 2 

    # Calculate mode (with custom logic for multiple modes)
    counter = Counter(sorted_numbers)
    max_frequency = max(counter.values()) 

    # Find all values with max frequency, then get the smallest
    modes = [value for value, freq in counter.items() if freq == max_frequency]
    mode = min(modes) # Smallest value among modes

    # Calculate range (avoid using 'range' as variable name)
    value_range = max(sorted_numbers) - min(sorted_numbers)
    
    return {
        'mean' : mean,
        'median' : median,
        'mode' : mode,
        'range' : value_range
        }

