from convert_temperature.src.main import convert_temperature
import pytest

def test_celsius_to_fahrenheit():
    """Test conversion from Celsius to Fahrenheit."""
    assert convert_temperature(0, 'C', 'F') == 32.0
    assert convert_temperature(100, 'C', 'F') == 212.0
    assert convert_temperature(-40, 'C', 'F') == -40.0

def test_fahrenheit_to_celsius():
    """Test conversion from Fahrenheit to Celsius"""
    assert convert_temperature(32, 'F', 'C') == 0.0
    assert convert_temperature(212, 'F', 'C') == 100.0
    assert convert_temperature(-40, 'F', 'C') == -40.0

def test_same_scale():
    """Test that same scale returns original value."""
    assert convert_temperature(25, 'C', 'C') == 25.0
    assert convert_temperature(77, 'F', 'F') == 77.0

def test_invalid_scales():
    """Test that invalid scales raise ValueError."""
    with pytest.raises(ValueError):
        convert_temperature(100, 'X', 'F')
        
    with pytest.raises(ValueError):
        convert_temperature(100, 'C', 'K')

def test_case_insensitive():
    """Test that scales are case-insensitive."""
    assert convert_temperature(0, 'c', 'f') == 32.0
    assert convert_temperature(32, 'f', 'c') == 0.0
    