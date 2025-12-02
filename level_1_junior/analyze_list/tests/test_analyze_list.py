import pytest
from src.main import analyze_list
import math

def test_list_empty():
    """Test that empty list returns empty dictionary."""
    assert analyze_list([]) == {}

def test_type_of_list():
    """Test that non-numeric elements raise TypeError."""
    with pytest.raises(TypeError):
        analyze_list(['Red', 2, 5, 65, 1, 'Green']) 
    with pytest.raises(TypeError):
        analyze_list([1.2, 'Blue', 75.43, 'Gray', 10.3, 43.2])

def test_single_element():
    '''Test list with single element'''
    result = analyze_list([42])
    assert result == {'mean': 42, 'median': 42, 'mode': 42, 'range': 0}


def test_mean_calculation():
    """Test mean calculation with various inputs."""
    # Use math.isclose for floating-point comparisons
    result = analyze_list([1, 1, 1, 1, 1, 1, 1])
    assert result['mean'] == 1
    
    result = analyze_list([3, 3, 65, 21, 3, 76, 98, 3, 21, 3])
    assert math.isclose(result['mean'], 29.6)
    
    result = analyze_list([12, 7, 98, 32, 1.2, 457.76, 1.2, 4.87, 2, 2])
    assert math.isclose(result['mean'], 61.803)


def test_median_calculation():
    """Test median calculation for odd and even length lists."""
    result = analyze_list([1, 2, 3, 4, 5, 5, 5])
    assert result['median'] == 4
    
    result = analyze_list([1, 2, 3, 4])
    assert result['median'] == 2.5

def test_mode_with_multiple_modes():
    """Test mode calculation when multiple values have same frequency."""
    # Should return smallest mode (2, not 3)
    result = analyze_list([1, 2, 2, 3, 3, 4])
    assert result['mode'] == 2
    
    result = analyze_list([5, 5, 6, 6, 7, 7, 7])
    assert result['mode'] == 7  # 7 appears 3 times, others appear 2
    
    result = analyze_list([1, 1, 2, 2, 3])
    assert result['mode'] == 1  # 1 and 2 tie, 1 is smaller


def test_range_calculation():
    """Test range calculation."""
    result = analyze_list([1, 2, 3, 4, 5, 6, 7])
    assert result['range'] == 6
    
    result = analyze_list([20, 231, 5, 8, 43, 1, 3])
    assert result['range'] == 230
    
    result = analyze_list([1.2, 65.3, 76.3, 12.4, 100.0, 1.0])
    assert math.isclose(result['range'], 99.0)


def test_mixed_int_float():
    """Test with mixed integer and float values."""
    result = analyze_list([1, 2.5, 3, 4.5, 5])
    assert math.isclose(result['mean'], 3.2)
    assert result['median'] == 3
    assert result['mode'] == 1  # All appear once, 1 is smallest
    assert math.isclose(result['range'], 4.0)
